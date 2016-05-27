#!/bin/bash

#
# This script builds the project.
#

PRJ_ROOT_PATH=$(readlink -f ..)
echo "Project path: $PRJ_ROOT_PATH"

# Build project
echo "Building plugin project..."
cd "$PRJ_ROOT_PATH"
mvn clean install -DskipTests
echo "Plugin project built successfully."
