# Complete Unified Order Example
def master_factory(required_id, *args, status="Pending", **kwargs):
    print("Required ID:", required_id)
    print("Extra Args Tuple:", args)
    print("Status Flag:", status)
    print("Extra Kwargs Dict:", kwargs)

master_factory(101, "Extra1", "Extra2", status="Active", location="India", score=95)