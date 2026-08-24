---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.5
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 11
common:
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/json-schema/rbac-role.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/json-schema/rbac-permission.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/json-schema/rbac-assignment.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/json-structure/rbac-role-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/json-structure/rbac-permission-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/json-structure/rbac-assignment-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/json-ld/rbac-context.jsonld
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/examples/rbac-role-example.json
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/examples/rbac-permission-example.json
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/examples/rbac-assignment-example.json
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/vocabulary/rbac-vocabulary.yml
- group: other
  title: ''
  type: Standards
  url: https://csrc.nist.gov/projects/role-based-access-control
- group: docs
  title: ''
  type: Documentation
  url: https://kubernetes.io/docs/reference/access-authn-authz/rbac/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html
created: '2025-01-01'
description: 'Role-Based Access Control (RBAC) is a security paradigm that restricts system access based on assigned roles rather than individual user identities. Users are granted permissions through role membership, simplifying access management and ensuring the principle of least privilege. RBAC is foundational to enterprise identity, authorization, and compliance programs and is implemented across operating systems, cloud platforms, databases, and APIs. The NIST/ANSI/INCITS 359-2004 standard formally defines the RBAC model across four components: Core RBAC, Hierarchical RBAC, Static Separation of Duty, and Dynamic Separation of Duty. Cloud platforms (AWS IAM, Azure RBAC, GCP IAM) and Kubernetes all implement RBAC natively, making it the de facto authorization standard for enterprise and cloud-native environments.'
examples:
- key_count: 10
  name: Rbac Assignment Example
  slug: rbac-assignment-example
- key_count: 8
  name: Rbac Permission Example
  slug: rbac-permission-example
- key_count: 10
  name: Rbac Role Example
  slug: rbac-role-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rbac.png
json_schemas:
- name: RBAC Role Assignment
  property_count: 8
  slug: rbac-assignment
- name: RBAC Permission
  property_count: 6
  slug: rbac-permission
- name: RBAC Role
  property_count: 8
  slug: rbac-role
json_structures:
- name: Rbac Assignment Structure
  property_count: 0
  slug: rbac-assignment-structure
- name: Rbac Permission Structure
  property_count: 0
  slug: rbac-permission-structure
- name: Rbac Role Structure
  property_count: 0
  slug: rbac-role-structure
jsonld:
- class_count: 8
  name: Rbac Context
  property_count: 12
  slug: rbac-context
layout: provider
modified: '2026-05-02'
name: RBAC
nav: Providers
network: true
overview: 'RBAC is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Access Control, Authorization, Cloud-Native, Compliance, and Identity Management.


  The RBAC catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RBAC''s developer surface includes code examples, documentation, and 12 more developer resources.'
random_paper: 9
rules:
- effective_rule_count: 5
  extends: []
  name: RBAC API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rbac-jsonschema-spectral-rules
score:
  band: emerging
  composite: 14.1
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 25.0
    contract_quality: 16.9
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 25.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 14.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rbac/refs/heads/main/screenshots/rbac-2026-06-20T192625.png
slug: rbac
tags:
- Access Control
- Authorization
- Cloud-Native
- Compliance
- Identity Management
- Kubernetes
- RBAC
- Security
---
