class Solution(object):
    def findMinArrowShots(self, points):
        
        if not points: return 0

        points = sorted(points, key=lambda x:x[1])
        
        count = 1
        left = points[0][1]
        
        for i in points:
            if(i[0]>left):
                count += 1
                left = i[1]
        
        return count