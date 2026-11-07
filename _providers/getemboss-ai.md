---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: true
    agentic_commerce: self
    auth_clarity: served
    consent_identity: true
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: three_quarters
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 75.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 33
  human_in_the_loop: 1
  name: Getemboss Ai Agentic Access
  operation_count: 66
  slug: getemboss-ai-agentic-access
  summary_line: 66 operations · 33 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: 'Remote Model Context Protocol server at https://api.getemboss.ai/mcp (Streamable HTTP) exposing twenty form-filling tools under forms:read / forms:write scopes. OAuth 2.1 with PKCE and dynamic client '
  name: Emboss MCP Server
  slug: emboss-mcp-server
- description: Agent2Agent interface at https://api.getemboss.ai/a2a (JSON-RPC, A2A 1.0) discovered through a signed agent card served at /.well-known/agent-card.json on both getemboss.ai and api.getemboss.ai. Twent
  name: Emboss A2A Agent
  slug: emboss-a2a-agent
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: The Admin API from Emboss — 40 operation(s) for admin.
  name: Emboss Admin API
  phrasing_intents:
  - id: admin_get_account_admin_account_get
    intent: View an owner's account and retention default
    question: What retention default will new forms inherit for this account owner?
  - id: admin_patch_account_admin_account_patch
    intent: Change an owner's default retention policy
    question: How do I change the default retention policy for an account as an admin?
  - id: admin_usage_admin_usage_get
    intent: View usage totals for an owner as admin
    question: Can an admin see the current usage summary for any account owner?
  - id: admin_usage_detail_admin_usage_detail_get
    intent: Get an owner's detailed usage for a month
    question: Can I see a detailed usage breakdown for one owner in a specific month?
  - id: admin_billing_breakdown_admin_billing_breakdown_get
    intent: Get an owner's billing breakdown for a month
    question: What will an owner be billed for in a given month, line by line?
  - id: admin_forms_admin_forms_get
    intent: List an owner's forms as admin
    question: Can an admin search through all the forms a particular owner has uploaded?
  - id: admin_create_form_admin_forms_post
    intent: Upload a fillable form on behalf of an owner
    question: How do I create a fillable form for a customer from the admin batch-fill page?
  - id: admin_batch_runs_admin_forms_batch_runs_get
    intent: List an owner's batch-fill runs
    question: Which batch-fill runs has an owner kicked off?
  phrasing_ops: 43
  slug: getemboss-ai-admin-api
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: The App API from Emboss — 3 operation(s) for app.
  name: Emboss App API
  phrasing_intents:
  - id: app_login_app_login_post
    intent: Sign in to the mobile app
    question: How does the app sign a user in with email and password?
  - id: app_refresh_app_refresh_post
    intent: Refresh an app session token
    question: What do I do when the app's access token expires?
  - id: app_logout_app_logout_post
    intent: Sign out of the app
    question: How do I sign a device out of the app?
  phrasing_ops: 3
  slug: getemboss-ai-app-api
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: The Artifacts API from Emboss — 2 operation(s) for artifacts.
  name: Emboss Artifacts API
  phrasing_intents:
  - id: get_artifact_artifacts__artifact_id__get
    intent: Get an artifact's metadata
    question: What do I know about a generated document artifact, like its type and size?
  - id: get_artifact_content_artifacts__artifact_id__content_get
    intent: Download an artifact's content
    question: How do I download the actual file behind an artifact?
  phrasing_ops: 2
  slug: getemboss-ai-artifacts-api
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: The D API from Emboss — 1 operation(s) for d.
  name: Emboss D API
  phrasing_intents:
  - id: redeem_d__token__get
    intent: Redeem a download link token
    question: How do I open a download link I was sent?
  phrasing_ops: 1
  slug: getemboss-ai-d-api
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: The Fax API from Emboss — 2 operation(s) for fax.
  name: Emboss Fax API
  phrasing_intents:
  - id: send_fax_fax_post
    intent: Send a fax from my account
    question: How do I fax one or more PDFs to a number from my account?
  - id: get_fax_fax__job_id__get
    intent: Check a fax's delivery status
    question: Did my fax go through?
  phrasing_ops: 2
  slug: getemboss-ai-fax-api
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: The Forms API from Emboss — 25 operation(s) for forms.
  name: Emboss Forms API
  phrasing_intents:
  - id: account_quote_forms_quote_post
    intent: Quote the account price for processing a form
    question: What would it cost my account to process this PDF before I commit?
  - id: create_form_forms_post
    intent: Upload a PDF and make it a fillable form
    question: How do I upload a PDF so Emboss detects its fields?
  - id: list_forms_forms_get
    intent: List my uploaded forms
    question: Which forms have I uploaded to my account?
  - id: get_form_forms__form_id__get
    intent: Get a form and its processing status
    question: Is my uploaded form done extracting yet?
  - id: delete_form_forms__form_id__delete
    intent: Delete a form and its documents
    question: How do I delete a form and its stored documents?
  - id: get_contract_forms__form_id__contract_get
    intent: Get a form's field contract
    question: What fields does my form have and which are required?
  - id: get_fillable_forms__form_id__fillable_get
    intent: Download the fillable PDF of a form
    question: Where do I download the fillable version of a flat PDF I uploaded?
  - id: get_thumbnail_forms__form_id__thumbnail_get
    intent: Get a form's thumbnail image
    question: Can I get a small preview image of one of my forms?
  phrasing_ops: 27
  slug: getemboss-ai-forms-api
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: The Health API from Emboss — 1 operation(s) for health.
  name: Emboss Health API
  phrasing_intents:
  - id: health_health_get
    intent: Check that the service is up
    question: Is the Emboss service up right now?
  phrasing_ops: 1
  slug: getemboss-ai-health-api
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: The Keys API from Emboss — 2 operation(s) for keys.
  name: Emboss Keys API
  phrasing_intents:
  - id: create_key_keys_post
    intent: Create a new API key
    question: How do I generate a new API key?
  - id: list_keys_keys_get
    intent: List an owner's API keys
    question: Which API keys exist on my account?
  - id: delete_key_keys__key_id__delete
    intent: Delete an API key
    question: How do I permanently delete an API key I no longer need?
  - id: patch_key_keys__key_id__patch
    intent: Rename or change the state of an API key
    question: Can I rename an existing API key?
  phrasing_ops: 4
  slug: getemboss-ai-keys-api
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: The Library API from Emboss — 1 operation(s) for library.
  name: Emboss Library API
  phrasing_intents:
  - id: get_library_library_get
    intent: Browse or search the form library
    question: Which ready-made government forms are in the library?
  phrasing_ops: 1
  slug: getemboss-ai-library-api
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: The Oauth API from Emboss — 5 operation(s) for oauth.
  name: Emboss OAuth API
  phrasing_intents:
  - id: preflight_oauth___rest__options
    intent: Answer CORS preflight for OAuth routes
    question: Do the OAuth endpoints support CORS preflight requests from browsers?
  - id: register_oauth_register_post
    intent: Register an OAuth client dynamically
    question: How does an MCP client register itself for OAuth?
  - id: authorize_oauth_authorize_get
    intent: Start the OAuth authorization flow
    question: Where do I send a user to grant my app access to their account?
  - id: token_oauth_token_post
    intent: Exchange an OAuth code for tokens
    question: How do I turn an authorization code into an access token?
  - id: revoke_oauth_revoke_post
    intent: Revoke an OAuth token
    question: How does a client revoke an OAuth token it holds?
  phrasing_ops: 5
  slug: getemboss-ai-oauth-api
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: The Openapi.json API from Emboss — 1 operation(s) for openapi.json.
  name: Emboss Openapi.json API
  phrasing_intents:
  - id: pay_openapi_manifest_openapi_json_get
    intent: Get the pay manifest at the site root
    question: Where do discovery tools find the paid operations manifest?
  phrasing_ops: 1
  slug: getemboss-ai-openapi-json-api
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: The Pay API from Emboss — 7 operation(s) for pay.
  name: Emboss Pay API
  phrasing_intents:
  - id: pay_index_pay_get
    intent: List the paid operations and their docs
    question: Which pay-per-use operations are available and where are their docs?
  - id: pay_openapi_manifest_pay_openapi_json_get
    intent: Get the pay manifest at its legacy /pay path
    question: Does the older /pay/openapi.json link still serve the pay manifest?
  - id: pay_llms_txt_pay_llms_txt_get
    intent: Get the llms.txt for the pay door
    question: Is there an llms.txt that tells agents the starting prices for paid ops?
  - id: pay_pricing_alias_pay_pricing_get
    intent: Get the public price list under /pay
    question: What does each pay-per-use operation cost, listed next to the quote endpoint?
  - id: pay_quote_pay_quote_post
    intent: Inspect a PDF's exact price before paying
    question: How many pages does my PDF have and is it already fillable, before I pay?
  - id: pay_pay__op__post
    intent: Pay for and run a named PDF operation
    question: How do I pay for and run one operation, like fill or fax, by its name?
  - id: pay_job_status_pay_jobs__job_id__get
    intent: Poll a paid job's status for free
    question: How do I check on a paid job without paying again or having an account?
  phrasing_ops: 7
  slug: getemboss-ai-pay-api
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: The Pricing API from Emboss — 1 operation(s) for pricing.
  name: Emboss Pricing API
  phrasing_intents:
  - id: public_price_list_pricing_get
    intent: Get the public price list
    question: How much does Emboss charge for filling, reading and faxing PDFs?
  phrasing_ops: 1
  slug: getemboss-ai-pricing-api
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: The Proposals API from Emboss — 6 operation(s) for proposals.
  name: Emboss Proposals API
  phrasing_intents:
  - id: commit_proposals__proposal_id__commit_post
    intent: Commit a reviewed proposal into a filled PDF
    question: How do I accept a proposal and render the final filled form?
  - id: get_proposal_proposals__proposal_id__get
    intent: Review a fill proposal
    question: What answers were proposed for my form before I commit?
  - id: receipt_proposals__proposal_id__receipt_get
    intent: Get the receipt for a committed proposal
    question: Where do I get a receipt after committing a proposal?
  - id: commit_pdf_proposals__proposal_id__pdf_get
    intent: Download the PDF from a committed proposal
    question: Where do I download the filled PDF after committing a proposal?
  - id: add_attachment_proposals__proposal_id__attachments_post
    intent: Attach a supporting file to a proposal
    question: Can I attach a supporting document to a proposal before committing?
  - id: remove_attachment_proposals__proposal_id__attachments__n__delete
    intent: Remove an attachment from a proposal
    question: How do I take an attachment back off a proposal?
  phrasing_ops: 6
  slug: getemboss-ai-proposals-api
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: The Sessions API from Emboss — 5 operation(s) for sessions.
  name: Emboss Sessions API
  phrasing_intents:
  - id: create_session_sessions_post
    intent: Start an interactive fill session for a form
    question: How do I start filling a form field by field interactively?
  - id: get_session_sessions__sid__get
    intent: Get a fill session's current field values
    question: What values have been entered so far in my fill session?
  - id: put_fields_sessions__sid__fields_put
    intent: Set field values in a fill session
    question: How do I enter or change answers in an open fill session?
  - id: fill_sessions__sid__fill_post
    intent: Render the filled PDF for a session
    question: How do I finish a session and produce the filled PDF?
  - id: session_pdf_sessions__sid__pdf_get
    intent: Download a session's filled PDF
    question: Where do I download the PDF from a completed fill session?
  phrasing_ops: 5
  slug: getemboss-ai-sessions-api
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: The Stripe API from Emboss — 1 operation(s) for stripe.
  name: Emboss Stripe API
  phrasing_intents:
  - id: stripe_webhook_stripe_webhook_post
    intent: Receive Stripe billing webhook events
    question: Where should Stripe deliver billing webhook events for this service?
  phrasing_ops: 1
  slug: getemboss-ai-stripe-api
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: The Usage API from Emboss — 1 operation(s) for usage.
  name: Emboss Usage API
  phrasing_intents:
  - id: get_usage_usage_get
    intent: See my account's usage
    question: How much have I used this month on my API key?
  phrasing_ops: 1
  slug: getemboss-ai-usage-api
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: The Users API from Emboss — 7 operation(s) for users.
  name: Emboss Users API
  phrasing_intents:
  - id: signup_users_post
    intent: Sign up for a new account
    question: How do I create an account with email and password?
  - id: verify_users_verify_post
    intent: Verify a new account's email
    question: How do I confirm my email after signing up?
  - id: login_users_login_post
    intent: Log in to the website with a password
    question: How do I sign in to my web account with my password?
  - id: verify_resend_users_verify_resend_post
    intent: Resend the email verification code
    question: I never got my verification email; can it be resent?
  - id: login_with_token_users_login_token_post
    intent: Sign in with a one-time login token
    question: How does clicking the verification link sign me in without a password?
  - id: reset_request_users_reset_request_post
    intent: Request a password reset email
    question: I forgot my password; how do I get a reset link?
  - id: reset_confirm_users_reset_confirm_post
    intent: Set a new password with a reset token
    question: How do I set a new password after getting the reset email?
  phrasing_ops: 7
  slug: getemboss-ai-users-api
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: The Utilities API from Emboss — 1 operation(s) for utilities.
  name: Emboss Utilities API
  phrasing_intents:
  - id: run_utility_utilities__skill__post
    intent: Run a free PDF utility like merge or rotate
    question: Can I merge, split or rotate PDFs I already produced for free?
  phrasing_ops: 1
  slug: getemboss-ai-utilities-api
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: The Webhooks API from Emboss — 1 operation(s) for webhooks.
  name: Emboss Webhooks API
  phrasing_intents:
  - id: fax_webhook_webhooks_fax_post
    intent: Receive fax delivery status callbacks
    question: Where does the fax carrier report delivery status updates?
  phrasing_ops: 1
  slug: getemboss-ai-webhooks-api
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: The .well Known API from Emboss — 3 operation(s) for .well known.
  name: Emboss .well Known API
  phrasing_intents:
  - id: as_metadata__well_known_oauth_authorization_server_get
    intent: Get OAuth authorization server metadata
    question: Where are the OAuth authorization and token endpoints advertised?
  - id: rs_metadata__well_known_oauth_protected_resource_mcp_get
    intent: Get protected resource metadata for the MCP server
    question: Which authorization server protects the MCP endpoint?
  - id: preflight__well_known___rest__options
    intent: Answer CORS preflight for well-known files
    question: Can browser-based clients read the well-known discovery files cross-origin?
  phrasing_ops: 3
  slug: getemboss-ai-well-known-api
