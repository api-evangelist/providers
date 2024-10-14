FROM alpine:latest

LABEL "com.github.actions.name"="Create Zip File"
LABEL "com.github.actions.description"="Create a zip file containing specific files from your repository"
LABEL "com.github.actions.icon"="folder-plus"
LABEL "com.github.actions.color"="gray-dark"

LABEL "repository"="https://github.com/kinlane/add-item"
LABEL "homepage"="https://github.com/kinlane/add-item"
LABEL "maintainer"="Kin Lane <kinlane@gmail.com>"

RUN apk add zip
