import os

import streamlit as st
import streamlit.components.v1 as components

parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "frontend/build")

_selectable_data_table = components.declare_component(
    "react_table", url=build_dir,
)


def selectable_data_table(data, key=None):
    return _selectable_data_table(data=data, default=[], key=key)