artifact_total: 40
asyncapis:
- description: ''
  name: Getemboss Ai Callbacks
  slug: getemboss-ai-callbacks
common:
- group: other
  href: https://artifacts.apis.io/getemboss-ai/capabilities/getemboss-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/getemboss-ai-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/getemboss-ai/skills/getemboss-ai-emboss-SKILL.md
  title: ''
  type: AgentSkill
  url: skills/getemboss-ai-emboss-SKILL.md
- group: agent
  href: https://artifacts.apis.io/getemboss-ai/skills/getemboss-ai-emboss-setup-SKILL.md
  title: ''
  type: AgentSkill
  url: skills/getemboss-ai-emboss-setup-SKILL.md
- group: agent
  href: https://artifacts.apis.io/getemboss-ai/skills/getemboss-ai-emboss-gemini-SKILL.md
  title: ''
  type: AgentSkill
  url: skills/getemboss-ai-emboss-gemini-SKILL.md
- group: agent
  href: https://artifacts.apis.io/getemboss-ai/skills/getemboss-ai-fill-from-data.md
  title: ''
  type: AgentSkill
  url: skills/getemboss-ai-fill-from-data.md
- group: agent
  href: https://artifacts.apis.io/getemboss-ai/skills/getemboss-ai-prepare-commit-fax.md
  title: ''
  type: AgentSkill
  url: skills/getemboss-ai-prepare-commit-fax.md
