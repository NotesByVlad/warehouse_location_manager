# Warehouse Location Manager

A Python project for managing warehouse locations.

This project is being developed as one of the core components of a future **Warehouse Management System (WMS)**. Its purpose is to manage warehouse locations throughout their lifecycle, from generation to daily operations such as searching, blocking, occupying, and maintaining locations.

## Project Goals

The Location Manager will eventually be responsible for:

* Generating warehouse locations
* Loading and saving warehouse data
* Searching for locations
* Blocking and unblocking locations
* Occupying and freeing locations
* Providing warehouse statistics
* Serving as the location subsystem of a larger WMS

## Project Structure

The project currently contains a **Location Generator**, which was copied from the standalone **Warehouse Location Generator** repository.

The generator works and is capable of creating warehouse locations based on configurable warehouse rules. However, it was intentionally copied without major changes and will be **refactored** as the Location Manager evolves.

The long-term goal is to integrate the generator naturally into the manager rather than treating it as a separate application.

## Future Vision

This project is intended to become the location component of a complete Warehouse Management System, where other modules such as:

* Receiving
* Inventory
* Outbound
* Picking
* Cycle Counting

will eventually interact with the Location Manager.

The philosophy of this repository is to build small, functional components first, then combine them into a larger and well-structured WMS.

## Status

Current stage:

* ✅ Initial repository created
* ✅ Warehouse generator integrated
* 🔄 Generator refactoring planned
* 🚧 Location Manager development in progress

This repository is part of a long-term learning project focused on Python, software architecture, and Warehouse Management Systems.
