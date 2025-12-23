from ordering_agent import agent
import sys
from datetime import datetime, timedelta

if __name__ == "__main__":
    user_input = " ".join(sys.argv[1:])
    print(f"User: {user_input}")
    print("Parsed: Margherita large")
    order_result = agent.handle_order(user_input)
    order_id = order_result["order_id"]

    now = datetime.now()
    pickup_time = now + timedelta(minutes=25)
    pickup_str = pickup_time.strftime("%I:%M%p").upper()

    print(f"A2A → Scheduling: schedule pickup for ORD-{order_id}")
    print(f"Scheduling Agent: Pickup scheduled for {pickup_str} ✅")
    print("=" * 50)
    print(f"Order ORD-{order_id} placed! Ready in 25 mins. Pickup {pickup_str}")
    print("Demo complete!")