- group: agent
  href: https://artifacts.apis.io/getemboss-ai/skills/getemboss-ai-pay-per-call-anonymous.md
  title: ''
  type: AgentSkill
  url: skills/getemboss-ai-pay-per-call-anonymous.md
- group: company
  title: ''
  type: Website
  url: https://getemboss.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://getemboss.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://getemboss.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://getemboss.ai/docs/reference/create-form
- group: start
  title: ''
  type: GettingStarted
  url: https://getemboss.ai/docs/quickstart
- group: start
  title: ''
  type: Console
  url: https://api.getemboss.ai/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GetEmboss-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://getemboss.ai/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://api.getemboss.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://getemboss.ai/signup
- group: start
  title: ''
  type: Login
  url: https://getemboss.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getemboss.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getemboss.ai/privacy
- group: other
  title: ''
  type: Glossary
  url: https://getemboss.ai/glossary
- group: agent
  href: https://artifacts.apis.io/getemboss-ai/llms/getemboss-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getemboss-ai-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://getemboss.ai/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://api.getemboss.ai/llms.txt
- group: build
  href: https://artifacts.apis.io/getemboss-ai/packages/getemboss-ai-packages.yml
  title: ''
  type: Packages
  url: packages/getemboss-ai-packages.yml
- group: agent
  href: https://artifacts.apis.io/getemboss-ai/well-known/getemboss-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getemboss-ai-well-known.yml
