import matplotlib.pyplot as plt
from py3dbp import Packer, Bin, Item
import numpy as np

# Define the cargo pallet dimensions
cargo_DG_length = 60
cargo_DG_width = 60
cargo_DG_height = 100

cargo_GEN_length = 100
cargo_GEN_width = 100
cargo_GEN_height = 200

cargo_OTHER_length = 80
cargo_OTHER_width = 80
cargo_OTHER_height = 120

# Create a Packer instance
packer = Packer()

# Create a Bin representing the cargo plane
dg = Bin("Cargo DG", cargo_DG_length, cargo_DG_width, cargo_DG_height, max_weight= 1000)
gen = Bin("Cargo GEN", cargo_GEN_length, cargo_GEN_width, cargo_GEN_height, max_weight= 1000)
other = Bin("Cargo OTHER", cargo_OTHER_length, cargo_OTHER_width, cargo_OTHER_height, max_weight= 1000)



flag=False
i=0
j=0
k=0
while flag==False:
    print("Please input type of good (dg,gen) or q for finished")
    Typeofgood=input()
    if Typeofgood=='q':
        flag=True
    else:
        print(" Please enter length of good ")
        depth=input()
        print(" Please enter width of good ")
        width=input()
        print(" Please enter height of good ")
        height=input()
        print(" Please enter weight of good ")
        weight=input()

        if Typeofgood == 'dg':
            print (" Good assigned to Dangerous Goods Cargo ")

            packer.pack_to_bin(dg, Item("Box "+str(i), depth,width,height,weight))

            # if i==0:
            #     dg=np.array(["box "+str(i),length,width,height,weight])
            # else:
            #     row_to_be_added = np.array([length,width,height,weight])
            #     dg = np.vstack ((dg, row_to_be_added) )
            #DGpacker.add_item(Item("Box "+str(i), length,width,height,weight))
            i=+1
        elif Typeofgood== 'gen':
            print(" Good assigned to General Goods Cargo ")
            packer.pack_to_bin(gen, Item("Box "+str(j), depth,width,height,weight))

            # if j ==0:
            #     gen=np.array([length,width,height,weight])
            # else:
            #     row_to_be_added = np.array([length,width,height,weight])
            #     gen = np.vstack ((gen, row_to_be_added) )
            j=+1
        else:
            print(" Goods have to been transferred to Miscallaneous Goods Cargo ")
            packer.pack_to_bin(other, Item("Box "+str(k), depth,width,height,weight))

            # if k ==0:
            #     ms=np.array([length,width,height,weight])
            # else:
            #     row_to_be_added = np.array([length,width,height,weight])
            #     ms = np.vstack ((ms, row_to_be_added) )
            k=+1
# # Create the dataset of cargo boxes

# cargo_boxes = [
#     Item("Box 1", 30, 20, 40, 100),
#     Item("Box 2", 50, 30, 60, 100),
#     Item("Box 3", 40, 40, 50, 400),
#     # Add more cargo boxes as needed
# ]

# # Add cargo boxes to the packer
# for box in cargo_boxes:
#     packer.add_item(box)

# # Add the cargo plane bin to the packer
# packer.add_bin(bin)

# Pack the cargo boxes into the cargo plane
# packer.pack()

# Retrieve the packed boxes and their positions


    # Output the optimal cargo arrangement
for packed_ULD in [dg, gen, other]:
    print(f"-----{packed_ULD.name}-----")
    packed_boxes = packed_ULD.items
    # Output the optimal cargo arrangement
    for i, box in enumerate(packed_boxes):
        # draw the plots of x-y plot on plt
        plt.plot([0, 0], [0, packed_ULD.width], color='b')
        plt.plot([0, packed_ULD.depth], [packed_ULD.width, packed_ULD.width], color='b')
        plt.plot([packed_ULD.depth, packed_ULD.depth], [packed_ULD.width, 0], color='b')
        plt.plot([packed_ULD.depth, 0], [0, 0], color='b')
        plt.title(f"Box {i+1}")

        print(f"Box {i+1}: Name={box.name}, Position=({box.position[0]}, {box.position[1]}, {box.position[2]})")
        # use matplotlib to plot the results from the packer following the sequence of the boxes
        plt.plot([box.position[0], box.position[0]], [box.position[1], box.position[1] + box.width], color='r')
        plt.plot([box.position[0], box.position[0] + box.depth], [box.position[1] + box.width, box.position[1] + box.width], color='r')
        plt.plot([box.position[0] + box.depth, box.position[0] + box.depth], [box.position[1] + box.width, box.position[1]], color='r')
        plt.plot([box.position[0] + box.depth, box.position[0]], [box.position[1], box.position[1]], color='r')
        # plt.text(box.position[0], box.position[1], box.position[2], box.name, fontsize=12)
        plt.show()
        # close the plot
        plt.close()

    # Calculate space utilization
    total_packed_volume = sum(box.get_volume() for box in packed_boxes)
    cargo_plane_volume = packed_ULD.get_volume()
    space_utilization = total_packed_volume / cargo_plane_volume
    print(f"Space Utilization: {space_utilization * 100}%")

