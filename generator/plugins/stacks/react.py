from generator.plugins.base import StackPlugin

TYPES = {
    "1": {
        "key":         "component",
        "label":       "Component",
        "description": "Reusable UI piece — ginagamit sa maraming lugar",
        "examples":    "Navbar, Button, Card, Avatar",
    },
    "2": {
        "key":         "page",
        "label":       "Page",
        "description": "Isang buong screen o view ng app mo",
        "examples":    "Dashboard, Login, Profile, Settings",
    },
    "3": {
        "key":         "form",
        "label":       "Form",
        "description": "May mga input fields at submit button",
        "examples":    "LoginForm, SignupForm, CheckoutForm",
    },
    "4": {
        "key":         "layout",
        "label":       "Layout",
        "description": "Wrapper ng pages mo — header, footer, sidebar",
        "examples":    "MainLayout, AuthLayout, AdminLayout",
    },
    "5": {
        "key":         "modal",
        "label":       "Modal",
        "description": "Popup dialog — para sa confirm, alert, ganyan",
        "examples":    "ConfirmModal, AlertModal, DeleteModal",
    },
    "6": {
        "key":         "hook",
        "label":       "Hook",
        "description": "Custom React logic na pwede mong i-reuse",
        "examples":    "useAuth, useFetch, useModal",
    },
}


class ReactPlugin(StackPlugin):
    name = "react"
    label = "React + TypeScript + Tailwind"
    stack = "frontend"
    templates = "frontend"
    types = TYPES
