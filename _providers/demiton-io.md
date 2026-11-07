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
  - security
  - sandbox
  trial: false
  try_now: true
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: The Demiton API is the platform's REST interface for programmatic access, exposing the same registers, workflow runs and reports visible in the app. It is available on the Baseline tier and authentica
  name: Demiton API
  slug: demiton-io-api
- description: The published, versioned JSON Schema (draft 2020-12) contracts for the 184 registers listed in Civil Memory, each served at https://docs.demiton.io/registers/<register>/v<version>.json and saved verba
  name: Demiton Register Contracts
  slug: demiton-io-register-contracts
- description: Remote Model Context Protocol server that exposes a contractor's operational data and Civil Memory as tools to Claude, ChatGPT and IDE clients. It is available on every tier, and every call needs an a
  name: Ask Demiton MCP Server
  slug: ask-demiton-mcp
artifact_total: 194
common:
- group: build
  href: https://artifacts.apis.io/demiton-io/integrations/demiton-io-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/demiton-io-integration-edges.yml
- group: commercial
  href: https://artifacts.apis.io/demiton-io/plans/demiton-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/demiton-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/demiton-io/conventions/demiton-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/demiton-io-conventions.yml
- group: start
  href: https://artifacts.apis.io/demiton-io/sandbox/demiton-io-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/demiton-io-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/demiton-io/authentication/demiton-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/demiton-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/demiton-io/scopes/demiton-io-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/demiton-io-scopes.yml
- group: operate
  href: https://artifacts.apis.io/demiton-io/lifecycle/demiton-io-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/demiton-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/demiton-io/lifecycle/demiton-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/demiton-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/demiton-io/conformance/demiton-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/demiton-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/demiton-io/llms/demiton-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/demiton-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/demiton-io/mcp/demiton-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/demiton-io-mcp.yml
- group: auth
  href: https://artifacts.apis.io/demiton-io/well-known/demiton-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/demiton-io-security.txt
- group: auth
  href: https://artifacts.apis.io/demiton-io/well-known/demiton-io-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/demiton-io-app-security.txt
- group: agent
  href: https://artifacts.apis.io/demiton-io/well-known/demiton-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/demiton-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/demiton-io/hosts/demiton-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/demiton-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/demiton-io/vendors/demiton-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/demiton-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/demiton-io/security/demiton-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/demiton-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/demiton-io/security/demiton-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/demiton-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://demiton.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.demiton.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.demiton.io/access/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.demiton.io/start-here/quickstart/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.demiton.io/changelog/
- group: company
  title: ''
  type: Blog
  url: https://demiton.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://demiton.io/en-au/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/demitonapp
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://demiton.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://demiton.io/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://demiton.io/security
- group: operate
  title: ''
  type: StatusPage
  url: https://status.demiton.io/
- group: operate
  title: ''
  type: Support
  url: https://demiton.io/contact
- group: start
  title: ''
  type: Login
  url: https://app.demiton.io/auth/login
- group: start
  title: ''
  type: SignUp
  url: https://app.demiton.io/auth/register
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.demiton.io/llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/demiton
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@DemitonApp
- group: other
  title: ''
  type: X
  url: https://x.com/DemitonApp
created: '2026-11-05'
description: Demiton (Demiton Pty Ltd, ABN 40 687 279 330, Australia) is a margin-protection platform for civil contractors. It fills project registers from the systems a contractor already runs, in published, versioned JSON Schema register contracts, and catches the five 'diseases' of a civil job's margin - rework, baseline overrun, forfeited entitlements, disputes and non-compliance. Its Civil Memory record spans the public market (OCDS/OC4IDS) through award into delivery, and is queryable from Claude or ChatGPT over the Model Context Protocol (Ask Demiton), alongside Studio, Market, Memory and Agents surfaces and an API access offering.
image: https://demiton.io/logos/vector/demiton-knot-navy.svg
json_schemas:
- name: allocation contract v1
  property_count: 14
  slug: demiton-io-allocation-v1
- name: asbestos_register contract v1
  property_count: 17
  slug: demiton-io-asbestos_register-v1
