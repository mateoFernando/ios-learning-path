// import CoreLocation
func rankByWalkingTime(
    _ restaurants: [Restaurant],
    from origin: CLLocationCoordinate2D
) async throws -> [Ranked] {
    var ranked: [Ranked] = []

    try await withThrowingTaskGroup(of: Void.self) { group in
        for r in restaurants {
            group.addTask {
                let min = try await router.walkingMinutes(
                    from: origin, to: r.coordinate
                )
                // ❌ Mutation of captured var 'ranked'
                //    in concurrently-executing code
                ranked.append(.init(r, min))
            }
        }
        try await group.waitForAll()
    }
    return ranked.sorted { $0.minutes < $1.minutes }
}
