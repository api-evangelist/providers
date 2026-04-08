---
aid: ansible
url: https://raw.githubusercontent.com/api-evangelist/ansible/refs/heads/main/apis.yml
apis:
- name: Ansible Automation Platform API
  description: RESTful API for Ansible Automation Platform (formerly Ansible Tower) that enables programmatic access to job templates, inventories, credentials, and automation workflows.
  image: https://www.ansible.com/hubfs/Images/Red-Hat-Ansible_OG.png
  humanURL: https://docs.ansible.com/automation-controller/latest/html/controllerapi/
  baseURL: https://your-controller-host/api/v2/
  tags:
  - Automation
  - Inventories
  - Jobs
  - Workflows
  properties:
  - type: Documentation
    url: https://docs.ansible.com/automation-controller/latest/html/controllerapi/
  - type: OpenAPI
    url: https://your-controller-host/api/v2/swagger/
  - type: Authentication
    url: https://docs.ansible.com/automation-controller/latest/html/controllerapi/authentication.html
  contact:
  - FN: Ansible Support
    email: ansible-support@redhat.com
    url: https://access.redhat.com/support
- name: AWX API
  description: RESTful API for AWX (the open-source upstream project for Ansible Automation Platform) providing access to job management, inventory, and automation resources.
  image: https://www.ansible.com/hubfs/Images/Red-Hat-Ansible_OG.png
  humanURL: https://github.com/ansible/awx
  baseURL: https://your-awx-host/api/v2/
  tags:
  - Automation
  - Jobs
  - Open Source
  - REST API
  properties:
  - type: Documentation
    url: https://docs.ansible.com/ansible-tower/latest/html/towerapi/
  - type: GitHub Repository
    url: https://github.com/ansible/awx
  - type: API Explorer
    url: https://your-awx-host/api/v2/
- name: Ansible Galaxy API
  description: API for Ansible Galaxy, a hub for finding, sharing, and downloading Ansible roles and collections.
  image: https://www.ansible.com/hubfs/Images/Red-Hat-Ansible_OG.png
  humanURL: https://galaxy.ansible.com/
  baseURL: https://galaxy.ansible.com/api/
  tags:
  - Collections
  - Community
  - Content
  - Roles
  properties:
  - type: Documentation
    url: https://galaxy.ansible.com/docs/
  - type: API Documentation
    url: https://galaxy.ansible.com/api/v3/
  - type: GitHub Repository
    url: https://github.com/ansible/galaxy
name: Ansible
tags:
- Automation
- Configuration Management
- DevOps
- Infrastructure as Code
- Orchestration
type: Contract
image: https://www.ansible.com/hubfs/Images/Red-Hat-Ansible_OG.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Ansible is an open-source automation platform that provides simple IT automation for cloud provisioning, configuration management, application deployment, and orchestration.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

