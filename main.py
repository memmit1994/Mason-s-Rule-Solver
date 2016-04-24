from functions import *



edges ={
    1:[2,4],
    2:[2,3],
    3:[3,4],
    4:[]
#         1:[2],
#         2:[5,3],
#         3:[4],
#         4:[6],
#         5:[5,6],
#         6:[7],
#         7:[]
         }
gains={
    (1,2):'b',
    (2,2):'c',
    (2,3):'d',
    (3,3):'e',
    (3,4):'f',
    (1,4):'a'
    # (1,2):'a',
    # (2,3):'b',
    # (3,4):'c',
    # (4,6):'d',
    # (6,7):'e',
    # (2,5):'f',
    # (5,5):'g',
    # (5,6):'h'
}





# # get number of nodes
# numberOfNodes = input("\nPlease enter the number of nodes in your SFG: ")
#
# # edge list dictionary with nodes as keys and list of edges as value
#
# # get edges
# for i in range(numberOfNodes):
#     edgesAsString = raw_input("Enter nodes that are connected to (out from) node #" + str(i + 1)+" separated by spaces: ")
#
#     edges[i+1]= StringListToNums(removeEmptyStrings(edgesAsString.split(" "))) if len(edgesAsString)!= 0 else []
#
#
# gains = {}
# #get gains
# for x in edges.keys():
#     gainsX = edges[x]
#     gainsX = [] if gainsX is None else gainsX
#     for i in gainsX:
#         gains[(x,i)]=raw_input("Enter the gain of node "+str(x)+" => "+str(i)+": ")






paths,cycles = [],getCycles(edges)

getPaths(1, len(edges.keys()), edges, [], paths)
print '\nforward Paths : \n\n' + str(paths)

nonTouching = {}
getNonTouching(cycles,1,nonTouching)

print "\nLevels Of Non Touching Loops : \n"
print nonTouching
print "\n\n"
print "\n                         "+getNumerator(cycles,paths,gains)+"\n"
print " Transfer Function = ___________________________________________________________________ \n"
print "\n                         "+getDelta(nonTouching,gains)
