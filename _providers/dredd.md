---
access_model:
  confidence: high
  label: Free and open source
  onboarding: unknown
  pricing: free
  public: true
  source:
  - license
  - plans
  trial: false
  try_now: false
api_count: 1
apis:
- description: 'Dredd is a language-agnostic command-line tool for validating an API description document against a backend implementation. It supports API Blueprint, OpenAPI 2.0, and OpenAPI 3.0, and provides hooks '
  name: Dredd
  slug: dredd
artifact_total: 5
common:
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apiaryio/dredd/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apiaryio/dredd/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dredd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dredd.org
- group: docs
  title: ''
  type: Documentation
  url: https://dredd.org/en/latest/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apiaryio
- group: start
  title: ''
  type: GettingStarted
  url: https://dredd.org/en/latest/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://github.com/apiaryio/dredd/issues
- group: other
  title: ''
  type: DockerImage
  url: https://hub.docker.com/r/apiaryio/dredd
- group: build
  title: ''
  type: Packages
  url: packages/dredd-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dredd-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/dredd-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dredd-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dredd-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dredd-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dredd-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dredd-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/dredd-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dredd-rate-limits.yml
created: '2026-03-25'
description: Dredd is a language-agnostic, MIT-licensed open source command-line tool that validates a running HTTP API against its own API description document. It compiles every request/response pair documented in an API Blueprint, OpenAPI 2.0 or (experimentally) OpenAPI 3.0 file into an HTTP transaction, calls the API under test, and reports where the implementation and the documentation disagree. Hooks written in Node.js, Ruby, Python, PHP, Perl, Go or Rust handle per-transaction test setup and teardown, and pluggable reporters (xunit, dot, markdown, html) wire it into CI. Dredd publishes no API of its own — it is a client you install and run. The project has been archived and unmaintained since November 2024; the last release, 14.1.0, shipped in November 2021.
finops:
- name: Dredd Finops
  service_category: API
  slug: dredd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dredd.png
layout: provider
modified: '2026-09-13'
name: Dredd
nav: Providers
network: true
overview: 'Dredd publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Contract Testing, API Testing, OpenAPI, API Blueprint, and Tooling.


  Dredd''s developer surface includes documentation, getting-started guide, support, CLI, changelog, and 14 more developer resources.'
plans:
- name: Dredd Plans Pricing
  plan_count: 0
  slug: dredd-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Dredd Rate Limits
  slug: dredd-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/dredd/refs/heads/main/screenshots/dredd-2026-06-20T180221.png
security:
- kind: domain-security
  name: Dredd Domain Security
  slug: dredd-domain-security
  summary_line: TLSv1.3
slug: dredd
tags:
- Contract Testing
- API Testing
- OpenAPI
- API Blueprint
- Tooling
- Developer Tools
- Command Line
- Continuous Integration
- JSON Schema
- Open Source
website: https://dredd.org
---
