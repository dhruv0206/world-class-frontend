#!/bin/bash
# Run for a specified duration to process queue automatically
# Usage: ./scripts/batch_runner.sh <seconds> (default: 10800 for 3 hours)

DURATION=${1:-10800}
END=$((SECONDS+DURATION))

echo "Starting batch run of frontend-taste-learner for $DURATION seconds..."

while [ $SECONDS -lt $END ]; do
    echo "Starting fresh iteration..."
    
    # Must use 'chat' command and load the required skills directly with --yolo to bypass confirmation
    OUTPUT=$(hermes chat "run frontend-taste-learner" --skills frontend-taste-learner --yolo 2>&1)
    
    if echo "$OUTPUT" | grep -qi "Queue complete"; then
        echo "Queue is empty. Stopping batch run."
        break
    fi
    
    echo "Iteration complete. Pausing for 10 seconds before the next site..."
    sleep 10
done

echo "Batch run completed."
