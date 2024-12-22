canvas.grid(row=0, column=0, rowspan=6, padx=10, pady=10)
canvas.bind("<Button-1>", add_waypoint)
canvas.bind("<ButtonPress-3>", on_starting_box_press)
canvas.bind("<B3-Motion>", on_starting_box_drag)
canvas.bind("<ButtonRelease-3>", on_starting_box_release)

# Default background image
field_image_path = os.path.join(current_directory, "field.png")
if os.path.exists(field_image_path):
    field_image = Image.open(field_image_path).resize((FIELD_PIXELS, FIELD_PIXELS))
    field_photo = ImageTk.PhotoImage(field_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=field_photo)
    canvas.image = field_photo

# Draw initial starting box
redraw_starting_box()

# Waypoints display
waypoint_list = tk.Text(root, width=25, height=20)
waypoint_list.grid(row=0, column=1, padx=10, pady=10)

# Buttons
tk.Button(root, text="Clear", command=clear_waypoints).grid(row=1, column=1, pady=5)
tk.Button(root, text="Load JSON", command=load_json).grid(row=2, column=1, pady=5)

# Save Buttons for Corners
for i, corner in enumerate(corner_files.keys()):
    tk.Button(root, text=f"Save {corner}", command=lambda c=corner: save_to_json(c)).grid(row=3+i, column=1, pady=5)

# Run the app
root.mainloop()