---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 118
  human_in_the_loop: 12
  name: Didomi Agentic Access
  operation_count: 190
  slug: didomi-agentic-access
  summary_line: 190 operations · 118 acting · 12 human-in-the-loop
api_count: 37
apis:
- description: The Didomi Web SDK is the browser-side library that renders consent notices, preference centers, and privacy widgets, gates third-party tags on user consent, and writes IAB TCF v2 / GPP / Didomi conse
  name: Didomi Web SDK
  slug: didomi-web-sdk
- description: Didomi's Android and Android TV SDK delivers native consent notices, preference popups, and TCF / GPP / Didomi consent string generation in Java / Kotlin / Jetpack Compose apps. It shares consent with
  name: Didomi Android SDK
  slug: didomi-android-sdk
- description: The iOS / tvOS / Mac Catalyst SDK renders Didomi consent notices and preference centers natively in Swift and Objective-C apps, coordinates Apple's App Tracking Transparency (ATT) prompt with consent,
  name: Didomi iOS SDK
  slug: didomi-ios-sdk
- description: Didomi maintains first-party CMP plugins for React Native, Flutter, Unity (games and game consoles), Vega OS (LG webOS smart TVs), and Google AMP. Each wraps the platform's notice rendering, consent s
  name: Didomi Cross-Platform SDKs (React Native, Flutter, Unity, Vega OS, AMP)
  slug: didomi-cross-platform-sdks
