---
aid: ansible-roles
url: https://raw.githubusercontent.com/api-evangelist/ansible-roles/refs/heads/main/apis.yml
apis:
- name: Ansible Galaxy API
  description: Public API for searching, discovering, and downloading Ansible roles and collections.
  image: https://galaxy.ansible.com/static/galaxy-logo.png
  humanURL: https://galaxy.ansible.com
  baseURL: https://galaxy.ansible.com/api/v1
  version: v1
  properties:
  - type: documentation
    url: https://galaxy.ansible.com/docs/
  - type: openapi
    url: https://galaxy.ansible.com/api/v1/openapi.json
  - type: swagger
    url: https://galaxy.ansible.com/api/v1/swagger/
  contact:
  - type: email
    url: mailto:info@ansible.com
  - type: support
    url: https://github.com/ansible/galaxy/issues
  operations:
  - name: Search Roles
    description: Search for Ansible roles by keyword, tag, or author
    method: GET
    path: /roles/
    parameters:
    - name: search
      type: string
      description: Search term for role name or description
    - name: page
      type: integer
      description: Page number for pagination
    - name: page_size
      type: integer
      description: Number of results per page
  - name: Get Role Details
    description: Retrieve detailed information about a specific role
    method: GET
    path: /roles/{id}/
    parameters:
    - name: id
      type: integer
      description: Unique identifier for the role
      required: true
  - name: List Role Versions
    description: Get all available versions of a role
    method: GET
    path: /roles/{id}/versions/
  - name: Download Role
    description: Download a specific version of a role
    method: GET
    path: /roles/{id}/versions/{version}/download/
  - name: Search Collections
    description: Search for Ansible collections
    method: GET
    path: /collections/
  - name: Get Collection Details
    description: Retrieve information about a specific collection
    method: GET
    path: /collections/{namespace}/{name}/
- name: Ansible Galaxy API v3
  description: Next generation API for Ansible Galaxy with enhanced collection support.
  baseURL: https://galaxy.ansible.com/api/v3
  version: v3
  properties:
  - type: documentation
    url: https://galaxy.ansible.com/docs/api/
  operations:
  - name: List Collections
    description: List all available collections with filtering options
    method: GET
    path: /plugin/ansible/content/published/collections/index/
  - name: Get Collection Version
    description: Get specific version details of a collection
    method: GET
    path: /plugin/ansible/content/published/collections/index/{namespace}/{name}/versions/{version}/
name: Ansible Roles
tags:
- Ansible
- Automation
- Configuration-Management
- Devops
- Infrastructure-As-Code
type: Contract
image: https://ansible.com/images/ansible-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for managing and discovering Ansible Roles from Ansible Galaxy.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

