---
aid: ssh
name: SSH
description: SSH (Secure Shell) is a cryptographic network protocol for secure remote login, command execution, and file transfer between computers over unsecured networks. It provides strong encryption, authentication, and data integrity, replacing insecure protocols like Telnet and rlogin. SSH is a fundamental tool for system administration, DevOps, and secure infrastructure access. Multiple vendors provide SSH client libraries, server implementations, and management APIs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - SSH
  - Secure Shell
  - Remote Access
  - Cryptography
  - Network Security
  - System Administration
url: https://raw.githubusercontent.com/api-evangelist/ssh/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: ssh:openssh-management
    name: OpenSSH Key Management API
    description: OpenSSH is the premier open-source SSH implementation. While SSH itself is a protocol, OpenSSH provides programmatic interfaces for key management, authorized_keys configuration, known_hosts management, and integration with PAM and certificate authorities. SSH certificate authorities enable large-scale key management via short-lived certificates.
    humanURL: https://www.openssh.com/
    baseURL: https://api.openssh.example.com/v1
    tags:
      - SSH
      - OpenSSH
      - Key Management
      - Certificate Authority
      - Authentication
    properties:
      - type: Documentation
        url: https://www.openssh.com/manual.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/ssh/refs/heads/main/openapi/ssh-key-management-openapi.yml
  - aid: ssh:teleport-api
    name: Teleport Access Management API
    description: Teleport is a modern SSH infrastructure access platform providing certificate-based authentication, session recording, audit logging, and role-based access control for SSH, Kubernetes, databases, and web applications. Teleport's API enables programmatic management of users, roles, certificates, and access policies.
    humanURL: https://goteleport.com/
    baseURL: https://teleport.example.com/v1
    tags:
      - SSH
      - Access Management
      - Certificate Authority
      - Zero Trust
      - Privileged Access
    properties:
      - type: Documentation
        url: https://goteleport.com/docs/
common:
  - type: Website
    url: https://www.openssh.com/
  - type: Documentation
    url: https://www.openssh.com/manual.html
  - type: GitHub Organization
    url: https://github.com/openssh
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/ssh/refs/heads/main/openapi/ssh-key-management-openapi.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/ssh/refs/heads/main/json-schema/ssh-key-schema.json
  - type: JSONStructure
    url: https://raw.githubusercontent.com/api-evangelist/ssh/refs/heads/main/json-structure/ssh-key-structure.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/ssh/refs/heads/main/json-ld/ssh-context.jsonld
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/ssh/refs/heads/main/rules/ssh-rules.yml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/ssh/refs/heads/main/capabilities/key-management.yaml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/ssh/refs/heads/main/vocabulary/ssh-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
