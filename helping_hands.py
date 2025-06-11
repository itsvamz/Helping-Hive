import reflex as rx
from typing import Dict, List, Set, Optional

# Sample data dictionaries
CSTN_TO_CFSH = {
    "customer1": ["cfsh1", "cfsh2", "cfsh3"],
    "customer2": ["cfsh4", "cfsh5"],
    "customer3": ["cfsh6", "cfsh7", "cfsh8", "cfsh9"],
}

CFSH_TO_ENGINES = {
    "cfsh1": ["engine1", "engine2"],
    "cfsh2": ["engine3", "engine4", "engine5"],
    "cfsh3": ["engine6"],
    "cfsh4": ["engine7", "engine8"],
    "cfsh5": ["engine9"],
    "cfsh6": ["engine10", "engine11"],
    "cfsh7": ["engine12"],
    "cfsh8": ["engine13", "engine14", "engine15"],
    "cfsh9": ["engine16"],
}

ENGINE_TO_GROUPS = {
    "engine1": ["group1"],
    "engine2": ["group1"],
    "engine3": ["group2"],
    "engine4": ["group1"],
    "engine5": ["group4"],
    "engine6": ["group1"],
    "engine7": ["group2"],
    "engine8": ["group1"],
    "engine9": ["group3"],
    "engine10": ["group1"],
    "engine11": ["group4"],
    "engine12": ["group2"],
    "engine13": ["group1"],
    "engine14": ["group2"],
    "engine15": ["group3"],
    "engine16": ["group1"],
}

GROUP_TO_STACKS = {
    "group1": ["stack1", "stack2", "stack3"],
    "group2": ["stack4", "stack5"],
    "group3": ["stack6", "stack7", "stack8"],
    "group4": ["stack9", "stack10"],
}

# Information for sidebar
CSTN_INFO = {
    "customer1": ["Region: North America", "Tier: Premium", "Contact: john@customer1.com"],
    "customer2": ["Region: Europe", "Tier: Standard", "Contact: mary@customer2.com"],
    "customer3": ["Region: Asia", "Tier: Enterprise", "Contact: zhang@customer3.com"],
}

CFSH_INFO = {
    "cfsh1": ["Status: Active", "Location: US-East", "Capacity: 100GB"],
    "cfsh2": ["Status: Active", "Location: US-West", "Capacity: 250GB"],
    "cfsh3": ["Status: Maintenance", "Location: EU-Central", "Capacity: 500GB"],
    "cfsh4": ["Status: Active", "Location: EU-West", "Capacity: 150GB"],
    "cfsh5": ["Status: Active", "Location: Asia-Pacific", "Capacity: 300GB"],
    "cfsh6": ["Status: Active", "Location: US-Central", "Capacity: 200GB"],
    "cfsh7": ["Status: Inactive", "Location: EU-North", "Capacity: 100GB"],
    "cfsh8": ["Status: Active", "Location: Asia-East", "Capacity: 400GB"],
    "cfsh9": ["Status: Active", "Location: US-South", "Capacity: 180GB"],
}

