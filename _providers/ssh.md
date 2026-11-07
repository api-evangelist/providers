---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Ssh Agentic Access
  operation_count: 13
  slug: ssh-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 1
apis:
- description: 'Teleport is a modern SSH infrastructure access platform providing certificate-based authentication, session recording, audit logging, and role-based access control for SSH, Kubernetes, databases, and '
  name: Teleport Access Management API
  slug: teleport-api
- baseURL: https://api.openssh.example.com/v1
  baseurl_source: declared
  description: Authorized keys management for users
  name: SSH Authorized Keys API
  slug: ssh-authorized-keys-api
- baseURL: https://api.openssh.example.com/v1
  baseurl_source: declared
  description: SSH certificate authority and certificate signing
  name: SSH Certificates API
  slug: ssh-certificates-api
- baseURL: https://api.openssh.example.com/v1
  baseurl_source: declared
  description: SSH server host key management
  name: SSH Host Keys API
  slug: ssh-host-keys-api
- baseURL: https://api.openssh.example.com/v1
  baseurl_source: declared
  description: SSH key pair management
  name: SSH Keys API
  slug: ssh-keys-api
- baseURL: https://api.openssh.example.com/v1
  baseurl_source: declared
  description: Known hosts verification and management
  name: SSH Known Hosts API
  slug: ssh-known-hosts-api
artifact_total: 25
collections:
- collection_type: open
  name: SSH Key Management Authorized Keys API
  slug: open-ssh-authorized-keys-api
- collection_type: open
  name: SSH Key Management Authorized Keys Certificates API
  slug: open-ssh-certificates-api
- collection_type: open
  name: SSH Key Management Authorized Keys Host Keys API
  slug: open-ssh-host-keys-api
- collection_type: open
  name: SSH Key Management API
  slug: open-ssh-key-management
- collection_type: open
  name: SSH Key Management Authorized Keys API
  slug: open-ssh-keys-api
- collection_type: open
  name: SSH Key Management Authorized Keys Known Hosts API
  slug: open-ssh-known-hosts-api
common:
- group: commercial
  href: https://artifacts.apis.io/ssh/plans/ssh-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ssh-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ssh/rate-limits/ssh-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ssh-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ssh/finops/ssh-finops.yml
  title: ''
  type: FinOps
  url: finops/ssh-finops.yml
- group: other
  href: https://artifacts.apis.io/ssh/capabilities/ssh-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ssh-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/ssh/agentic-access/ssh-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ssh-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/ssh/security/ssh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ssh-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/ssh/authentication/ssh-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ssh-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.openssh.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.openssh.com/manual.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openssh
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/ssh/refs/heads/main/openapi/ssh-key-management-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/ssh/refs/heads/main/json-schema/ssh-key-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/ssh/refs/heads/main/json-structure/ssh-key-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/ssh/refs/heads/main/json-ld/ssh-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/ssh/refs/heads/main/rules/ssh-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/ssh/refs/heads/main/vocabulary/ssh-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://ssh.com/blog/rss.xml
created: '2025-01-01'
description: SSH (Secure Shell) is a cryptographic network protocol for secure remote login, command execution, and file transfer between computers over unsecured networks. It provides strong encryption, authentication, and data integrity, replacing insecure protocols like Telnet and rlogin. SSH is a fundamental tool for system administration, DevOps, and secure infrastructure access. Multiple vendors provide SSH client libraries, server implementations, and management APIs.
examples:
- key_count: 4
  name: Ssh List Keys Example
  slug: ssh-list-keys-example
- key_count: 4
  name: Ssh Sign Certificate Example
  slug: ssh-sign-certificate-example
finops:
- has_sources: false
  method: generated
  name: Ssh Finops
  primary_unit: request
  service_category: API
  slug: ssh-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ssh.png
json_schemas:
- name: SSH Key
  property_count: 8
  slug: ssh-key
json_structures:
- name: Ssh Key Structure
  property_count: 0
  slug: ssh-key-structure
jsonld:
- class_count: 15
  name: Ssh Context
  property_count: 6
  slug: ssh-context
layout: provider
modified: '2026-05-19'
name: SSH
nav: Providers
network: true
overview: 'SSH publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authorized Keys API, Certificates API, Host Keys API, and 3 more. Tagged areas include SSH, Secure Shell, Remote Access, Cryptography, and Network Security.


  The SSH catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SSH''s developer surface includes authentication, documentation, engineering blog, and 14 more developer resources.'
plans:
- name: Ssh Plans Pricing
  plan_count: 3
  slug: ssh-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Ssh Rate Limits
  slug: ssh-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: SSH — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ssh-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: SSH API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: ssh-rules
screenshot: https://apis.io/screenshots/ssh/ssh-2026-06-20T194434.png
security:
- kind: authentication
  name: Ssh Authentication
  slug: ssh-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ssh Domain Security
  slug: ssh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ssh
tags:
- SSH
- Secure Shell
- Remote Access
- Cryptography
- Network Security
- System Administration
website: https://www.openssh.com/
---
