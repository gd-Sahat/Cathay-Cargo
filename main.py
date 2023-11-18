from py3dbp import Packer, Bin, Item
import pandas as pd
import numpy as np

# Define the cargo plane dimensions
cargo_plane_length = 80
cargo_plane_width = 80
cargo_plane_height = 120

# Create a Packer instance
packer = Packer()

# Create a Bin representing the cargo plane
bin = Bin("Cargo Plane", cargo_plane_length, cargo_plane_width, cargo_plane_height, max_weight= 1000)

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
        length=input()
        print(" Please enter width of good ")
        width=input()
        print(" Please enter height of good ")
        height=input()
        print(" Please enter weight of good ")
        weight=input()

        if Typeofgood == 'dg':
            print (" Good assigned to Dangerous Goods Cargo ")
            if i==0:
                dg=np.array([length,width,height,weight])
            else:
                row_to_be_added = np.array([length,width,height,weight])
                dg = np.vstack ((dg, row_to_be_added) )
            i=+1
        elif Typeofgood== 'gen':
            print(" Good assigned to General Goods Cargo ")
            if j ==0:
                gen=np.array([length,width,height,weight])
            else:
                row_to_be_added = np.array([length,width,height,weight])
                gen = np.vstack ((gen, row_to_be_added) )
            j=+1
        else:
            print(" Goods have to been transferred to Miscallaneous Goods Cargo ")
            if k ==0:
                ms=np.array([length,width,height,weight])
            else:
                row_to_be_added = np.array([length,width,height,weight])
                ms = np.vstack ((ms, row_to_be_added) )
            k=+1

# Create the dataset of cargo boxes
cargo_boxes = [
    Item("Box 1", 30, 20, 40, 100),
    Item("Box 2", 50, 30, 60, 100),
    Item("Box 3", 40, 40, 50, 400),
    # Add more cargo boxes as needed
]

# Add cargo boxes to the packer
for box in cargo_boxes:
    packer.add_item(box)

# Add the cargo plane bin to the packer
packer.add_bin(bin)

# Pack the cargo boxes into the cargo plane
packer.pack()

# Retrieve the packed boxes and their positions


# Output the optimal cargo arrangement
packed_boxes = packer.bins[0].items

# Output the optimal cargo arrangement
for i, box in enumerate(packed_boxes):
    print(f"Box {i+1}: Name={box.name}, Position=({box.position[0]}, {box.position[1]}, {box.position[2]})")

# Calculate space utilization
total_packed_volume = sum(box.get_volume() for box in packed_boxes)
cargo_plane_volume = cargo_plane_length * cargo_plane_width * cargo_plane_height
space_utilization = total_packed_volume / cargo_plane_volume
print(f"Space Utilization: {space_utilization * 100}%")