- group: auth
  href: https://artifacts.apis.io/getemboss-ai/well-known/getemboss-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getemboss-ai-security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: https://getemboss.ai/.well-known/security.txt
- group: other
  title: ''
  type: AICatalog
  url: https://getemboss.ai/.well-known/ard.json
- group: agent
  href: https://artifacts.apis.io/getemboss-ai/mcp/getemboss-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/getemboss-ai-mcp.yml
- group: build
  href: https://artifacts.apis.io/getemboss-ai/mcp/getemboss-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/getemboss-ai-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/getemboss-ai/a2a/getemboss-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/getemboss-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/getemboss-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/getemboss-ai/conformance/getemboss-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getemboss-ai-conformance.yml
- group: auth
  href: https://artifacts.apis.io/getemboss-ai/authentication/getemboss-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getemboss-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/getemboss-ai/scopes/getemboss-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/getemboss-ai-scopes.yml
- group: design
  href: https://artifacts.apis.io/getemboss-ai/conventions/getemboss-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/getemboss-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/getemboss-ai/conventions/getemboss-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/getemboss-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/getemboss-ai/errors/getemboss-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/getemboss-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/getemboss-ai/lifecycle/getemboss-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/getemboss-ai-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/getemboss-ai/changelog/getemboss-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/getemboss-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/getemboss-ai/data-model/getemboss-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/getemboss-ai-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/getemboss-ai/plans/getemboss-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/getemboss-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/getemboss-ai/rate-limits/getemboss-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/getemboss-ai-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/getemboss-ai/sandbox/getemboss-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/getemboss-ai-sandbox.yml
