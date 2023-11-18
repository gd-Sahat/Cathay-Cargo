from py3dbp import Packer, Bin, Item

# Define the cargo plane dimensions
cargo_plane_length = 80
cargo_plane_width = 80
cargo_plane_height = 120

# Create a Packer instance
packer = Packer()

# Create a Bin representing the cargo plane
bin = Bin("Cargo Plane", cargo_plane_length, cargo_plane_width, cargo_plane_height, max_weight= 1000)

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