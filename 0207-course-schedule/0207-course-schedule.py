from collections import defaultdict, deque


class Solution(object):

  def canFinish(self, numCourses, prerequisites):

    adj = defaultdict(list)
    in_degree = [0] * numCourses

    for dest, src in prerequisites:
      adj[src].append(dest)  
      in_degree[dest] += 1

    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    completed_courses = 0

    while queue:
      course = queue.popleft()
      completed_courses += 1

      for next_course in adj[course]:
        in_degree[next_course] -= 1
        if in_degree[next_course] == 0:
          queue.append(next_course)

    # Agar saare courses complete ho gaye toh True
    return completed_courses == numCourses
        