- name: asset_disposal contract v3
  property_count: 13
  slug: demiton-io-asset_disposal-v3
- name: asset_meter_reading contract v1
  property_count: 11
  slug: demiton-io-asset_meter_reading-v1
- name: asset_utilisation contract v1
  property_count: 18
  slug: demiton-io-asset_utilisation-v1
- name: attendance_record contract v1
  property_count: 12
  slug: demiton-io-attendance_record-v1
- name: bank_accounts contract v3
  property_count: 8
  slug: demiton-io-bank_accounts-v3
- name: bank_guarantee contract v2
  property_count: 18
  slug: demiton-io-bank_guarantee-v2
- name: bid_no_bid_verdict contract v2
  property_count: 21
  slug: demiton-io-bid_no_bid_verdict-v2
- name: budget_vs_actual contract v2
  property_count: 9
  slug: demiton-io-budget_vs_actual-v2
- name: cash_position contract v2
  property_count: 7
  slug: demiton-io-cash_position-v2
- name: certification_register contract v1
  property_count: 18
  slug: demiton-io-certification_register-v1
- name: change_event contract v2
  property_count: 20
  slug: demiton-io-change_event-v2
- name: chart_of_accounts contract v1
  property_count: 8
  slug: demiton-io-chart_of_accounts-v1
- name: claim_line_observation contract v1
  property_count: 0
  slug: demiton-io-claim_line_observation-v1
- name: claim_window_verdict contract v2
  property_count: 15
  slug: demiton-io-claim_window_verdict-v2
- name: competency_verification contract v1
  property_count: 9
  slug: demiton-io-competency_verification-v1
- name: compliance_certifications contract v2
  property_count: 15
  slug: demiton-io-compliance_certifications-v2
- name: compliance_documents contract v1
  property_count: 13
  slug: demiton-io-compliance_documents-v1
- name: compliance_evidence contract v2
  property_count: 30
  slug: demiton-io-compliance_evidence-v2
- name: compliance_gate_verdict contract v1
  property_count: 8
  slug: demiton-io-compliance_gate_verdict-v1
- name: compliance_prequal contract v1
  property_count: 9
  slug: demiton-io-compliance_prequal-v1
- name: compliance_state contract v1
  property_count: 27
  slug: demiton-io-compliance_state-v1
- name: construction_methodology contract v1
  property_count: 8
  slug: demiton-io-construction_methodology-v1
- name: contract_award_match contract v1
  property_count: 0
  slug: demiton-io-contract_award_match-v1
- name: contract_link contract v1
  property_count: 12
  slug: demiton-io-contract_link-v1
- name: contract_notice contract v1
  property_count: 16
  slug: demiton-io-contract_notice-v1
- name: contract_penalty contract v1
  property_count: 10
  slug: demiton-io-contract_penalty-v1
- name: contract_terms contract v2
  property_count: 40
  slug: demiton-io-contract_terms-v2
- name: cost_element contract v2
  property_count: 17
  slug: demiton-io-cost_element-v2
- name: credit_note contract v3
  property_count: 19
  slug: demiton-io-credit_note-v3
- name: customer_list contract v3
  property_count: 26
  slug: demiton-io-customer_list-v3
- name: daily_log contract v1
  property_count: 14
  slug: demiton-io-daily_log-v1
- name: day_works_docket contract v2
  property_count: 25
  slug: demiton-io-day_works_docket-v2
- name: diary_compliance_assessment contract v1
  property_count: 0
  slug: demiton-io-diary_compliance_assessment-v1
- name: diary_photo_observation contract v1
  property_count: 15
  slug: demiton-io-diary_photo_observation-v1
- name: dimension_set_entry contract v1
  property_count: 7
  slug: demiton-io-dimension_set_entry-v1
- name: document_filing_convention contract v1
  property_count: 8
  slug: demiton-io-document_filing_convention-v1
- name: document_list contract v1
  property_count: 0
  slug: demiton-io-document_list-v1
- name: document_location contract v1
  property_count: 16
  slug: demiton-io-document_location-v1
- name: document_transmittal contract v1
  property_count: 20
  slug: demiton-io-document_transmittal-v1