ENGINE_INFO = {
    "engine1": ["Version: 2.1.0", "CPU: 4 cores", "Memory: 8GB"],
    "engine2": ["Version: 2.0.5", "CPU: 2 cores", "Memory: 4GB"],
    "engine3": ["Version: 2.1.2", "CPU: 8 cores", "Memory: 16GB"],
    "engine4": ["Version: 2.0.8", "CPU: 4 cores", "Memory: 8GB"],
    "engine5": ["Version: 2.1.1", "CPU: 6 cores", "Memory: 12GB"],
    "engine6": ["Version: 2.0.9", "CPU: 2 cores", "Memory: 4GB"],
    "engine7": ["Version: 2.1.0", "CPU: 4 cores", "Memory: 8GB"],
    "engine8": ["Version: 2.0.7", "CPU: 8 cores", "Memory: 16GB"],
    "engine9": ["Version: 2.1.3", "CPU: 2 cores", "Memory: 4GB"],
    "engine10": ["Version: 2.0.6", "CPU: 4 cores", "Memory: 8GB"],
    "engine11": ["Version: 2.1.0", "CPU: 6 cores", "Memory: 12GB"],
    "engine12": ["Version: 2.0.8", "CPU: 2 cores", "Memory: 4GB"],
    "engine13": ["Version: 2.1.2", "CPU: 8 cores", "Memory: 16GB"],
    "engine14": ["Version: 2.0.9", "CPU: 4 cores", "Memory: 8GB"],
    "engine15": ["Version: 2.1.1", "CPU: 2 cores", "Memory: 4GB"],
    "engine16": ["Version: 2.0.7", "CPU: 6 cores", "Memory: 12GB"],
}

# Add STACK_INFO dictionary after other info dictionaries
STACK_INFO = {
    "stack1": ["Type: Production", "Version: 1.0.0", "Status: Active"],
    "stack2": ["Type: Staging", "Version: 1.1.0", "Status: Active"],
    "stack3": ["Type: Development", "Version: 1.2.0", "Status: Active"],
    "stack4": ["Type: Production", "Version: 2.0.0", "Status: Active"],
    "stack5": ["Type: Staging", "Version: 2.1.0", "Status: Active"],
    "stack6": ["Type: Development", "Version: 2.2.0", "Status: Active"],
    "stack7": ["Type: Production", "Version: 3.0.0", "Status: Active"],
    "stack8": ["Type: Staging", "Version: 3.1.0", "Status: Active"],
    "stack9": ["Type: Development", "Version: 3.2.0", "Status: Active"],
    "stack10": ["Type: Production", "Version: 4.0.0", "Status: Active"],
}

