---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: AWS CodeCommit API provides operations for repositories, commits, branches, and pull requests.
  name: CodeCommit API
  slug: codecommit-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-codecommit/refs/heads/main/llms/amazon-codecommit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amazon-codecommit-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-codecommit/refs/heads/main/well-known/amazon-codecommit-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amazon-codecommit-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-codecommit/refs/heads/main/well-known/amazon-codecommit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amazon-codecommit-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amazon-codecommit/refs/heads/main/hosts/amazon-codecommit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amazon-codecommit-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amazon-codecommit/refs/heads/main/vendors/amazon-codecommit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amazon-codecommit-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-codecommit/refs/heads/main/packages/amazon-codecommit-packages.yml
  title: ''
  type: SDKs
  url: packages/amazon-codecommit-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-codecommit/refs/heads/main/packages/amazon-codecommit-packages.yml
  title: ''
  type: Packages
  url: packages/amazon-codecommit-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.amazon.com/terms-and-agreements
- group: start
  title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=builderId
- group: auth
  title: ''
  type: Security
  url: https://aws.amazon.com/security/?nc2=h_dsc_aa_sec
- group: start
  title: ''
  type: Sandbox
  url: https://console.aws.amazon.com/console/home
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://aws.amazon.com/media/?nc2=h_sol_ind_med
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.amazon.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-codecommit/refs/heads/main/security/amazon-codecommit-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-codecommit-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-codecommit/refs/heads/main/security/amazon-codecommit-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-codecommit-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-codecommit/refs/heads/main/security/amazon-codecommit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-codecommit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/codecommit/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/codecommit/latest/userguide/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/codecommit/latest/APIReference/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/codecommit/getting-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/codecommit/pricing/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/aws/category/developer-tools/
coverage:
  checked: '2026-10-13'
  detail: API reference pages are rendered via JavaScript and no OpenAPI spec is publicly available.
  evidence:
  - status: 200
    url: https://docs.aws.amazon.com/cli/latest/reference/codecommit/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: Amazon CodeCommit is a fully managed source control service that hosts secure Git repositories. It enables developers to store and version code in the AWS cloud, integrates with other AWS services, provides fine‑grained access control, and supports pull requests, code reviews, and automated CI/CD pipelines. As part of the Amazon Web Services suite, CodeCommit offers high availability, encryption at rest and in transit, and scalable performance for teams of any size.
layout: provider
modified: '2026-10-12'
name: Amazon CodeCommit
nav: Providers
network: true
overview: 'Amazon CodeCommit is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SourceControl, Git, and Cloud.


  Amazon CodeCommit''s developer surface includes signup flow, sandbox, documentation, API reference, getting-started guide, pricing, support, and 19 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 62.5
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Amazon Codecommit Domain Security
  slug: amazon-codecommit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Codecommit Vulnerability Disclosure
  slug: amazon-codecommit-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Codecommit Trust Center
  slug: amazon-codecommit-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-codecommit
tags:
- Company
- SourceControl
- Git
- Cloud
website: https://aws.amazon.com/codecommit/
---
