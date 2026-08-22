---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Sigstore Agentic Access
  operation_count: 11
  slug: sigstore-agentic-access
  summary_line: 11 operations · 4 acting
api_count: 6
apis:
- description: Cosign is the Sigstore tool for signing and verifying container images and other OCI artifacts. It enables keyless signing using OIDC identity, hardware token signing, and policy enforcement for conta
  name: Cosign
  slug: cosign
- description: The CA API from Sigstore — 3 operation(s) for ca.
  name: Sigstore CA API
  slug: sigstore-ca-api
- description: The entries API from Sigstore — 3 operation(s) for entries.
  name: Sigstore entries API
  slug: sigstore-entries-api
- description: The index API from Sigstore — 1 operation(s) for index.
  name: Sigstore index API
  slug: sigstore-index-api
- description: The pubkey API from Sigstore — 1 operation(s) for pubkey.
  name: Sigstore pubkey API
  slug: sigstore-pubkey-api
- description: The tlog API from Sigstore — 2 operation(s) for tlog.
  name: Sigstore tlog API
  slug: sigstore-tlog-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fulcio
  slug: open-fulcio
- collection_type: open
  name: Fulcio CA API
  slug: open-sigstore-ca-api
- collection_type: open
  name: Fulcio CA entries API
  slug: open-sigstore-entries-api
- collection_type: open
  name: Fulcio CA index API
  slug: open-sigstore-index-api
- collection_type: open
  name: Fulcio CA pubkey API
  slug: open-sigstore-pubkey-api
- collection_type: open
  name: Fulcio CA tlog API
  slug: open-sigstore-tlog-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/sigstore/cosign/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sigstore-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sigstore-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sigstore
- group: company
  title: ''
  type: Website
  url: https://www.sigstore.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sigstore.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sigstore.dev/quickstart/quickstart-cosign/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sigstore
- group: company
  title: ''
  type: Blog
  url: https://blog.sigstore.dev/
- group: operate
  title: ''
  type: Community
  url: https://sigstore.dev/community/
- group: other
  title: ''
  type: Policy Controller
  url: https://docs.sigstore.dev/policy-controller/overview/
- group: auth
  title: ''
  type: Security
  url: https://docs.sigstore.dev/about/security/
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/sigstore/refs/heads/main/vocabulary/sigstore-vocabulary.yml
created: '2026-03-26'
description: Sigstore is a set of free-to-use open source tools for signing, verifying, and protecting software supply chain artifacts. It provides a transparent and auditable signing infrastructure that eliminates the need for managing signing keys, making software supply chain security more accessible. The Sigstore ecosystem includes Cosign for artifact signing, Fulcio as the certificate authority, and Rekor as the cryptographically secure transparency log.
examples:
- key_count: 3
  name: Sigstore Create Log Entry Example
  slug: sigstore-create-log-entry-example
- key_count: 3
  name: Sigstore Get Signing Cert Example
  slug: sigstore-get-signing-cert-example
- key_count: 3
  name: Sigstore Search Log Index Example
  slug: sigstore-search-log-index-example
finops:
- name: Sigstore Finops
  service_category: Software Supply Chain Security
  slug: sigstore-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sigstore.png
json_schemas:
- name: Sigstore Fulcio Signing Certificate
  property_count: 2
  slug: sigstore-certificate
- name: Sigstore Rekor Log Entry
  property_count: 6
  slug: sigstore-log-entry
json_structures:
- name: Sigstore Log Entry Structure
  property_count: 0
  slug: sigstore-log-entry-structure
jsonld:
- class_count: 30
  name: Sigstore Context
  property_count: 2
  slug: sigstore-context
layout: provider
modified: '2026-05-19'
name: Sigstore
nav: Providers
network: true
overview: 'Sigstore publishes 5 APIs on the [APIs.io](https://apis.io/) network, including CA API, entries API, index API, and 2 more. Tagged areas include Certificate Authority, Code Signing, Containers, Cryptography, and Open Source.


  The Sigstore catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sigstore''s developer surface includes documentation, getting-started guide, engineering blog, and 10 more developer resources.'
plans:
- name: Sigstore Plans Pricing
  plan_count: 1
  slug: sigstore-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Sigstore Rate Limits
  slug: sigstore-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Sigstore API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sigstore-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Sigstore API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: sigstore-rules
score:
  band: thin
  composite: 32.6
  delta: -6.2
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 25.0
    contract_quality: 51.2
    developer_ergonomics: 26.2
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 18.4
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/sigstore/refs/heads/main/screenshots/sigstore-2026-06-20T193917.png
security:
- kind: domain-security
  name: Sigstore Domain Security
  slug: sigstore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sigstore
tags:
- Certificate Authority
- Code Signing
- Containers
- Cryptography
- Open Source
- PKI
- Security
- Software Supply Chain
- Transparency Log
website: https://www.sigstore.dev/
---