class State(rx.State):
    # Top row state
    selected_cstn: str = list(CSTN_TO_CFSH.keys())[0]
    
    # CFSH and engines state
    selected_engine: str = ""
    selected_cfsh: str = ""
    
    # Search and groups state
    search_term: str = ""
    selected_group: str = ""
    selected_stack: str = ""
    
    # Sidebar state
    sidebar_visible: bool = False
    cstn_dropdown_open: bool = False
    cfsh_dropdown_open: str = ""
    engine_dropdown_open: str = ""
    stack_dropdown_open: bool = False
    group_dropdown_open: bool = False
    
    def toggle_sidebar(self):
        self.sidebar_visible = not self.sidebar_visible
    
    def toggle_stack_dropdown(self):
        self.stack_dropdown_open = not self.stack_dropdown_open
        self.cstn_dropdown_open = False
        self.cfsh_dropdown_open = ""
        self.engine_dropdown_open = ""
        self.group_dropdown_open = False
    
    def toggle_group_dropdown(self):
        self.group_dropdown_open = not self.group_dropdown_open
        self.cstn_dropdown_open = False
        self.cfsh_dropdown_open = ""
        self.engine_dropdown_open = ""
        self.stack_dropdown_open = False
    
    def toggle_cstn_dropdown(self):
        self.cstn_dropdown_open = not self.cstn_dropdown_open
        self.cfsh_dropdown_open = ""
        self.engine_dropdown_open = ""
        self.stack_dropdown_open = False
        self.group_dropdown_open = False
    
    def toggle_cfsh_dropdown(self, cfsh: str):
        if self.cfsh_dropdown_open == cfsh:
            self.cfsh_dropdown_open = ""
        else:
            self.cfsh_dropdown_open = cfsh
            self.cstn_dropdown_open = False
            self.engine_dropdown_open = ""
            self.stack_dropdown_open = False
            self.group_dropdown_open = False
    
    def toggle_engine_dropdown(self, engine: str):
        if self.engine_dropdown_open == engine:
            self.engine_dropdown_open = ""
        else:
            self.engine_dropdown_open = engine
            self.cstn_dropdown_open = False
            self.cfsh_dropdown_open = ""
            self.stack_dropdown_open = False
            self.group_dropdown_open = False
    
    # Toggle state for third column
    toggle_state: bool = True  # True for first tab, False for second tab
    
    @rx.var
    def current_cfsh_names(self) -> List[str]:
        """Get CFSH names for current customer."""
        print(f"Getting CFSH names for customer: {self.selected_cstn}")  # Debug print
        print(f"Available customers: {list(CSTN_TO_CFSH.keys())}")  # Debug print
        cfsh_list = CSTN_TO_CFSH.get(self.selected_cstn, [])
        print(f"Found CFSH list: {cfsh_list}")  # Debug print
        return cfsh_list
    
    @rx.var
    def filtered_groups(self) -> List[str]:
        groups = list(GROUP_TO_STACKS.keys())
        if self.search_term:
            groups = [g for g in groups if self.search_term.lower() in g.lower()]
        return groups
    
    @rx.var
    def current_stacks(self) -> List[str]:
        return GROUP_TO_STACKS.get(self.selected_group, [])
    
    def set_cstn_name(self, value: str):
        self.selected_cstn = value
        # Clear selections when customer changes
        self.selected_engine = ""
        self.selected_cfsh = ""
        self.update_sidebar_visibility()
    
    def set_engine(self, engine: str):
        """Set the selected engine."""
        self.selected_engine = engine
        self.update_sidebar_visibility()
    
    def set_cfsh(self, cfsh: str):
        """Set the selected CFSH."""
        if self.selected_cfsh == cfsh:
            # If clicking the same CFSH, toggle it off
            self.selected_cfsh = ""
            self.selected_engine = ""  # Clear engine selection too
        else:
            # Select the new CFSH
            self.selected_cfsh = cfsh
            # Don't auto-select engine, let user click hearts
        self.update_sidebar_visibility()
    
    def set_search_term(self, value: str):
        self.search_term = value
    
    def set_selected_group(self, value: str):
        if value:  # Only update if a value is provided
            self.selected_group = value
            self.selected_stack = ""  # Reset stack selection
            self.update_sidebar_visibility()
    
    def set_selected_stack(self, value: str):
        if value:  # Only update if a value is provided
            self.selected_stack = value
            self.update_sidebar_visibility()
    
    def update_sidebar_visibility(self):
        self.sidebar_visible = bool(self.selected_engine or self.selected_stack)
    
    def toggle_tab_state(self):
        self.toggle_state = not self.toggle_state

def top_row() -> rx.Component:
    """Top row with customer selection dropdown."""
    return rx.hstack(
        rx.heading("CSTN: ", size="4", color="white"),
        rx.select(
            list(CSTN_TO_CFSH.keys()),
            value=State.selected_cstn,
            on_change=State.set_cstn_name,
            width="200px",
            bg="gray.800",
            color="white",
            border="1px solid #4a5568",
        ),
        # Debug text to show current customer
        rx.text(f"Current customer: {State.selected_cstn}", color="gray.400", margin_left="4"),
        spacing="4",
        padding="4",
        border_bottom="1px solid #4a5568",
        width="100%",
        bg="gray.900",
    )

