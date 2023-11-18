from py3dbp import *
import pandas as pd
import random


packer = Packer()
# Define the container dimensions (length, width, height)
conex = Bin("Conex Container", (120, 96, 102), 10000, 0, 0)
packer.addBin(conex)

# Load item details from Excel file
item_list = "C:/Users/ParsonsJS/Container Stuff/Spares carton dimensions.xlsx"
item_df = pd.read_excel(item_list)

# Adjust df to fit Item class with appropriate columns
# Define the columns to check for existence
columns_to_check = ['Importance', 'Loadbear', 'Updown', 'Color', 'Typeof']

# Check if columns exist and add them if they don't
for column in columns_to_check:
    if column not in item_df.columns:
        if column == 'Importance':
            item_df[column] = 1
        elif column == 'Loadbear':
            item_df[column] = 100
        elif column == 'Updown':
            item_df[column] = 'TRUE'
        elif column == 'Typeof':
            item_df[column] = 'cube'
        elif column == 'Color':
            num_rows = len(item_df)
            colors = [
                '#{:02x}{:02x}{:02x}'.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for
                _ in range(num_rows)]
            item_df[column] = colors

# Create the WHD tuple column from Final Length, Width, and Height
item_df['WHD'] = item_df.apply(lambda row: (row['Final Length'], row['Final Height'], row['Final Width']), axis=1)

# Add each part to the packer
for index, row in item_df.iterrows():
    item = Item(row['Part #'], row['Name'], row['Typeof'], row['WHD'], row['Unit weight'], row['Importance'],
                row['Loadbear'], row['Updown'], row['Color'])
    if not item.getVolume().is_nan():
        packer.addItem(item)
    else:
        print(row["Name"] + " has no Shipping dimensions")

# calculate packing
packer.pack(
    bigger_first=True,
    distribute_items=False,
    fix_point=True,
    check_stable=True,
    support_surface_ratio=0.75,
    number_of_decimals=2
)

# put order
packer.putOrder()

# print result
b = packer.bins[0]
print("***************************************************")
for idx, b in enumerate(packer.bins):
    print("**", b.string(), "**")
    print("***************************************************")
    print("FITTED ITEMS:")
    print("***************************************************")
    volume = b.width * b.height * b.depth
    volume_t = 0
    volume_f = 0
    weight_t = 0
    unfitted_name = ''
    for item in b.items:
        print("partno : ", item.partno)
        print("color : ", item.color)
        print("position : ", item.position)
        print("rotation type : ", item.rotation_type)
        print("W*H*D : ", str(item.width) + ' * ' + str(item.height) + ' * ' + str(item.depth))
        print("volume : ", float(item.width) * float(item.height) * float(item.depth))
        print("weight : ", float(item.weight))
        volume_t += float(item.width) * float(item.height) * float(item.depth)
        weight_t += float(item.weight)
        print("***************************************************")

    print('space utilization : {}%'.format(round(volume_t / float(volume) * 100, 2)))
    print('residual volumn : ', float(volume) - volume_t)
    print("gravity distribution : ", b.gravity)
    print('total weight of container:', weight_t)
    print("***************************************************")
    # draw results
    painter = Painter(b)
    fig = painter.plotBoxAndItems(
        title=b.partno,
        alpha=0.9,
        write_num=False,
        fontsize=10
    )

print("***************************************************")
print("UNFITTED ITEMS:")
for item in packer.unfit_items:
    volume_f += float(item.width) * float(item.height) * float(item.depth)
    unfitted_name += '{},'.format(item.name)
#     print("***************************************************")
print("***************************************************")
print('unpack item : ', unfitted_name)
print('unpack item volumn : ', volume_f)

# fig.show()

# Add List GUI
