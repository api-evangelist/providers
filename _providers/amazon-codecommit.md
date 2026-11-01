---
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.3
  scored_at: '2026-10-31'
api_count: 11
apis:
- description: AWS CodeCommit API provides operations for repositories, commits, branches, and pull requests.
  name: CodeCommit API
  slug: codecommit-api
- baseURL: https://codecommit.amazonaws.com
  baseurl_source: declared
  description: The Codecommit Approval Rule Template API from Amazon CodeCommit — 8 operation(s) for codecommit approval rule template.
  name: Amazon CodeCommit Codecommit Approval Rule Template API
  slug: amazon-codecommit-approval-rule-template-api
- baseURL: https://codecommit.amazonaws.com
  baseurl_source: declared
  description: The Codecommit Branch API from Amazon CodeCommit — 3 operation(s) for codecommit branch.
  name: Amazon CodeCommit Codecommit Branch API
  slug: amazon-codecommit-branch-api
- baseURL: https://codecommit.amazonaws.com
  baseurl_source: declared
  description: The Codecommit Comment API from Amazon CodeCommit — 4 operation(s) for codecommit comment.
  name: Amazon CodeCommit Codecommit Comment API
  slug: amazon-codecommit-comment-api
- baseURL: https://codecommit.amazonaws.com
  baseurl_source: declared
  description: The Codecommit Commit API from Amazon CodeCommit — 3 operation(s) for codecommit commit.
  name: Amazon CodeCommit Codecommit Commit API
  slug: amazon-codecommit-commit-api
- baseURL: https://codecommit.amazonaws.com
  baseurl_source: declared
  description: The Codecommit File API from Amazon CodeCommit — 3 operation(s) for codecommit file.
  name: Amazon CodeCommit Codecommit File API
  slug: amazon-codecommit-file-api
- baseURL: https://codecommit.amazonaws.com
  baseurl_source: declared
  description: The Codecommit Merge Conflict API from Amazon CodeCommit — 3 operation(s) for codecommit merge conflict.
  name: Amazon CodeCommit Codecommit Merge Conflict API
  slug: amazon-codecommit-merge-conflict-api
- baseURL: https://codecommit.amazonaws.com
  baseurl_source: declared
  description: The Codecommit Operations API from Amazon CodeCommit — 44 operation(s) for codecommit operations.
  name: Amazon CodeCommit Codecommit Operations API
  slug: amazon-codecommit-operations-api
- baseURL: https://codecommit.amazonaws.com
  baseurl_source: declared
  description: The Codecommit Pull Request API from Amazon CodeCommit — 3 operation(s) for codecommit pull request.
  name: Amazon CodeCommit Codecommit Pull Request API
  slug: amazon-codecommit-pull-request-api
- baseURL: https://codecommit.amazonaws.com
  baseurl_source: declared
  description: The Codecommit Repository API from Amazon CodeCommit — 6 operation(s) for codecommit repository.
  name: Amazon CodeCommit Codecommit Repository API
  slug: amazon-codecommit-repository-api
- baseURL: https://codecommit.amazonaws.com
  baseurl_source: declared
  description: The Codecommit Repository Trigger API from Amazon CodeCommit — 3 operation(s) for codecommit repository trigger.
  name: Amazon CodeCommit Codecommit Repository Trigger API
  slug: amazon-codecommit-repository-trigger-api
artifact_total: 14
common:
- group: other
  href: https://artifacts.apis.io/amazon-codecommit/capabilities/amazon-codecommit-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-codecommit-capability-edges.yml
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: agent
  href: https://artifacts.apis.io/amazon-codecommit/llms/amazon-codecommit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amazon-codecommit-llms.txt
- group: auth
  href: https://artifacts.apis.io/amazon-codecommit/well-known/amazon-codecommit-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amazon-codecommit-security.txt
- group: agent
  href: https://artifacts.apis.io/amazon-codecommit/well-known/amazon-codecommit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amazon-codecommit-well-known.yml
- group: other
  href: https://artifacts.apis.io/amazon-codecommit/hosts/amazon-codecommit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amazon-codecommit-hosts.yml
- group: other
  href: https://artifacts.apis.io/amazon-codecommit/vendors/amazon-codecommit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amazon-codecommit-vendors.yml
- group: build
  href: https://artifacts.apis.io/amazon-codecommit/packages/amazon-codecommit-packages.yml
  title: ''
  type: SDKs
  url: packages/amazon-codecommit-packages.yml
- group: build
  href: https://artifacts.apis.io/amazon-codecommit/packages/amazon-codecommit-packages.yml
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
  href: https://artifacts.apis.io/amazon-codecommit/security/amazon-codecommit-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-codecommit-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amazon-codecommit/security/amazon-codecommit-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-codecommit-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-codecommit/security/amazon-codecommit-domain-security.yml
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
overview: 'Amazon CodeCommit is listed with 11 APIs on the [APIs.io](https://apis.io/) network, including Codecommit Approval Rule Template API, Codecommit Branch API, Codecommit Comment API, and 8 more. Tagged areas include Company, Version Control, and Cloud.


  Amazon CodeCommit''s developer surface includes signup flow, sandbox, documentation, API reference, getting-started guide, pricing, support, and 20 more developer resources.'
random_paper: 23
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 33.0
    catalog_earned_first_party: 0.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 12.3
  facets:
    access_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 53.3
    developer_ergonomics: 59.5
    discoverability: 60.7
    operational_transparency: 15.8
  previous_composite: 35.4
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
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
- Version Control
- Cloud
website: https://aws.amazon.com/codecommit/
---
