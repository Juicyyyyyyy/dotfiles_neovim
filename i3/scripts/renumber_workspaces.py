#!/usr/bin/env python3

import i3ipc

def renumber_workspaces(i3, event=None):
    workspaces = i3.get_workspaces()
    
    # Sort workspaces by their current number (num)
    sorted_workspaces = sorted(workspaces, key=lambda ws: ws.num)
    
    # Renumber workspaces sequentially
    for i, ws in enumerate(sorted_workspaces, start=1):
        if ws.name != str(i):
            print(f'Renaming workspace {ws.name} to {i}')
            i3.command(f'rename workspace "{ws.name}" to "{i}"')

if __name__ == "__main__":
    i3 = i3ipc.Connection()

    # Renumber once at startup
    renumber_workspaces(i3)

    # Attach listeners
    i3.on("workspace::focus", renumber_workspaces)
    i3.on("workspace::empty", renumber_workspaces)
    i3.on("window::close", renumber_workspaces)

    # Start event listener
    i3.main()
