// import CoreLocation
func rankByWalkingTime(
    _ restaurants: [Restaurant],
    from origin: CLLocationCoordinate2D
) async throws -> [Ranked] {
    try await withThrowingTaskGroup(of: Ranked.self) { group in
        for r in restaurants {
            group.addTask {
                let min = try await router.walkingMinutes(
                    from: origin, to: r.coordinate
                )
                return .init(r, min)          // ✅ devuelve
            }
        }
        var ranked: [Ranked] = []
        for try await item in group { // ✅ el padre recoge
            ranked.append(item)
        }
        return ranked.sorted { $0.minutes < $1.minutes }
    }
}