- group: design
  href: https://artifacts.apis.io/getemboss-ai/asyncapi/getemboss-ai-callbacks.yml
  title: ''
  type: Webhooks
  url: asyncapi/getemboss-ai-callbacks.yml
- group: other
  href: https://artifacts.apis.io/getemboss-ai/overlays/getemboss-ai-account-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/getemboss-ai-account-overlay.yaml
- group: other
  href: https://artifacts.apis.io/getemboss-ai/overlays/getemboss-ai-pay-per-call-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/getemboss-ai-pay-per-call-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/getemboss-ai/security/getemboss-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getemboss-ai-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://getemboss.ai/security
- group: auth
  href: https://artifacts.apis.io/getemboss-ai/security/getemboss-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/getemboss-ai-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/getemboss-ai/regulatory/getemboss-ai-regulatory-posture.yml
  title: ''
  type: Regulatory
  url: regulatory/getemboss-ai-regulatory-posture.yml
- group: other
  title: ''
  type: Subprocessors
  url: https://getemboss.ai/subprocessors
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://getemboss.ai/privacy
- group: other
  title: ''
  type: DataResidency
  url: https://getemboss.ai/subprocessors
- group: other
  title: ''
  type: AITransparency
  url: https://getemboss.ai/docs/ephemeral-processing
- group: agent
  href: https://artifacts.apis.io/getemboss-ai/agentic-access/getemboss-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/getemboss-ai-agentic-access.yml
- group: build
  title: ''
  type: Examples
  url: https://getemboss.ai/docs/examples
- group: other
  title: ''
  type: APICatalog
  url: https://getemboss.ai/.well-known/api-catalog
- group: other
  href: https://artifacts.apis.io/getemboss-ai/well-known/getemboss-ai-ucp.json
  title: ''
  type: UCP
  url: well-known/getemboss-ai-ucp.json
- group: other
  title: ''
  type: ContentSignal
  url: https://getemboss.ai/robots.txt
- group: other
  title: ''
  type: AIPREF
  url: https://getemboss.ai/robots.txt
