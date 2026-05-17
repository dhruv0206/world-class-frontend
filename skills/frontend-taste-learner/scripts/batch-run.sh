#!/bin/bash
# Usage: bash scripts/batch-run.sh [duration_in_seconds]
# Loops the frontend-taste-learner skill autonomously.

DURATION=${1:-10800} # Default to 3 hours
END=$((SECONDS+DURATION))

echo "Starting batch run of frontend-taste-learner for $DURATION seconds..."

while [ $SECONDS -lt $END ]; do
    echo "Starting fresh iteration at $(date)..."
    OUTPUT=$(hermes chat "run frontend-taste-learner" --skills frontend-taste-learner --yolo 2>&1)
    
    # Check if the agent reported the queue is empty
    if echo "$OUTPUT" | grep -qi "Queue complete"; then
        echo "Queue is empty. Stopping batch run."
        break
    fi
    
    echo "Iteration complete. Pausing for 10 seconds before the next site..."
    sleep 10
done

echo "Batch run completed at $(date)."