def cfsh_row(cfsh: str) -> rx.Component:
    """Create a row for a CFSH with its engine hearts."""
    # Get engines using rx.cond
    engines = rx.cond(
        cfsh == "cfsh1",
        ["engine1", "engine2"],
        rx.cond(
            cfsh == "cfsh2",
            ["engine3", "engine4", "engine5"],
            rx.cond(
                cfsh == "cfsh3",
                ["engine6"],
                rx.cond(
                    cfsh == "cfsh6",
                    ["engine10", "engine11"],
                    rx.cond(
                        cfsh == "cfsh7",
                        ["engine12"],
                        rx.cond(
                            cfsh == "cfsh8",
                            ["engine13", "engine14", "engine15"],
                            rx.cond(
                                cfsh == "cfsh9",
                                ["engine16"],
                                []
                            )
                        )
                    )
                )
            )
        )
    )
    
    return rx.hstack(
        # Radio button for CFSH selection
        rx.button(
            rx.cond(
                State.selected_cfsh == cfsh,
                "●",  # Filled circle when selected
                "○"   # Empty circle when not selected
            ),
            on_click=lambda: State.set_cfsh(cfsh),
            variant="ghost",
            padding="2",
            color=rx.cond(State.selected_cfsh == cfsh, "blue.400", "white"),
            font_size="20px",
            _hover={"bg": "gray.700"},
            min_width="30px",
        ),
        
        # CFSH name
        rx.text(cfsh, color="white", margin_left="2"),
        
        # Debug text to show number of engines using .length()
        rx.text(
            rx.cond(
                engines.length() == 1,
                "(1 engine)",
                f"({engines.length()} engines)"
            ),
            color="gray.400",
            margin_left="4"
        ),
        
        # Hearts for engines using rx.foreach
        rx.hstack(
            rx.foreach(
                engines,
                lambda engine: rx.tooltip(
                    rx.button(
                        rx.cond(
                            State.selected_engine == engine,
                            "❤",  # Filled heart when selected
                            "♡"   # Empty heart when not selected
                        ),
                        on_click=lambda e=engine: State.set_engine(e),
                        variant="ghost",
                        padding="2",
                        color=rx.cond(State.selected_engine == engine, "red.400", "white"),
                        font_size="24px",
                        _hover={"bg": "gray.700"},
                        min_width="40px",
                    ),
                    label=engine,  # Just show the engine name for now
                    placement="top",
                    has_arrow=True,
                    arrow_size=8,
                    bg="gray.800",
                    color="white",
                )
            ),
            spacing="4",
        ),
        
        width="100%",
        padding="4",
        border_bottom="1px solid #4a5568",
        align="center",
        spacing="4",
    )

def cfsh_section() -> rx.Component:
    """Section showing CFSH instances with their engines."""
    # Debug print for current CFSH names
    print(f"Current CFSH names: {State.current_cfsh_names}")
    
    return rx.vstack(
        rx.heading("CFSH Instances", size="4", padding="2", color="white"),
        rx.vstack(
            rx.foreach(State.current_cfsh_names, cfsh_row),
            width="100%",
            spacing="2",
        ),
        width="100%",
        padding="4",
        bg="gray.900",
    )

def first_column() -> rx.Component:
    """First column with group search and selection."""
    return rx.vstack(
        rx.heading("Groups", size="4", padding="2", color="white"),
        rx.input(
            placeholder="Search groups...",
            value=State.search_term,
            on_change=State.set_search_term,
            width="100%",
            margin_bottom="4",
            border="1px solid #4a5568",
            border_radius="md",
            padding="2",
            bg="gray.800",
            color="white",
            _placeholder={"color": "gray.400"},
        ),
        rx.radio_group(
            items=State.filtered_groups,
            value=State.selected_group,
            on_change=State.set_selected_group,
            width="100%",
        ),
        align="start",
        padding="4",
        height="100%",
        bg="gray.900",
        border_radius="lg",
        border="1px solid #4a5568",
        box_shadow="sm",
        width="30%",
    )