- name: drawing_register contract v1
  property_count: 19
  slug: demiton-io-drawing_register-v1
- name: driving_behaviour_event contract v1
  property_count: 13
  slug: demiton-io-driving_behaviour_event-v1
- name: dropbox_document_routing contract v1
  property_count: 14
  slug: demiton-io-dropbox_document_routing-v1
- name: email_issue contract v1
  property_count: 16
  slug: demiton-io-email_issue-v1
- name: employee_contact_detail contract v1
  property_count: 12
  slug: demiton-io-employee_contact_detail-v1
- name: employee_hr_records contract v1
  property_count: 26
  slug: demiton-io-employee_hr_records-v1
- name: employee_list contract v1
  property_count: 20
  slug: demiton-io-employee_list-v1
- name: entity_attribute contract v1
  property_count: 10
  slug: demiton-io-entity_attribute-v1
- name: entity_link_origin contract v2
  property_count: 13
  slug: demiton-io-entity_link_origin-v2
- name: environmental_aspect contract v1
  property_count: 10
  slug: demiton-io-environmental_aspect-v1
- name: environmental_observation contract v1
  property_count: 18
  slug: demiton-io-environmental_observation-v1
- name: equipment_assignment contract v1
  property_count: 8
  slug: demiton-io-equipment_assignment-v1
- name: equipment_list contract v1
  property_count: 22
  slug: demiton-io-equipment_list-v1
- name: equipment_transfer contract v1
  property_count: 11
  slug: demiton-io-equipment_transfer-v1
- name: estimating_email contract v1
  property_count: 20
  slug: demiton-io-estimating_email-v1
- name: evidence_gap_verdict contract v2
  property_count: 13
  slug: demiton-io-evidence_gap_verdict-v2
- name: expense_claims contract v2
  property_count: 11
  slug: demiton-io-expense_claims-v2
- name: extraction_procedure contract v1
  property_count: 7
  slug: demiton-io-extraction_procedure-v1
- name: financial_period_list contract v1
  property_count: 10
  slug: demiton-io-financial_period_list-v1
- name: fixed_asset_list contract v2
  property_count: 16
  slug: demiton-io-fixed_asset_list-v2
- name: fuel_transaction contract v2
  property_count: 16
  slug: demiton-io-fuel_transaction-v2
- name: gl_journal_entry contract v2
  property_count: 12
  slug: demiton-io-gl_journal_entry-v2
- name: gps_event contract v1
  property_count: 13
  slug: demiton-io-gps_event-v1
- name: group_members contract v1
  property_count: 9
  slug: demiton-io-group_members-v1
- name: health_screening contract v1
  property_count: 12
  slug: demiton-io-health_screening-v1
- name: hilti_location contract v1
  property_count: 9
  slug: demiton-io-hilti_location-v1
- name: implementation_request contract v2
  property_count: 8
  slug: demiton-io-implementation_request-v2
- name: induction_onboarding contract v1
  property_count: 14
  slug: demiton-io-induction_onboarding-v1
- name: inspection_test_result contract v1
  property_count: 30
  slug: demiton-io-inspection_test_result-v1
- name: insurance_certificate contract v2
  property_count: 10
  slug: demiton-io-insurance_certificate-v2
- name: intercompany_transaction contract v2
  property_count: 17
  slug: demiton-io-intercompany_transaction-v2
- name: invoice_issued contract v3
  property_count: 25
  slug: demiton-io-invoice_issued-v3
- name: item_master contract v1
  property_count: 16
  slug: demiton-io-item_master-v1
- name: job_budget contract v2
  property_count: 7
  slug: demiton-io-job_budget-v2
- name: job_progress contract v1
  property_count: 10
  slug: demiton-io-job_progress-v1
- name: leave_balance contract v1
  property_count: 9
  slug: demiton-io-leave_balance-v1
- name: leave_category_list contract v1
  property_count: 32
  slug: demiton-io-leave_category_list-v1
- name: leave_request contract v1
  property_count: 14
  slug: demiton-io-leave_request-v1
- name: legal_entities contract v2
  property_count: 19
  slug: demiton-io-legal_entities-v2
