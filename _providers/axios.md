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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Axios is a promise-based HTTP client for the browser and Node.js with automatic JSON data transformation and request/response interceptors.
  name: Axios
  slug: axios
artifact_total: 23
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/axios/axios/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/axios/axios/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/axios/axios/blob/v1.x/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/axios/axios/blob/v1.x/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/axios/axios/blob/v1.x/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/axios/axios/blob/v1.x/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/axios-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://axios-http.com
- group: docs
  title: ''
  type: Documentation
  url: https://axios-http.com/docs/intro
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/axios/axios
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/axios/axios
- group: build
  title: npm Package
  type: SDKs
  url: https://www.npmjs.com/package/axios
created: '2026-03-27'
description: Axios is a promise-based HTTP client for the browser and Node.js with automatic JSON data transformation and request/response interceptors.
features:
- description: Built on promises for clean async/await and .then() chaining patterns.
  name: Promise-Based
- description: Works in both browser and Node.js environments with automatic XHR/http adapter selection.
  name: Browser and Node.js Support
- description: Automatically serializes JavaScript objects to JSON and parses JSON responses.
  name: Automatic JSON Transformation
- description: Add custom logic to requests and responses before they are handled.
  name: Request and Response Interceptors
- description: Cancel in-flight requests using AbortController or the CancelToken API.
  name: Request Cancellation
- description: Built-in client-side XSRF protection support.
  name: XSRF Protection
- description: Configure request timeouts for automatic cancellation of long-running requests.
  name: Timeout Support
- description: Track upload and download progress with onUploadProgress and onDownloadProgress callbacks.
  name: Progress Tracking
finops:
- name: Axios Finops
  service_category: API
  slug: axios-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/axios.png
integrations:
- description: Commonly used for data fetching in React applications with hooks.
  name: React
- description: Official recommendation for HTTP requests in Vue.js applications.
  name: Vue.js
- description: Used for server-side HTTP requests with the native http/https adapter.
  name: Node.js
- description: First-class TypeScript support with bundled type definitions.
  name: TypeScript
- description: Easily mocked with jest.mock() for unit testing HTTP-dependent code.
  name: Jest
layout: provider
modified: '2026-04-19'
name: Axios
nav: Providers
network: true
overview: 'Axios publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Clients, HTTP Client, JavaScript, and Node.js.


  Axios'' developer surface includes documentation and 11 more developer resources.'
plans:
- name: Axios Plans Pricing
  plan_count: 3
  slug: axios-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Axios Rate Limits
  slug: axios-rate-limits
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 84.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 26.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/axios/refs/heads/main/screenshots/axios-2026-06-20T172811.png
security:
- kind: domain-security
  name: Axios Domain Security
  slug: axios-domain-security
  summary_line: TLSv1.3 · HSTS
slug: axios
tags:
- Clients
- HTTP Client
- JavaScript
- Node.js
use_cases:
- description: Consume RESTful APIs from frontend applications and Node.js servers.
  name: REST API Consumption
- description: Upload files with progress tracking to backend services.
  name: File Uploads
- description: Add auth tokens and headers automatically via request interceptors.
  name: Authentication
- description: Fetch data in React, Vue, Angular, and other JavaScript frameworks.
  name: Data Fetching
- description: Test API integrations in Node.js scripts and test suites.
  name: API Testing
website: https://axios-http.com
---
