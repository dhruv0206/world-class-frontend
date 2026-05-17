#!/bin/bash
echo "Starting exhaustive batch run of frontend-taste-learner..."
echo "This will run continuously until the queue is empty."

while true; do
    echo "Starting fresh iteration..."
    OUTPUT=$(hermes chat "run frontend-taste-learner" --skills frontend-taste-learner --yolo 2>&1)
    
    # Check if the agent reported the queue is empty
    if echo "$OUTPUT" | grep -qi "Queue complete"; then
        echo "Queue is empty. Stopping batch run."
        break
    fi
    
    echo "Iteration complete. Pausing for 15 seconds before the next site..."
    sleep 15
done

echo "Exhaustive batch run completed! All sites processed."