- name: maintenance_record contract v2
  property_count: 24
  slug: demiton-io-maintenance_record-v2
- name: margin_driver_contribution contract v1
  property_count: 13
  slug: demiton-io-margin_driver_contribution-v1
- name: margin_watch_learning contract v1
  property_count: 12
  slug: demiton-io-margin_watch_learning-v1
- name: market_intelligence contract v2
  property_count: 17
  slug: demiton-io-market_intelligence-v2
- name: market_opportunity_fit_score contract v1
  property_count: 0
  slug: demiton-io-market_opportunity_fit_score-v1
- name: memory_recall contract v1
  property_count: 14
  slug: demiton-io-memory_recall-v1
- name: opportunities contract v2
  property_count: 19
  slug: demiton-io-opportunities-v2
- name: opportunity contract v2
  property_count: 17
  slug: demiton-io-opportunity-v2
- name: opportunity_specifications contract v1
  property_count: 9
  slug: demiton-io-opportunity_specifications-v1
- name: opportunity_win_probability contract v2
  property_count: 14
  slug: demiton-io-opportunity_win_probability-v2
- name: overrun_risk_verdict contract v2
  property_count: 11
  slug: demiton-io-overrun_risk_verdict-v2
- name: overstaffing_verdict contract v1
  property_count: 12
  slug: demiton-io-overstaffing_verdict-v1
- name: pay_categories contract v1
  property_count: 23
  slug: demiton-io-pay_categories-v1
- name: payable_entry contract v2
  property_count: 17
  slug: demiton-io-payable_entry-v2
- name: payment_schedule contract v2
  property_count: 13
  slug: demiton-io-payment_schedule-v2
- name: payroll_run contract v2
  property_count: 15
  slug: demiton-io-payroll_run-v2
- name: permit_to_work contract v1
  property_count: 20
  slug: demiton-io-permit_to_work-v1
- name: plant_charge_rate contract v1
  property_count: 8
  slug: demiton-io-plant_charge_rate-v1
- name: plant_fuel_usage contract v2
  property_count: 19
  slug: demiton-io-plant_fuel_usage-v2
- name: plant_prestart contract v2
  property_count: 19
  slug: demiton-io-plant_prestart-v2
- name: plant_registration contract v2
  property_count: 14
  slug: demiton-io-plant_registration-v2
- name: plant_risk_assessment contract v1
  property_count: 20
  slug: demiton-io-plant_risk_assessment-v1
- name: plant_snapshot contract v1
  property_count: 6
  slug: demiton-io-plant_snapshot-v1
- name: platform_award contract v3
  property_count: 23
  slug: demiton-io-platform_award-v3
- name: platform_contractor_stats contract v2
  property_count: 21
  slug: demiton-io-platform_contractor_stats-v2
- name: platform_entity_attr contract v2
  property_count: 12
  slug: demiton-io-platform_entity_attr-v2
- name: platform_evidence_standard contract v1
  property_count: 20
  slug: demiton-io-platform_evidence_standard-v1
- name: platform_obligation contract v1
  property_count: 42
  slug: demiton-io-platform_obligation-v1
- name: platform_planning contract v3
  property_count: 30
  slug: demiton-io-platform_planning-v3
- name: platform_prequal contract v2
  property_count: 10
  slug: demiton-io-platform_prequal-v2
- name: platform_rate contract v2
  property_count: 11
  slug: demiton-io-platform_rate-v2
- name: platform_research_finding contract v3
  property_count: 21
  slug: demiton-io-platform_research_finding-v3
- name: platform_tender contract v3
  property_count: 23
  slug: demiton-io-platform_tender-v3
- name: platform_weather contract v2
  property_count: 15
  slug: demiton-io-platform_weather-v2
- name: policy_acknowledgements contract v1
  property_count: 12
  slug: demiton-io-policy_acknowledgements-v1
- name: portal_document contract v2
  property_count: 12
  slug: demiton-io-portal_document-v2
- name: prequalification_answer contract v1
  property_count: 18
  slug: demiton-io-prequalification_answer-v1
- name: price_adjustment_verdict contract v1
  property_count: 21
  slug: demiton-io-price_adjustment_verdict-v1