def second_column() -> rx.Component:
    """Second column showing stacks for the selected group."""
    return rx.vstack(
        rx.heading("Stacks", size="4", padding="2", color="white"),
        rx.cond(
            State.selected_group,
            rx.vstack(
                rx.text(f"Selected Group: {State.selected_group}", color="gray.300", margin_bottom="2"),
                rx.select(
                    rx.Var.create(GROUP_TO_STACKS)[State.selected_group],
                    value=State.selected_stack,
                    on_change=State.set_selected_stack,
                    placeholder="Select a stack",
                    width="100%",
                    border="1px solid #4a5568",
                    border_radius="md",
                    padding="2",
                    bg="gray.800",
                    color="white",
                    _placeholder={"color": "gray.400"},
                ),
                width="100%",
            ),
            rx.vstack(
                rx.text("Select a group first", color="gray.400", margin_bottom="2"),
                rx.select(
                    [],
                    is_disabled=True,
                    placeholder="No group selected",
                    width="100%",
                    border="1px solid #4a5568",
                    border_radius="md",
                    padding="2",
                    bg="gray.800",
                    color="white",
                    _placeholder={"color": "gray.400"},
                ),
                width="100%",
            )
        ),
        align="start",
        width="25%",
        padding="4",
        bg="gray.900",
        border_radius="lg",
        border="1px solid #4a5568",
        box_shadow="sm",
    )

def format_var_list(var_list, default="None"):
    """Helper function to safely format a Reflex Var list."""
    return rx.cond(
        var_list != "",  # Changed from var_list.length() > 0
        rx.text(var_list),  # Changed from "Multiple items selected"
        rx.text(default)
    )

def third_column() -> rx.Component:
    """Third column with tabs for details."""
    return rx.vstack(
        rx.hstack(
            rx.heading("Details", size="4", color="white"),
            rx.spacer(),
            rx.switch(
                is_checked=State.toggle_state,
                on_change=State.toggle_tab_state,
                color_scheme="blue",
            ),
            width="100%",
            padding="2",
        ),
        rx.cond(
            State.toggle_state,
            # First tab content
            rx.vstack(
                rx.heading("Selection Summary", size="3", padding="2", color="white"),
                rx.text(f"Selected Customer: {State.selected_cstn}", color="gray.300"),
                rx.hstack(
                    rx.text("Selected CFSH: ", color="gray.300"),
                    rx.cond(
                        State.selected_cfsh != "",
                        rx.text(State.selected_cfsh, color="gray.300"),
                        rx.text("None", color="gray.300")
                    )
                ),
                rx.hstack(
                    rx.text("Selected Engine: ", color="gray.300"),
                    rx.cond(
                        State.selected_engine != "",
                        rx.text(State.selected_engine, color="gray.300"),
                        rx.text("None", color="gray.300")
                    )
                ),
                rx.hstack(
                    rx.text("Selected Group: ", color="gray.300"),
                    rx.cond(
                        State.selected_group != "",
                        rx.text(State.selected_group, color="gray.300"),
                        rx.text("None", color="gray.300")
                    )
                ),
                rx.hstack(
                    rx.text("Selected Stack: ", color="gray.300"),
                    rx.cond(
                        State.selected_stack != "",
                        rx.text(State.selected_stack, color="gray.300"),
                        rx.text("None", color="gray.300")
                    )
                ),
                align="start",
                width="100%",
                padding="4",
                bg="gray.800",
                border_radius="md",
                border="1px solid #4a5568",
            ),
            # Second tab content
            rx.vstack(
                rx.heading("Additional Info", size="3", padding="2", color="white"),
                rx.text("Additional information will be displayed here.", color="gray.300"),
                align="start",
                width="100%",
                padding="4",
                bg="gray.800",
                border_radius="md",
                border="1px solid #4a5568",
            ),
        ),
        align="start",
        width="45%",
        padding="4",
        bg="gray.900",
        border_radius="lg",
        border="1px solid #4a5568",
        box_shadow="sm",
    )