created: '2026-09-19'
description: 'Emboss is a PDF form-filling API for developers and agents. Hand it a flat or scanned PDF and it detects the fields and returns a fillable AcroForm, fills the form from structured values or from supporting documents (proposing every answer with its source, asking about what is missing), verifies the result, reads a filled form back into labelled values, batch-fills one copy per spreadsheet row, packages the filled form with its attachments and a receipt, and faxes the result to any US, Canadian or Mexican fax number. Usage-based pricing in cents with a monthly free allowance and no subscription. The same engine is exposed through four doors on api.getemboss.ai: a 115-operation authenticated REST API (OpenAPI 3.1, Bearer API key or OAuth 2.1 with dynamic client registration), a remote MCP server (20 tools, OAuth-protected, listed in the MCP registry), a signed A2A 1.0 agent card with 23 skills, and an anonymous pay-per-call door priced per job over x402 (USDC on Base) or MPP
  (Tempo stablecoin or card). Every document is deleted 60-70 minutes after the last activity under ephemeral processing.'
finops:
- has_sources: true
  method: derived
  name: Getemboss Ai Finops
  primary_unit: form
  service_category: ''
  slug: getemboss-ai-finops
  template: false
image: https://getemboss.ai/emboss-logo-512.png
layout: provider
mcp_servers:
- description: 'Emboss operates ONE remote MCP server at https://api.getemboss.ai/mcp (Streamable HTTP). It is OAuth 2.1 protected: an anonymous POST tools/list and an anonymous initialize both returned 401 with WWW-'
  name: Emboss MCP Server
  slug: emboss
modified: '2026-10-10'
name: Emboss
nav: Providers
network: true
overview: 'Emboss publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, App API, Artifacts API, and 20 more. Tagged areas include PDF, Forms, Document Processing, Form Filling, and Fax.


  The Emboss catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Emboss'' developer surface includes documentation, API reference, getting-started guide, developer console, pricing, signup flow, authentication, and 55 more developer resources.'
plans:
- name: Getemboss Ai Plans Pricing
  plan_count: 14
  slug: getemboss-ai-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Getemboss Ai Rate Limits
  slug: getemboss-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Emboss API Rules
  rule_count: 63
  severity_counts:
    error: 50
    hint: 0
    info: 2
    warn: 11
  slug: getemboss-ai-rules
scopes:
- name: Getemboss Ai Scopes
  scope_count: 2
  slug: getemboss-ai-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 60.3
  coverage:
    artifact_dirs: 32
    catalog_earned: 67.5
    catalog_earned_first_party: 20.0
    catalog_gap: 47.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.7
  facets:
    access_clarity: 61.8
    contract_governance: 31.8
    contract_quality: 57.5
    developer_ergonomics: 35.7
    discoverability: 90.0
    operational_transparency: 48.7
  previous_composite: 72.0
  provenance:
    agentic_access: first-party
    conformance: first-party
    contracts:
      callable: 17.4
      derived: 0
      marker_coverage: 51.0
      total: 49
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 48.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/getemboss-ai/getemboss-ai-2026-10-11T104856.png
security:
- kind: authentication
  name: Getemboss Ai Authentication
  slug: getemboss-ai-authentication
  summary_line: http/oauth2/payment · 6 schemes
- kind: domain-security
  name: Getemboss Ai Domain Security
  slug: getemboss-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Getemboss Ai Vulnerability Disclosure
  slug: getemboss-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 6
skills:
- name: emboss
  slug: getemboss-ai-emboss-SKILL
- name: emboss
  slug: getemboss-ai-emboss-gemini-SKILL
- name: emboss-setup
  slug: getemboss-ai-emboss-setup-SKILL
- name: getemboss-ai-fill-from-data
  slug: getemboss-ai-fill-from-data
- name: getemboss-ai-pay-per-call-anonymous
  slug: getemboss-ai-pay-per-call-anonymous
- name: getemboss-ai-prepare-commit-fax
  slug: getemboss-ai-prepare-commit-fax
slug: getemboss-ai
tags:
- PDF
- Forms
- Document Processing
- Form Filling
- Fax
- Data Extraction
- Agent-Native
- MCP
- A2A
- x402
- Pay-per-call
- Government Forms
- Company
website: https://getemboss.ai/
---