- name: profit_and_loss contract v3
  property_count: 13
  slug: demiton-io-profit_and_loss-v3
- name: programme contract v1
  property_count: 9
  slug: demiton-io-programme-v1
- name: progress_claim contract v2
  property_count: 14
  slug: demiton-io-progress_claim-v2
- name: project_details contract v2
  property_count: 11
  slug: demiton-io-project_details-v2
- name: project_list contract v2
  property_count: 17
  slug: demiton-io-project_list-v2
- name: project_milestone contract v1
  property_count: 7
  slug: demiton-io-project_milestone-v1
- name: project_obligation contract v1
  property_count: 5
  slug: demiton-io-project_obligation-v1
- name: project_outcome contract v2
  property_count: 11
  slug: demiton-io-project_outcome-v2
- name: project_performance_record contract v2
  property_count: 20
  slug: demiton-io-project_performance_record-v2
- name: protection contract v1
  property_count: 8
  slug: demiton-io-protection-v1
- name: punch_list contract v1
  property_count: 20
  slug: demiton-io-punch_list-v1
- name: purchase_line contract v2
  property_count: 23
  slug: demiton-io-purchase_line-v2
- name: purchase_order contract v2
  property_count: 15
  slug: demiton-io-purchase_order-v2
- name: rate_card_verdict contract v1
  property_count: 24
  slug: demiton-io-rate_card_verdict-v1
- name: receivable_entry contract v2
  property_count: 14
  slug: demiton-io-receivable_entry-v2
- name: retention_position contract v2
  property_count: 8
  slug: demiton-io-retention_position-v2
- name: rework_risk_verdict contract v2
  property_count: 16
  slug: demiton-io-rework_risk_verdict-v2
- name: rfi contract v1
  property_count: 17
  slug: demiton-io-rfi-v1
- name: safety_incident contract v2
  property_count: 15
  slug: demiton-io-safety_incident-v2
- name: safety_ncr contract v2
  property_count: 13
  slug: demiton-io-safety_ncr-v2
- name: self_reported_disease contract v1
  property_count: 11
  slug: demiton-io-self_reported_disease-v1
- name: site_activity contract v1
  property_count: 9
  slug: demiton-io-site_activity-v1
- name: site_bore_reference contract v2
  property_count: 18
  slug: demiton-io-site_bore_reference-v2
- name: site_diary contract v1
  property_count: 22
  slug: demiton-io-site_diary-v1
- name: site_geology contract v1
  property_count: 15
  slug: demiton-io-site_geology-v1
- name: site_inspection contract v1
  property_count: 14
  slug: demiton-io-site_inspection-v1
- name: site_requisitions contract v1
  property_count: 15
  slug: demiton-io-site_requisitions-v1
- name: sor_outturn_comparison contract v1
  property_count: 0
  slug: demiton-io-sor_outturn_comparison-v1
- name: sor_verification contract v1
  property_count: 9
  slug: demiton-io-sor_verification-v1
- name: sor_verification_tendered contract v1
  property_count: 13
  slug: demiton-io-sor_verification_tendered-v1
- name: speeding_event contract v1
  property_count: 18
  slug: demiton-io-speeding_event-v1
- name: subcontract contract v2
  property_count: 21
  slug: demiton-io-subcontract-v2
- name: subcontractor_list contract v1
  property_count: 17
  slug: demiton-io-subcontractor_list-v1
- name: superannuation_fund contract v1
  property_count: 11
  slug: demiton-io-superannuation_fund-v1
- name: survey_control contract v1
  property_count: 23
  slug: demiton-io-survey_control-v1
- name: tender_activity_map contract v1
  property_count: 7
  slug: demiton-io-tender_activity_map-v1
- name: tender_baseline contract v1
  property_count: 0
  slug: demiton-io-tender_baseline-v1
- name: tender_baseline_active contract v1
  property_count: 5
  slug: demiton-io-tender_baseline_active-v1
- name: tender_brief contract v2
  property_count: 10
  slug: demiton-io-tender_brief-v2
- name: tender_column_mapping contract v1
  property_count: 0
  slug: demiton-io-tender_column_mapping-v1
