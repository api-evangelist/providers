---
aid: ansible-playbooks
url: https://raw.githubusercontent.com/api-evangelist/ansible-playbooks/refs/heads/main/apis.yml
apis:
- name: Ansible Automation Platform API
  description: REST API for Ansible Automation Platform (formerly Tower/AWX) to manage playbooks, inventories, and job execution.
  image: https://www.ansible.com/hubfs/2016_Images/Assets/Ansible-Mark-Large-RGB-Pool.png
  humanURL: https://www.ansible.com/products/automation-platform
  baseURL: https://your-tower-instance/api/v2/
  tags:
  - Automation
  - Jobs
  - Orchestration
  - Playbooks
  properties:
  - type: Documentation
    url: https://docs.ansible.com/automation-controller/latest/html/controllerapi/
  - type: OpenAPI
    url: https://your-tower-instance/api/v2/swagger/
  - type: Authentication
    url: https://docs.ansible.com/automation-controller/latest/html/controllerapi/authentication.html
  - type: Pricing
    url: https://www.ansible.com/products/pricing
  contact:
  - type: Support
    url: https://access.redhat.com/support
  - type: Email
    url: ansible-support@redhat.com
- name: AWX API
  description: Open source upstream API for Ansible Tower, providing programmatic access to playbook execution and management.
  image: https://raw.githubusercontent.com/ansible/awx-logos/master/awx/ui/client/assets/logo-header.svg
  humanURL: https://github.com/ansible/awx
  baseURL: https://your-awx-instance/api/v2/
  tags:
  - Automation
  - AWX
  - Open Source
  - Playbooks
  properties:
  - type: Documentation
    url: https://github.com/ansible/awx/blob/devel/docs/rest_api.md
  - type: GitHub Repository
    url: https://github.com/ansible/awx
  - type: API Explorer
    url: https://your-awx-instance/api/v2/
  - type: Installation Guide
    url: https://github.com/ansible/awx/blob/devel/INSTALL.md
- name: Ansible Runner API
  description: Python interface and API for directly executing Ansible playbooks programmatically.
  humanURL: https://ansible-runner.readthedocs.io/
  baseURL: https://pypi.org/project/ansible-runner/
  tags:
  - Execution
  - Library
  - Playbooks
  - Python
  properties:
  - type: Documentation
    url: https://ansible-runner.readthedocs.io/en/stable/
  - type: GitHub Repository
    url: https://github.com/ansible/ansible-runner
  - type: Python Package
    url: https://pypi.org/project/ansible-runner/
  - type: Examples
    url: https://ansible-runner.readthedocs.io/en/stable/intro.html#examples
- name: Ansible Galaxy API
  description: API for discovering, sharing, and downloading Ansible roles and collections.
  humanURL: https://galaxy.ansible.com
  baseURL: https://galaxy.ansible.com/api/
  tags:
  - Collections
  - Community
  - Roles
  - Sharing
  properties:
  - type: Documentation
    url: https://galaxy.ansible.com/docs/
  - type: API Documentation
    url: https://galaxy.ansible.com/api/v3/
  - type: Collections
    url: https://galaxy.ansible.com/api/v3/collections/
  - type: Roles
    url: https://galaxy.ansible.com/api/v1/roles/
- name: Ansible Automation Hub API
  description: Enterprise API for certified Ansible content including collections, roles, and execution environments.
  humanURL: https://console.redhat.com/ansible/automation-hub
  baseURL: https://console.redhat.com/api/automation-hub/
  tags:
  - Certified Content
  - Collections
  - Enterprise
  - Red Hat
  properties:
  - type: Documentation
    url: https://access.redhat.com/documentation/en-us/red_hat_ansible_automation_platform/
  - type: API Guide
    url: https://console.redhat.com/ansible/automation-hub/api/
  - type: Certification
    url: https://www.ansible.com/products/content-tools
- name: Ansible Semaphore API
  description: Modern UI and API for running Ansible playbooks with a focus on simplicity.
  humanURL: https://www.ansible-semaphore.com/
  baseURL: https://your-semaphore-instance/api/
  tags:
  - Open Source
  - Playbooks
  - UI
  - Workflow
  properties:
  - type: Documentation
    url: https://docs.ansible-semaphore.com/
  - type: GitHub Repository
    url: https://github.com/ansible-semaphore/semaphore
  - type: API Documentation
    url: https://docs.ansible-semaphore.com/api-reference
name: Ansible Playbooks
tags:
- Automation
- Configuration Management
- DevOps
- Infrastructure as Code
- Orchestration
type: Contract
image: https://www.ansible.com/hubfs/2016_Images/Assets/Ansible-Mark-Large-RGB-Pool.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs and resources for managing and executing Ansible playbooks for IT automation, configuration management, and orchestration.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