def sidebar() -> rx.Component:
    """Sidebar showing details of selected items."""
    return rx.box(
        rx.vstack(
            # Sidebar header
            rx.heading("Details", size="4", padding="4", color="white"),
            rx.divider(border_color="gray.700"),
            
            # Scrollable content
            rx.scroll_area(
                rx.vstack(
                    # Customer info
                    rx.box(
                        rx.button(
                            rx.hstack(
                                rx.text(f"Customer: {State.selected_cstn}", color="white"),
                                rx.icon(tag="chevron-down"),
                                justify="between",
                                width="100%",
                            ),
                            on_click=State.toggle_cstn_dropdown,
                            width="100%",
                            variant="ghost",
                            _hover={"bg": "gray.700"},
                        ),
                        rx.cond(
                            State.cstn_dropdown_open,
                            rx.box(
                                rx.vstack(
                                    *[rx.text(info, color="gray.300") for info in CSTN_INFO.get(State.selected_cstn, [])],
                                    align="start",
                                    padding="2",
                                    spacing="1",
                                    background="gray.800",
                                    rounded="md",
                                    margin_left="4",
                                    margin_bottom="2",
                                    border="1px solid #4a5568",
                                ),
                                width="100%",
                            ),
                        ),
                        width="100%",
                        padding_x="4",
                        padding_y="2",
                    ),
                    
                    # CFSH info if any selected
                    rx.cond(
                        State.selected_cfsh != "",
                        rx.box(
                            rx.vstack(
                                rx.heading("Selected CFSH", size="3", margin_top="4", padding_x="4", color="white"),
                                rx.button(
                                    rx.hstack(
                                        rx.text(State.selected_cfsh, color="white"),
                                        rx.icon(tag="chevron-down"),
                                        justify="between",
                                        width="100%",
                                    ),
                                    on_click=lambda cfsh=State.selected_cfsh: State.toggle_cfsh_dropdown(cfsh),
                                    width="100%",
                                    variant="ghost",
                                    padding_x="4",
                                    _hover={"bg": "gray.700"},
                                ),
                                rx.cond(
                                    State.cfsh_dropdown_open == State.selected_cfsh,
                                    rx.box(
                                        rx.vstack(
                                            *[rx.text(info, color="gray.300") for info in CFSH_INFO.get(State.selected_cfsh, [])],
                                            align="start",
                                            padding="2",
                                            spacing="1",
                                            background="gray.800",
                                            rounded="md",
                                            margin_left="4",
                                            margin_bottom="2",
                                            border="1px solid #4a5568",
                                        ),
                                        width="100%",
                                    ),
                                ),
                                width="100%",
                            ),
                            width="100%",
                        ),
                    ),
                    
                    # Engine info if any selected
                    rx.cond(
                        State.selected_engine != "",
                        rx.box(
                            rx.vstack(
                                rx.heading("Selected Engine", size="3", margin_top="4", padding_x="4", color="white"),
                                rx.button(
                                    rx.hstack(
                                        rx.text(State.selected_engine, color="white"),
                                        rx.icon(tag="chevron-down"),
                                        justify="between",
                                        width="100%",
                                    ),
                                    on_click=lambda engine=State.selected_engine: State.toggle_engine_dropdown(engine),
                                    width="100%",
                                    variant="ghost",
                                    padding_x="4",
                                    _hover={"bg": "gray.700"},
                                ),
                                rx.cond(
                                    State.engine_dropdown_open == State.selected_engine,
                                    rx.box(
                                        rx.vstack(
                                            *[rx.text(info, color="gray.300") for info in ENGINE_INFO.get(State.selected_engine, [])],
                                            align="start",
                                            padding="2",
                                            spacing="1",
                                            background="gray.800",
                                            rounded="md",
                                            margin_left="4",
                                            margin_bottom="2",
                                            border="1px solid #4a5568",
                                        ),
                                        width="100%",
                                    ),
                                ),
                                width="100%",
                            ),
                            width="100%",
                        ),
                    ),
                    
                    # Group info if selected
                    rx.cond(
                        State.selected_group != "",
                        rx.box(
                            rx.vstack(
                                rx.heading("Selected Group", size="3", margin_top="4", padding_x="4", color="white"),
                                rx.button(
                                    rx.hstack(
                                        rx.text(State.selected_group, color="white"),
                                        rx.icon(tag="chevron-down"),
                                        justify="between",
                                        width="100%",
                                    ),
                                    on_click=State.toggle_group_dropdown,
                                    width="100%",
                                    variant="ghost",
                                    padding_x="4",
                                    _hover={"bg": "gray.700"},
                                ),
                                rx.cond(
                                    State.group_dropdown_open,
                                    rx.box(
                                        rx.vstack(
                                            *[rx.text(f"Stack: {stack}", color="gray.300") for stack in GROUP_TO_STACKS.get(State.selected_group, [])],
                                            align="start",
                                            padding="2",
                                            spacing="1",
                                            background="gray.800",
                                            rounded="md",
                                            margin_left="4",
                                            margin_bottom="2",
                                            border="1px solid #4a5568",
                                        ),
                                        width="100%",
                                    ),
                                ),
                                width="100%",
                            ),
                            width="100%",
                        ),
                    ),
                    
                    # Stack info if selected
                    rx.cond(
                        State.selected_stack != "",
                        rx.box(
                            rx.vstack(
                                rx.heading("Selected Stack", size="3", margin_top="4", padding_x="4", color="white"),
                                rx.button(
                                    rx.hstack(
                                        rx.text(State.selected_stack, color="white"),
                                        rx.icon(tag="chevron-down"),
                                        justify="between",
                                        width="100%",
                                    ),
                                    on_click=State.toggle_stack_dropdown,
                                    width="100%",
                                    variant="ghost",
                                    padding_x="4",
                                    _hover={"bg": "gray.700"},
                                ),
                                rx.cond(
                                    State.stack_dropdown_open,
                                    rx.box(
                                        rx.vstack(
                                            *[rx.text(info, color="gray.300") for info in STACK_INFO.get(State.selected_stack, [])],
                                            align="start",
                                            padding="2",
                                            spacing="1",
                                            background="gray.800",
                                            rounded="md",
                                            margin_left="4",
                                            margin_bottom="2",
                                            border="1px solid #4a5568",
                                        ),
                                        width="100%",
                                    ),
                                ),
                                width="100%",
                            ),
                            width="100%",
                        ),
                    ),
                    
                    # Spacer to push content up when there are few items
                    rx.spacer(),
                    
                    width="100%",
                    spacing="4",
                    padding_bottom="4",
                ),
                height="calc(100vh - 120px)",
                width="100%",
                type="always",
                scrollbar_width="8px",
            ),
            
            # Close button at the bottom
            rx.button(
                "Close",
                on_click=State.toggle_sidebar,
                width="100%",
                border_radius="0",
                color_scheme="blue",
                _hover={"bg": "blue.600"},
            ),
        ),
        height="100%",
        spacing="0",
        display=rx.cond(State.sidebar_visible, "flex", "none"),
        position="fixed",
        right="-1px",  # Push to absolute right edge
        top="0",
        width="400px",
        bg="gray.900",
        border_left="1px solid #4a5568",
        box_shadow="lg",
        z_index="1000",
        overflow="hidden",
    )

def main_content() -> rx.Component:
    """Main content area with all sections."""
    return rx.box(
        rx.vstack(
            # Top row with customer selection
            top_row(),
            
            # CFSH section
            cfsh_section(),
            
            # Three columns section
            rx.hstack(
                first_column(),
                second_column(),
                third_column(),
                height="calc(100vh - 250px)",
                width="100%",  # Keep original width
                spacing="4",
                padding="4",
                align="start",
            ),
            
            width="100%",
            height="100vh",
            overflow="hidden",
            bg="gray.950",
        ),
        sidebar(),
        width="100%",
        height="100vh",
        position="relative",
    )

# Create the app
app = rx.App()

# Add the index page
app.add_page(component=main_content, route="/")

if __name__ == "__main__":
    app.run()
