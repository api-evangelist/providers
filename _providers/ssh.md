---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Ssh Agentic Access
  operation_count: 13
  slug: ssh-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 6
apis:
- description: 'Teleport is a modern SSH infrastructure access platform providing certificate-based authentication, session recording, audit logging, and role-based access control for SSH, Kubernetes, databases, and '
  name: Teleport Access Management API
  slug: teleport-api
- description: Authorized keys management for users
  name: SSH Authorized Keys API
  slug: ssh-authorized-keys-api
- description: SSH certificate authority and certificate signing
  name: SSH Certificates API
  slug: ssh-certificates-api
- description: SSH server host key management
  name: SSH Host Keys API
  slug: ssh-host-keys-api
- description: SSH key pair management
  name: SSH Keys API
  slug: ssh-keys-api
- description: Known hosts verification and management
  name: SSH Known Hosts API
  slug: ssh-known-hosts-api
artifact_total: 20
collections:
- collection_type: open
  name: SSH Key Management API
  slug: open-ssh-key-management
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ssh-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ssh-domain-security.yml
- group: auth
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
- name: Ssh Finops
  service_category: API
  slug: ssh-finops
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
overview: 'SSH publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authorized Keys API, Certificates API, Host Keys API, and 2 more. Tagged areas include SSH, Secure Shell, Remote Access, Cryptography, and Network Security.


  The SSH catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SSH''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Ssh Plans Pricing
  plan_count: 3
  slug: ssh-plans-pricing
random_paper: 102
rate_limits:
- limit_count: 5
  name: Ssh Rate Limits
  slug: ssh-rate-limits
rules:
- name: SSH API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ssh-jsonschema-spectral-rules
- name: SSH API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: ssh-rules
score:
  band: thin
  composite: 40.5
  delta: -8.4
  facets:
    commercial_clarity: 15.8
    contract_quality: 62.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ssh/refs/heads/main/screenshots/ssh-2026-06-20T194434.png
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
