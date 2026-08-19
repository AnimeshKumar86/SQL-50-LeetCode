class Solution(object):

  def findCenter(self, edges):
   
    # Pehli edge: edges[0] = [u1, v1]
    # Dusri edge: edges[1] = [u2, v2]

    # Check karo ki edges[0] ka pehla element dusri edge mein hai ya nahi
    if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
      return edges[0][0]

    # Agar edges[0][0] common nahi hai, toh edges[0][1] hi center hoga
    return edges[0][1]
        