- name: tender_incoming contract v2
  property_count: 22
  slug: demiton-io-tender_incoming-v2
- name: tender_input contract v1
  property_count: 13
  slug: demiton-io-tender_input-v1
- name: tender_lesson contract v1
  property_count: 20
  slug: demiton-io-tender_lesson-v1
- name: tender_outcome contract v1
  property_count: 0
  slug: demiton-io-tender_outcome-v1
- name: tender_post_mortem contract v1
  property_count: 0
  slug: demiton-io-tender_post_mortem-v1
- name: tender_pricing_verdict contract v1
  property_count: 25
  slug: demiton-io-tender_pricing_verdict-v1
- name: tender_register_upload contract v1
  property_count: 0
  slug: demiton-io-tender_register_upload-v1
- name: tender_source_link contract v1
  property_count: 0
  slug: demiton-io-tender_source_link-v1
- name: tender_submission contract v2
  property_count: 10
  slug: demiton-io-tender_submission-v2
- name: tendered_budget contract v2
  property_count: 14
  slug: demiton-io-tendered_budget-v2
- name: tendered_rate_observation contract v1
  property_count: 15
  slug: demiton-io-tendered_rate_observation-v1
- name: timesheet_code_list contract v1
  property_count: 9
  slug: demiton-io-timesheet_code_list-v1
- name: timesheet_entry contract v1
  property_count: 11
  slug: demiton-io-timesheet_entry-v1
- name: toolbox_talk contract v1
  property_count: 19
  slug: demiton-io-toolbox_talk-v1
- name: traffic_management_plan contract v2
  property_count: 22
  slug: demiton-io-traffic_management_plan-v2
- name: training_records contract v1
  property_count: 14
  slug: demiton-io-training_records-v1
- name: trial_balance contract v2
  property_count: 12
  slug: demiton-io-trial_balance-v2
- name: user_list contract v1
  property_count: 12
  slug: demiton-io-user_list-v1
- name: utility_location contract v1
  property_count: 15
  slug: demiton-io-utility_location-v1
- name: variations contract v1
  property_count: 28
  slug: demiton-io-variations-v1
- name: vehicle_list contract v2
  property_count: 12
  slug: demiton-io-vehicle_list-v2
- name: vehicle_location contract v1
  property_count: 16
  slug: demiton-io-vehicle_location-v1
- name: vendor_list contract v3
  property_count: 23
  slug: demiton-io-vendor_list-v3
- name: work_activity_categories contract v1
  property_count: 6
  slug: demiton-io-work_activity_categories-v1
- name: worker_qualification contract v1
  property_count: 11
  slug: demiton-io-worker_qualification-v1
- name: worker_training_session contract v1
  property_count: 6
  slug: demiton-io-worker_training_session-v1
layout: provider
mcp_servers:
- description: Remote MCP server at api.demiton.io over streamable HTTP requiring OAuth; 5 tools listed.
  name: Ask Demiton MCP Server
  slug: io-demiton-demiton
modified: '2026-11-05'
name: Demiton
nav: Providers
network: true
overview: 'Demiton is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Civil Engineering, Project Management, and Compliance.


  Demiton''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, changelog, engineering blog, and 30 more developer resources.'
plans:
- name: Demiton Io Plans Pricing
  plan_count: 5
  slug: demiton-io-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Demiton Io Rate Limits
  slug: demiton-io-rate-limits
scopes:
- name: Demiton Io Scopes
  scope_count: 3
  slug: demiton-io-scopes
  summary_line: 3 scopes
score:
  band: developing
  composite: 47.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 52.4
    catalog_earned_first_party: 12.0
    catalog_gap: 62.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 7.2
    developer_ergonomics: 54.8
    discoverability: 68.3
    operational_transparency: 55.3
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 37.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Demiton Io Authentication
  slug: demiton-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Demiton Io Domain Security
  slug: demiton-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Demiton Io Vulnerability Disclosure
  slug: demiton-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: demiton-io
tags:
- Company
- Construction
- Civil Engineering
- Project Management
- Compliance
- MCP
- Artificial Intelligence
- Open Contracting
website: https://demiton.io/
---
