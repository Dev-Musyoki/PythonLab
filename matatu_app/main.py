from matatu import (
    InvalidFareError,
    RouteNotFoundError,
    get_fare,
    load_routes,
    log_event,
    save_routes,
)


def main():
    routes = [
        {"route_no": "58",  "name": "CBD - Rongai",     "fare": 100},
        {"route_no": "111", "name": "CBD - Kikuyu",     "fare": 80},
        {"route_no": "24",  "name": "CBD - Kawangware", "fare": -5},   # bad data on purpose
    ]
    save_routes(routes, "routes.json")
    loaded = load_routes("routes.json")
    print(f"Loaded {len(loaded)} routes")

    for route_no in ["58", "24", "46"]:
        try:
            fare = get_fare(loaded, route_no)
        except RouteNotFoundError as e:
            print(f"Not found -> {e}")
            log_event(f"Lookup failed: {e}")
        except InvalidFareError as e:
            print(f"Bad data -> {e}")
            log_event(f"Lookup failed: {e}")
        else:                                  # runs only if NO exception happened
            print(f"Route {route_no}: Ksh {fare}")
        finally:                               # runs always
            print("  (lookup finished)")

    print(load_routes("missing.json"))         # file that doesn't exist

    print("Log file contents:")
    with open("matatu_log.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())

if __name__ == "__main__":
    main()