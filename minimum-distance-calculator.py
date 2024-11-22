def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2) ** 0.5

points = [(0, 0), (1, 1), (3, 4), (6, 8), (2, 1)]

distances = []

for a in range(len(points)):
    for b in range(a + 1, len(points)):  
        dist = euclideanDistance(points[a], points[b])
        distances.append(dist)
        print(f"Distance between {points[a]} and {points[b]}: {dist}")

min_distance = min(distances)

print("Distances:", distances)
print("Minimum Distance:", min_distance)