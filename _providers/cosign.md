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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-09-25'
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
artifact_total: 9
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/sigstore/cosign/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/sigstore/cosign/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/sigstore/cosign/blob/main/CONTRIBUTING.md
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cosign/refs/heads/main/security/cosign-domain-security.yml
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
  url: https://www.sigstore.dev/community
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
  url: https://github.com/sigstore/community/blob/main/ROADMAP.md
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sigstore.dev/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cosign/refs/heads/main/packages/cosign-packages.yml
  title: ''
  type: Packages
  url: packages/cosign-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cosign/refs/heads/main/packages/cosign-packages.yml
  title: ''
  type: SDKs
  url: packages/cosign-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cosign/refs/heads/main/cli/cosign-cli.yml
  title: ''
  type: CLI
  url: cli/cosign-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cosign/refs/heads/main/changelog/cosign-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cosign-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cosign/refs/heads/main/lifecycle/cosign-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cosign-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sigstore.dev/
- group: operate
  title: ''
  type: Deprecation
  url: https://github.com/sigstore/cosign/blob/main/VERSIONING.md
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cosign/refs/heads/main/security/cosign-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cosign-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cosign/refs/heads/main/conformance/cosign-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cosign-conformance.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/cosign/refs/heads/main/sandbox/cosign-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/cosign-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cosign/refs/heads/main/conventions/cosign-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cosign-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cosign/refs/heads/main/errors/cosign-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/cosign-error-codes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cosign/refs/heads/main/authentication/cosign-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cosign-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cosign/refs/heads/main/data-model/cosign-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cosign-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cosign/refs/heads/main/llms/cosign-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cosign-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cosign/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cosign/refs/heads/main/mcp/cosign-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cosign-mcp.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cosign/refs/heads/main/plans/cosign-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cosign-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cosign/refs/heads/main/rate-limits/cosign-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cosign-rate-limits.yml
created: '2026-03-26'
description: Cosign is the command-line client of the Sigstore project for signing, verifying, and storing container images, OCI artifacts, blobs, and in-toto attestations. Cosign supports keyless signing using OpenID Connect identity providers (Google, GitHub, Microsoft) by obtaining short-lived certificates from the Fulcio certificate authority and recording signing events in the Rekor transparency log. Signatures and attestations are stored alongside the signed artifact in any OCI-compliant registry, and cosign integrates with policy controllers, KMS providers, hardware tokens, and SBOM workflows for software supply chain security.
finops:
- name: Cosign Finops
  service_category: API
  slug: cosign-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cosign.png
layout: provider
modified: '2026-09-07'
name: Cosign
nav: Providers
network: true
overview: 'Cosign publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Sigstore Rekor API (consumed), Sigstore Fulcio API (consumed), and 1 more. Tagged areas include Apache 2.0, Attestation, CLI, Code Signing, and Containers.


  Cosign''s developer surface includes documentation, getting-started guide, release notes, engineering blog, CLI, changelog, sandbox, and 31 more developer resources.'
plans:
- name: Cosign Plans Pricing
  plan_count: 0
  slug: cosign-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Cosign Rate Limits
  slug: cosign-rate-limits
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.7
  facets:
    access_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 24.0
    developer_ergonomics: 78.0
    discoverability: 69.6
    operational_transparency: 50.0
  open_source:
    applies: true
    score: 65.0
  previous_composite: 39.8
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/cosign/refs/heads/main/screenshots/cosign-2026-06-20T175045.png
security:
- kind: authentication
  name: Cosign Authentication
  slug: cosign-authentication
  summary_line: 6 schemes
- kind: domain-security
  name: Cosign Domain Security
  slug: cosign-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cosign Vulnerability Disclosure
  slug: cosign-vulnerability-disclosure
  summary_line: Hackerone
slug: cosign
tags:
- Apache 2.0
- Attestation
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
