---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agentic_access: false
    auth_clarity: false
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
  score: 19.4
  scored_at: '2026-08-06'
api_count: 3
apis:
- description: Cosign is a command-line tool for signing, verifying, and storing container images and OCI artifacts. It supports keyless signing, hardware-backed keys, KMS providers, in-toto and SLSA attestations, a
  name: Cosign CLI
  slug: cosign-cli
- description: Rekor is the Sigstore transparency log that cosign writes to and reads from when recording and verifying signing events. The public Rekor service exposes a REST API at rekor.sigstore.dev with operatio
  name: Sigstore Rekor API (consumed)
  slug: rekor-api
- description: Fulcio is the Sigstore certificate authority that issues short-lived X.509 code-signing certificates bound to OIDC identities. Cosign calls the Fulcio public CA at fulcio.sigstore.dev during keyless s
  name: Sigstore Fulcio API (consumed)
  slug: fulcio-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cosign-domain-security.yml
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
  url: https://docs.sigstore.dev/cosign/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sigstore.dev/quickstart/quickstart-cosign/
- group: other
  title: ''
  type: Installation
  url: https://docs.sigstore.dev/cosign/system_config/installation/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sigstore
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/sigstore/cosign
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/sigstore/cosign/releases
- group: company
  title: ''
  type: Blog
  url: https://blog.sigstore.dev/
- group: operate
  title: ''
  type: Community
  url: https://docs.sigstore.dev/about/community/
- group: operate
  title: ''
  type: Slack
  url: https://sigstore.slack.com/
- group: commercial
  title: ''
  type: License
  url: https://github.com/sigstore/cosign/blob/main/LICENSE
- group: auth
  title: ''
  type: Security
  url: https://github.com/sigstore/cosign/security
- group: operate
  title: ''
  type: RoadMap
  url: https://github.com/sigstore/cosign/blob/main/ROADMAP.md
created: '2026-03-26'
description: Cosign is the command-line client of the Sigstore project for signing, verifying, and storing container images, OCI artifacts, blobs, and in-toto attestations. Cosign supports keyless signing using OpenID Connect identity providers (Google, GitHub, Microsoft) by obtaining short-lived certificates from the Fulcio certificate authority and recording signing events in the Rekor transparency log. Signatures and attestations are stored alongside the signed artifact in any OCI-compliant registry, and cosign integrates with policy controllers, KMS providers, hardware tokens, and SBOM workflows for software supply chain security.
finops:
- name: Cosign Finops
  service_category: API
  slug: cosign-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cosign.png
layout: provider
modified: '2026-04-28'
name: Cosign
nav: Providers
network: true
overview: 'Cosign publishes 1 API on the [APIs.io](https://apis.io/) network: Sigstore Rekor API (consumed). Tagged areas include Apache 2.0, Attestations, CLI, Code Signing, and Containers.


  Cosign''s developer surface includes documentation, getting-started guide, release notes, engineering blog, and 11 more developer resources.'
plans:
- name: Cosign Plans Pricing
  plan_count: 3
  slug: cosign-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 5
  name: Cosign Rate Limits
  slug: cosign-rate-limits
score:
  band: thin
  composite: 36.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 32.3
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 36.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cosign/refs/heads/main/screenshots/cosign-2026-06-20T175045.png
security:
- kind: domain-security
  name: Cosign Domain Security
  slug: cosign-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cosign
tags:
- Apache 2.0
- Attestations
- CLI
- Code Signing
- Containers
- Fulcio
- Go
- Keyless
- OCI
- OIDC
- Open Source
- Rekor
- Sigstore
- Supply Chain
- Transparency Log
- Verification
website: https://www.sigstore.dev/
---