- description: Open-source libraries published under github.com/didomi for encoding, decoding, and validating the Didomi consent string and the IAB TCF v2 consent string. Includes TypeScript (`consent-string`, `cons
  name: Didomi Consent String Toolkit
  slug: didomi-consent-string-toolkit
- description: The consents/events API from Didomi — 2 operation(s) for consents/events.
  name: Didomi consents/events API
  slug: didomi-consents-events-api
- description: The consents/proofs API from Didomi — 2 operation(s) for consents/proofs.
  name: Didomi consents/proofs API
  slug: didomi-consents-proofs-api
- description: The consents/tokens API from Didomi — 1 operation(s) for consents/tokens.
  name: Didomi consents/tokens API
  slug: didomi-consents-tokens-api
- description: The consents/users API from Didomi — 2 operation(s) for consents/users.
  name: Didomi consents/users API
  slug: didomi-consents-users-api
- description: Manage cookies set by a property
  name: Didomi cookies API
  slug: didomi-cookies-api
- description: The dashboards-urls API from Didomi — 1 operation(s) for dashboards-urls.
  name: Didomi dashboards-urls API
  slug: didomi-dashboards-urls-api
- description: Provisioned domains for consent notices and privacy centers
  name: Didomi domains API
  slug: didomi-domains-api
- description: The Integrations API from Didomi — 1 operation(s) for integrations.
  name: Didomi Integrations API
  slug: didomi-integrations-api
- description: Manage API keys
  name: Didomi keys API
  slug: didomi-keys-api
- description: List of available languages for the SDKs
  name: Didomi languages API
  slug: didomi-languages-api
- description: Manage members of an organization
  name: Didomi members API
  slug: didomi-members-api
- description: A metadata service
  name: Didomi metadata API
  slug: didomi-metadata-api
- description: The metadata-purpose-regulation-override API from Didomi — 2 operation(s) for metadata-purpose-regulation-override.
  name: Didomi metadata-purpose-regulation-override API
  slug: didomi-metadata-purpose-regulation-override-api
- description: The notices API from Didomi — 18 operation(s) for notices.
  name: Didomi notices API
  slug: didomi-notices-api
- description: Manage organizations
  name: Didomi organizations API
  slug: didomi-organizations-api
- description: Manage organization source systems
  name: Didomi organizations-source-systems API
  slug: didomi-organizations-source-systems-api
- description: The partners API from Didomi — 2 operation(s) for partners.
  name: Didomi partners API
  slug: didomi-partners-api
- description: The partners-default-purposes API from Didomi — 1 operation(s) for partners-default-purposes.
  name: Didomi partners-default-purposes API
  slug: didomi-partners-default-purposes-api
- description: The partners-legitimate-interest-purposes API from Didomi — 1 operation(s) for partners-legitimate-interest-purposes.
  name: Didomi partners-legitimate-interest-purposes API
  slug: didomi-partners-legitimate-interest-purposes-api
- description: The partners-spi-purposes API from Didomi — 1 operation(s) for partners-spi-purposes.
  name: Didomi partners-spi-purposes API
  slug: didomi-partners-spi-purposes-api
- description: The partners-storages API from Didomi — 2 operation(s) for partners-storages.
  name: Didomi partners-storages API
  slug: didomi-partners-storages-api
- description: Manage premium features
  name: Didomi premium-features API
  slug: didomi-premium-features-api
- description: Manage privacy centers
  name: Didomi privacy-centers API
  slug: didomi-privacy-centers-api
- description: The purposes API from Didomi — 3 operation(s) for purposes.
  name: Didomi purposes API
  slug: didomi-purposes-api
- description: The purposes-groups API from Didomi — 2 operation(s) for purposes-groups.
  name: Didomi purposes-groups API
  slug: didomi-purposes-groups-api
- description: Manage quotas
  name: Didomi quotas API
  slug: didomi-quotas-api
- description: Manage secrets
  name: Didomi secrets API
  slug: didomi-secrets-api
- description: Manage sessions
  name: Didomi sessions API
  slug: didomi-sessions-api
- description: Manage SSO connections
  name: Didomi sso-connections API
  slug: didomi-sso-connections-api
- description: Manage the taxonomy for vendors
  name: Didomi taxonomies API
  slug: didomi-taxonomies-api
- description: Manage vendors used by a property
  name: Didomi vendors API
  slug: didomi-vendors-api
- description: The widgets/notices/remote-configs API from Didomi — 1 operation(s) for widgets/notices/remote-configs.
  name: Didomi widgets/notices/remote-configs API
  slug: didomi-widgets-notices-remote-configs-api
arazzos:
- description: Create a vendor taxonomy item, register a cookie classified with it, and read the cookie back.
  name: Didomi Classify a Vendor and Register a Cookie
  slug: didomi-classify-and-register-cookie-workflow
- description: Create an end user, patch it to assign your organization's internal user ID, and read it back.
  name: Didomi Create a Consent User and Assign an Internal ID
  slug: didomi-create-and-assign-consent-user-workflow
- description: Create a privacy center for an organization and read it back to confirm it was created.
  name: Didomi Create and Verify a Privacy Center
  slug: didomi-create-privacy-center-workflow
- description: Look up an end user by your internal ID and fulfil a right-to-erasure request by deleting their consent record.
  name: Didomi Data Subject Erasure Request
  slug: didomi-data-subject-erasure-workflow
- description: Create a consent notice, deploy a notice configuration to production, and confirm the deployment.
  name: Didomi Deploy a Consent Notice
  slug: didomi-deploy-notice-workflow
- description: Create a consent notice, group it under a new notice template, and read the template back.
  name: Didomi Group Notices Under a Template
  slug: didomi-group-notices-template-workflow
- description: Create an end user, assign an internal ID, and issue a scoped JWT consent token for that user.
  name: Didomi Issue a Consent Token for an End User
  slug: didomi-issue-consent-token-workflow
- description: Create an organization, invite a first member into it, and read the organization back.
  name: Didomi Provision an Organization and Invite a Member
  slug: didomi-provision-organization-workflow
- description: Create a consent event for an end user, then branch on whether it is confirmed or pending approval.
  name: Didomi Record a Consent Event and Confirm Status
  slug: didomi-record-consent-event-workflow
- description: Register a cookie set by a property and read it back to confirm registration.
  name: Didomi Register and Verify a Cookie
  slug: didomi-register-cookie-workflow
- description: Create a notice text, submit a content version for the Didomi approval process, and read the content status.
  name: Didomi Submit Notice Text Content for Approval
  slug: didomi-submit-notice-text-content-workflow
- description: Upload a file as proof of consent for an organization and read it back to verify storage.
  name: Didomi Upload and Verify a Consent Proof
  slug: didomi-upload-consent-proof-workflow
artifact_total: 150
asyncapis:
- description: 'Outbound webhook events emitted by the Didomi platform when an end-user''s consent or preference state changes. PROVENANCE: Didomi publishes NO AsyncAPI document. This file is an API Evangelist generat'
  name: Didomi Consent Webhooks
  slug: didomi-consent-webhooks-asyncapi
- description: Didomi publishes a real outbound webhook surface. When an end-user changes a consent or preference on any of an organization's websites, apps or preference centers, Didomi POSTs a JSON payload to a cu
  name: Didomi Webhooks
  slug: didomi-webhooks
collections:
- collection_type: postman
  name: Didomi API
  slug: postman-didomi-platform-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Didomi consents/events API
  slug: open-didomi-consents-events-api
- collection_type: open
  name: Didomi consents/events consents/proofs API
  slug: open-didomi-consents-proofs-api
- collection_type: open
  name: Didomi consents/events consents/tokens API
  slug: open-didomi-consents-tokens-api
- collection_type: open
  name: Didomi consents/events consents/users API
  slug: open-didomi-consents-users-api
- collection_type: open
  name: Didomi consents/events cookies API
  slug: open-didomi-cookies-api
- collection_type: open
  name: Didomi consents/events dashboards-urls API
  slug: open-didomi-dashboards-urls-api
- collection_type: open
  name: Didomi consents/events domains API
  slug: open-didomi-domains-api
- collection_type: open
  name: Didomi consents/events Integrations API
  slug: open-didomi-integrations-api
- collection_type: open
  name: Didomi consents/events keys API
  slug: open-didomi-keys-api
- collection_type: open
  name: Didomi consents/events languages API
  slug: open-didomi-languages-api
- collection_type: open
  name: Didomi consents/events members API
  slug: open-didomi-members-api
- collection_type: open
  name: Didomi consents/events metadata API
  slug: open-didomi-metadata-api
- collection_type: open
  name: Didomi consents/events metadata-purpose-regulation-override API
  slug: open-didomi-metadata-purpose-regulation-override-api
- collection_type: open
  name: Didomi consents/events notices API
  slug: open-didomi-notices-api
- collection_type: open
  name: Didomi consents/events organizations API
  slug: open-didomi-organizations-api
- collection_type: open
  name: Didomi consents/events organizations-source-systems API
  slug: open-didomi-organizations-source-systems-api
- collection_type: open
  name: Didomi consents/events partners API
  slug: open-didomi-partners-api
- collection_type: open
  name: Didomi consents/events partners-default-purposes API
  slug: open-didomi-partners-default-purposes-api
- collection_type: open
  name: Didomi consents/events partners-legitimate-interest-purposes API
  slug: open-didomi-partners-legitimate-interest-purposes-api
- collection_type: open
  name: Didomi consents/events partners-spi-purposes API
  slug: open-didomi-partners-spi-purposes-api
- collection_type: open
  name: Didomi consents/events partners-storages API
  slug: open-didomi-partners-storages-api
- collection_type: open
  name: Didomi API
  slug: open-didomi-platform-api
- collection_type: open
  name: Didomi consents/events premium-features API
  slug: open-didomi-premium-features-api
- collection_type: open
  name: Didomi consents/events privacy-centers API
  slug: open-didomi-privacy-centers-api
- collection_type: open
  name: Didomi consents/events purposes API
  slug: open-didomi-purposes-api
- collection_type: open
  name: Didomi consents/events purposes-groups API
  slug: open-didomi-purposes-groups-api
- collection_type: open
  name: Didomi consents/events quotas API
  slug: open-didomi-quotas-api
- collection_type: open
  name: Didomi consents/events secrets API
  slug: open-didomi-secrets-api
- collection_type: open
  name: Didomi consents/events sessions API
  slug: open-didomi-sessions-api
- collection_type: open
  name: Didomi consents/events sso-connections API
  slug: open-didomi-sso-connections-api
- collection_type: open
  name: Didomi consents/events taxonomies API
  slug: open-didomi-taxonomies-api
- collection_type: open
  name: Didomi consents/events vendors API
  slug: open-didomi-vendors-api
- collection_type: open
  name: Didomi consents/events widgets/notices/remote-configs API
  slug: open-didomi-widgets-notices-remote-configs-api
common:
- group: build
  title: ''
  type: Packages
  url: packages/didomi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/didomi-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/didomi-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/didomi-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/didomi-platform-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/didomi-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/didomi-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/didomi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/didomi-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/didomi-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/didomi-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/didomi-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/didomi-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/didomi-components.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/didomi-consent-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/didomi-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: security/didomi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/didomi-vulnerability-disclosure.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.didomi.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api.didomi.io/docs/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/kinlaneapi/didomi/overview
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/didomi/consent-string/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/didomi/consent-string/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/didomi-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/didomi-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/didomi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/didomi-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/didomi/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/didomi-classify-and-register-cookie-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/didomi-create-and-assign-consent-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/didomi-create-privacy-center-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/didomi-data-subject-erasure-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/didomi-deploy-notice-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/didomi-group-notices-template-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/didomi-issue-consent-token-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/didomi-provision-organization-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/didomi-record-consent-event-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/didomi-register-cookie-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/didomi-submit-notice-text-content-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/didomi-upload-consent-proof-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://www.didomi.io
- group: docs
  title: ''
  type: Documentation
  url: https://developers.didomi.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.didomi.io/readme
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.didomi.io/cmp/web-sdk/getting-started
- group: start
  title: ''
  type: Console
  url: https://console.didomi.io
- group: start
  title: ''
  type: Signup
  url: https://www.didomi.io/contact-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.didomi.io/offers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.didomi.io/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.didomi.io/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.didomi.io/cookie-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.didomi.io
- group: company
  title: ''
  type: Blog
  url: https://www.didomi.io/blog
- group: operate
  title: ''
  type: Support
  url: https://support.didomi.io
- group: learn
  title: ''
  type: Training
  url: https://www.didomi.io/didomi-academy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/didomi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/didomi
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@didomi/react
- group: build
  title: ''
  type: SDKs
  url: https://github.com/didomi/react-native
- group: build
  title: ''
  type: SDKs
  url: https://github.com/didomi/flutter
- group: build
  title: ''
  type: SDKs
  url: https://github.com/didomi/unity
- group: build
  title: ''
  type: SDKs
  url: https://github.com/didomi/didomi-ios-sdk-spm
- group: build
  title: ''
  type: Tools
  url: https://github.com/didomi/gtm-template
- group: build
  title: ''
  type: Tools
  url: https://github.com/didomi/magento
- group: build
  title: ''
  type: Tools
  url: https://github.com/didomi/mparticle-javascript-integration-didomi
- group: build
  title: ''
  type: Tools
  url: https://github.com/didomi/firebase
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/didomi/samples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/didomi/boilerplate-fastly-reverse-proxy-didomi-cmp
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/didomi/boilerplate-aws-cloudfront-reverse-proxy-didomi-cmp
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/didomi/boilerplate-cloudflare-reverse-proxy-didomi-cmp
- group: design
  title: ''
  type: JSONLD
  url: json-ld/didomi-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/didomi-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/didomi-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/didomi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/didomi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/didomi-finops.yml
created: '2026-05-25'
description: Didomi is a Paris-based consent and preference management platform (CMP/PMP) that helps publishers, advertisers, retailers, and large enterprises collect, manage, and act on user privacy choices across web, mobile, CTV, and AMP surfaces. The platform covers GDPR, CCPA and the wider US state-law landscape, IAB TCF v2.x, Google Consent Mode v2, the IAB GPP, GPC, the EU DMA, Chilean Law 25, Australian privacy law, and other regulations through a single multi-regulation configuration model. Didomi exposes a JSON REST API (https://api.didomi.io/v1/) plus first-party SDKs for Web, iOS/tvOS, Android/Android TV, Unity, React Native, Flutter, Vega OS, and AMP, alongside IAB-compliant consent string tooling and reverse-proxy boilerplates for Fastly, CloudFront, and Cloudflare.
examples:
- key_count: 10
  name: Didomi Consent Event Example
  slug: didomi-consent-event-example
- key_count: 15
  name: Didomi Consent Notice Example
  slug: didomi-consent-notice-example
- key_count: 11
  name: Didomi Privacy Request Example
  slug: didomi-privacy-request-example
features:
- description: One Didomi notice can target GDPR, CCPA and the wider US-state landscape, TCF v2.x, GPP, GPC, EU DMA, Chilean Law 25, Australian privacy law, and Nordic regimes from a single multi-regulation configuration.
  name: Multi-regulation CMP
- description: Didomi is an IAB-registered CMP that emits, validates, and decodes TCF v2.x and IAB GPP consent strings and honors Global Privacy Control signals.
  name: IAB TCF v2.x / GPP / GPC compliance
- description: Native, certified Google Consent Mode v2 integration on Web and Mobile, plus Amazon Consent Signal and Microsoft UET Consent Mode bridges.
  name: Google Consent Mode v2
- description: A separately licensed Preference Management module exposing custom preference centers, headless preference widgets, marketing channel preferences, and email/SMS opt-in flows.
  name: Preference Management Platform (PMP)
- description: DSAR / privacy-request intake forms, internal workflow, evidence storage, and reporting for GDPR Articles 15-22 and CCPA opt-out / delete rights.
  name: Privacy Requests Management
- description: Automated scanning of websites and apps for vendor coverage, unauthorized tags, and CMP behavior; CSV / Excel compliance reports surfaced via the Platform API and Console.
  name: Compliance Monitoring & Reports
- description: Configurable, themed widgets (preference centers, DSAR forms, headless React widgets, embeddable widgets) deployable on Didomi-managed or customer-owned domains.
  name: Privacy Widgets
- description: Serve consent notices from the customer's own domain via DNS delegation or via reverse-proxy boilerplates for Fastly, AWS CloudFront, and Cloudflare.
  name: Consent Notice on Custom Domain
- description: Authenticated users can carry their consent state across domains and across devices via the platform's tokens and links APIs.
  name: Cross-device / cross-domain consent sharing
- description: Server-side tagging product (Addingwell, acquired by Didomi) integrated with the consent model for first-party tagging without browser-side third-party calls.
  name: Server-side Google Tag Manager (Addingwell)
- description: First-party SDKs for Web, iOS / tvOS / Mac Catalyst, Android / Android TV, React Native, Flutter, Unity, Vega OS (LG smart TVs), and Google AMP.
  name: Cross-Platform SDKs
- description: Open-source consent-string encoders / decoders in TypeScript, Rust (with C and Java FFI), and Go, plus the iabtcf-es TCF v2 toolkit fork.
  name: Open Consent String tooling
- description: Platform API uses short-lived (one-hour) JWT access tokens obtained by exchanging API key + secret against POST /v1/sessions.
  name: JWT bearer authentication
- description: 100 requests per 15 seconds per organization across most routes, with the high-volume /consents/* family exempt; RateLimit / RateLimit-Policy headers and 429 + Retry-After when exceeded.
  name: Token-bucket rate limiting
- description: Programmatic management of organization members, roles, SSO connections, partner-portal sessions, and per-key API quotas via the Platform API.
  name: SSO and member management
finops:
- name: Didomi Finops
  service_category: ''
  slug: didomi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/didomi.png
integrations:
- description: First-class Didomi GTM template and native integration; certified Google Consent Mode v2 signal delivery.
  name: Google Tag Manager
- description: Pass TCF consent signal and non-personalized-ads (NPA) fallback to Google ad stack.
  name: Google Ad Manager / AdSense / AdX
- description: Documented integration patterns for managing tag firing under Didomi consent.
  name: Adobe Launch / Adobe DTM
- description: Native Tealium integration for tag governance under Didomi consent.
  name: Tealium iQ
- description: Tag firing control through Eulerian tag management.
  name: Eulerian
- description: Pass TCF v2 / US state-law consent to Prebid header bidding wrappers.
  name: Prebid
- description: Forward consent state to Salesforce DMP / Krux.
  name: Salesforce DMP (Krux)
- description: Integration with Piano Analytics (formerly AT Internet) for consent-aware analytics.
  name: Piano Analytics (AT Internet)
- description: Consent integration with Kameleoon experimentation / personalization platform.
  name: Kameleoon
- description: Privacy-friendly analytics integration.
  name: Simple Analytics
- description: Native bridge to Amazon's consent signal for Amazon Publisher Services.
  name: Amazon Consent Signal
- description: Native bridge to Microsoft UET / Bing Ads consent mode.
  name: Microsoft UET Consent Mode
- description: First-party JavaScript kit integration for mParticle customer data platform.
  name: mParticle
- description: Didomi Magento 2 extension for consent management on Magento storefronts.
  name: Magento 2
- description: Cloud Functions integration to ship Didomi consent into the Firebase / Google ecosystem.
  name: Firebase
- description: Public Postman workspace and collections for the Platform API.
  name: Postman
json_schemas:
- name: Didomi Consent Event
  property_count: 10
  slug: didomi-consent-event
- name: Didomi Consent Notice
  property_count: 15
  slug: didomi-consent-notice
- name: Didomi Privacy Request (DSAR)
  property_count: 11
  slug: didomi-privacy-request
json_structures:
- name: Didomi Consent Event Structure
  property_count: 10
  slug: didomi-consent-event-structure
jsonld:
- class_count: 22
  name: Didomi Context
  property_count: 10
  slug: didomi-context
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP tool surface derived from the Didomi OpenAPI (Didomi ships no MCP server)
  slug: candidate-mcp-tool-surface-derived-from-the-didomi-openapi-didomi-ships-no-mcp-server
modified: '2026-08-13'
name: Didomi
nav: Providers
network: true
overview: 'Didomi publishes 32 APIs on the [APIs.io](https://apis.io/) network, including consents/events API, consents/proofs API, consents/tokens API, and 29 more. Tagged areas include Advertising, AdTech, CCPA, CMP, and Consent.


  The Didomi catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Didomi''s developer surface includes changelog, API reference, authentication, developer portal, documentation, getting-started guide, developer console, and 69 more developer resources.'
plans:
- name: Didomi Plans Pricing
  plan_count: 6
  slug: didomi-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Didomi Rate Limits
  slug: didomi-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Didomi API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: didomi-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Didomi API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 5
  slug: didomi-rules
score:
  band: exemplar
  composite: 78.2
  delta: -7.2
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 55.3
    contract_quality: 76.6
    developer_ergonomics: 80.4
    discoverability: 57.4
    governance: 55.3
    operational_transparency: 81.6
  previous_composite: 85.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 32
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/didomi/refs/heads/main/screenshots/didomi-2026-06-20T180026.png
security:
- kind: authentication
  name: Didomi Authentication
  slug: didomi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Didomi Domain Security
  slug: didomi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Didomi Vulnerability Disclosure
  slug: didomi-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Didomi Trust Center
  slug: didomi-trust-center
  summary_line: ISO 27001, GDPR
slug: didomi
solutions:
- description: IAB TCF v2.x CMP specialized for ad-funded publishers and media groups.
  name: CMP for Publishers
- description: Consent capture and forwarding for advertiser stacks, MarTech tools, and CDPs.
  name: CMP for Advertisers and Brands
- description: Native CTV consent for Vega OS, Android TV, tvOS, and other TV runtimes.
  name: CMP for Connected TV
- description: iOS / Android / cross-platform consent management coordinated with ATT and Google Consent Mode v2.
  name: CMP for Mobile Apps
- description: Marketing-preference and channel-opt-in management beyond regulatory consent.
  name: Preference Management Platform
- description: GDPR / CCPA DSAR intake, internal workflow, and audit-grade evidence.
  name: Privacy Requests
- description: Continuous scanning of digital properties for vendor coverage, unauthorized tags, and CMP misconfigurations.
  name: Compliance Monitoring
- description: Server-side Google Tag Manager product acquired by Didomi, integrated with the Didomi consent model.
  name: Addingwell - Server-side Tagging
tags:
- Advertising
- AdTech
- CCPA
- CMP
- Consent
- Consent Management
- DSAR
- Data Privacy
- GDPR
- IAB TCF
- MarTech
- Preference Management
- Privacy
- Privacy Requests
- Regulatory Compliance
use_cases:
- description: News publishers and media groups (Yahoo, large French / European publishers) use Didomi as their IAB TCF CMP so SSPs and DSPs receive valid consent signals and ad inventory is monetizable under GDPR.
  name: Publisher CMP for ad monetization
- description: Retail and e-commerce brands (Lacoste, Rakuten, Michelin) capture consent for analytics, personalization, marketing, and CRM channels via the CMP and Preference Management Platform.
  name: Retailer / e-commerce consent and preference
- description: CTV apps on LG webOS / Vega OS, Android TV, and tvOS use Didomi's native SDKs to render consent on TV screens and emit the same TCF / Didomi consent strings used on web.
  name: Connected TV CMP
- description: Enterprises route GDPR Article 15-22 and CCPA opt-out / delete requests through Didomi's Privacy Requests product, with audit-grade proofs and structured exports.
  name: DSAR / privacy-request intake at scale
- description: Media groups operating dozens of domains share a single consent across all properties and across user devices via consent tokens and links.
  name: Cross-domain / cross-device consent for media groups
- description: Marketing teams replace browser-side third-party tags with server-side Google Tag Manager via Addingwell, gated on Didomi consent.
  name: Server-side first-party tagging
website: https://developers.didomi.io/
---
