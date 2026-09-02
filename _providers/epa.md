---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 148
  human_in_the_loop: 1
  name: Epa Agentic Access
  operation_count: 611
  slug: epa-agentic-access
  summary_line: 611 operations · 148 acting · 1 human-in-the-loop
api_count: 22
apis:
- description: Master inventory of EPA-regulated facilities cross-walked across air, water, waste, and drinking-water programs. Production query and submit endpoints require a NAAS account.
  name: EPA Facility Registry Service (FRS) API
  slug: epa-facility-registry-service-frs-api
- description: Toxic chemical release and transfer reporting (Form R / Form A) covering ~770 listed chemicals at TRI-covered facilities. Exposed primarily via the Envirofacts data service over the `tri.*` tables.
  name: EPA TRI (Toxics Release Inventory) Web Service
  slug: epa-tri-toxics-release-inventory-web-service
- description: Assessment, Total Maximum Daily Load Tracking and Implementation System — REST/JSON services for state water quality assessments, impaired waters, TMDLs, and actions.
  name: EPA ATTAINS Web Services
  slug: epa-attains-web-services
- description: Geospatial water program services including StreamCat, NHDPlus, and ATTAINS overlays.
  name: EPA WATERS — Watershed Assessment, Tracking & Environmental Results
  slug: epa-waters-watershed-assessment-tracking-environmental-results
- description: Internal-with-key access to NGGS grant programs — applications, obligations, place of performance, and funding opportunities. GraphQL plus REST format dispatchers (JSON/XML/CSV/Excel/PDF/HTML).
  name: EPA Grants API
  slug: epa-grants-api
- description: Searchable inventory of EPA-registered insect repellent products with active ingredient, target pest, and duration data.
  name: EPA Insect Repellents API
  slug: epa-insect-repellents-api
- description: Electronic hazardous waste manifest tracking system with REST APIs for manifest creation, retrieval, search, and lifecycle management. Production access via NAAS/CDX.
  name: EPA e-Manifest Hazardous Waste Tracking
  slug: epa-e-manifest-hazardous-waste-tracking
- description: Authoritative registries of substances, regulatory programs, terminology, and crosswalks used across EPA systems.
  name: EPA System of Registries (SoR)
  slug: epa-system-of-registries-sor
- description: Chemical, hazard, bioactivity, and exposure data covering tens of thousands of chemicals. Includes Chemical, Bioactivity, Hazard, Exposure, and ToxRefDB endpoints.
  name: CTX — Center for Computational Toxicology and Exposure APIs
  slug: ctx-center-for-computational-toxicology-and-exposure-apis
- description: The Account Type Codes API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for account type codes.
  name: EPA — U.S. Environmental Protection Agency Account Type Codes API
  slug: epa-account-type-codes-api
- description: The Accounts API from EPA — U.S. Environmental Protection Agency — 5 operation(s) for accounts.
  name: EPA — U.S. Environmental Protection Agency Accounts API
  slug: epa-accounts-api
- description: The Air Emission Testing API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for air emission testing.
  name: EPA — U.S. Environmental Protection Agency Air Emission Testing API
  slug: epa-air-emission-testing-api
- description: The Allowance Compliance API from EPA — U.S. Environmental Protection Agency — 4 operation(s) for allowance compliance.
  name: EPA — U.S. Environmental Protection Agency Allowance Compliance API
  slug: epa-allowance-compliance-api
- description: The Allowance Holdings API from EPA — U.S. Environmental Protection Agency — 4 operation(s) for allowance holdings.
  name: EPA — U.S. Environmental Protection Agency Allowance Holdings API
  slug: epa-allowance-holdings-api
- description: The Allowance Transactions API from EPA — U.S. Environmental Protection Agency — 4 operation(s) for allowance transactions.
  name: EPA — U.S. Environmental Protection Agency Allowance Transactions API
  slug: epa-allowance-transactions-api
- description: The Analysis Services API from EPA — U.S. Environmental Protection Agency — 5 operation(s) for analysis services.
  name: EPA — U.S. Environmental Protection Agency Analysis Services API
  slug: epa-analysis-services-api
- description: The Analyzer Ranges API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for analyzer ranges.
  name: EPA — U.S. Environmental Protection Agency Analyzer Ranges API
  slug: epa-analyzer-ranges-api
- description: Annual aggregated values.
  name: EPA — U.S. Environmental Protection Agency Annual Data API
  slug: epa-annual-data-api
- description: The Appendix E Correlation Test Run API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for appendix e correlation test run.
  name: EPA — U.S. Environmental Protection Agency Appendix E Correlation Test Run API
  slug: epa-appendix-e-correlation-test-run-api
- description: The Appendix E Correlation Test Summary API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for appendix e correlation test summary.
  name: EPA — U.S. Environmental Protection Agency Appendix E Correlation Test Summary API
  slug: epa-appendix-e-correlation-test-summary-api
- description: The Appendix E Heat Input From Gas API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for appendix e heat input from gas.
  name: EPA — U.S. Environmental Protection Agency Appendix E Heat Input From Gas API
  slug: epa-appendix-e-heat-input-from-gas-api
- description: The Appendix E Heat Input From Oil API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for appendix e heat input from oil.
  name: EPA — U.S. Environmental Protection Agency Appendix E Heat Input From Oil API
  slug: epa-appendix-e-heat-input-from-oil-api
- description: The Apportioned Annual Emissions API from EPA — U.S. Environmental Protection Agency — 8 operation(s) for apportioned annual emissions.
  name: EPA — U.S. Environmental Protection Agency Apportioned Annual Emissions API
  slug: epa-apportioned-annual-emissions-api
- description: The Apportioned Daily Emissions API from EPA — U.S. Environmental Protection Agency — 8 operation(s) for apportioned daily emissions.
  name: EPA — U.S. Environmental Protection Agency Apportioned Daily Emissions API
  slug: epa-apportioned-daily-emissions-api
- description: The Apportioned Emissions API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for apportioned emissions.
  name: EPA — U.S. Environmental Protection Agency Apportioned Emissions API
  slug: epa-apportioned-emissions-api
- description: The Apportioned Hourly Emissions API from EPA — U.S. Environmental Protection Agency — 8 operation(s) for apportioned hourly emissions.
  name: EPA — U.S. Environmental Protection Agency Apportioned Hourly Emissions API
  slug: epa-apportioned-hourly-emissions-api
- description: The Apportioned Hourly MATS Emissions API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for apportioned hourly mats emissions.
  name: EPA — U.S. Environmental Protection Agency Apportioned Hourly MATS Emissions API
  slug: epa-apportioned-hourly-mats-emissions-api
- description: The Apportioned MATS Emissions API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for apportioned mats emissions.
  name: EPA — U.S. Environmental Protection Agency Apportioned MATS Emissions API
  slug: epa-apportioned-mats-emissions-api
- description: The Apportioned Monthly Emissions API from EPA — U.S. Environmental Protection Agency — 8 operation(s) for apportioned monthly emissions.
  name: EPA — U.S. Environmental Protection Agency Apportioned Monthly Emissions API
  slug: epa-apportioned-monthly-emissions-api
- description: The Apportioned Ozone Emissions API from EPA — U.S. Environmental Protection Agency — 8 operation(s) for apportioned ozone emissions.
  name: EPA — U.S. Environmental Protection Agency Apportioned Ozone Emissions API
  slug: epa-apportioned-ozone-emissions-api
- description: The Apportioned Quarterly Emissions API from EPA — U.S. Environmental Protection Agency — 9 operation(s) for apportioned quarterly emissions.
  name: EPA — U.S. Environmental Protection Agency Apportioned Quarterly Emissions API
  slug: epa-apportioned-quarterly-emissions-api
- description: The Attributes API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for attributes.
  name: EPA — U.S. Environmental Protection Agency Attributes API
  slug: epa-attributes-api
- description: The Bap API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for bap.
  name: EPA — U.S. Environmental Protection Agency Bap API
  slug: epa-bap-api
- description: The Bulk Files API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for bulk files.
  name: EPA — U.S. Environmental Protection Agency Bulk Files API
  slug: epa-bulk-files-api
- description: The Calibration Injection API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for calibration injection.
  name: EPA — U.S. Environmental Protection Agency Calibration Injection API
  slug: epa-calibration-injection-api
- description: The Case Enforcement API from EPA — U.S. Environmental Protection Agency — 9 operation(s) for case enforcement.
  name: EPA — U.S. Environmental Protection Agency Case Enforcement API
  slug: epa-case-enforcement-api
- description: The CIP Indexing Services API from EPA — U.S. Environmental Protection Agency — 3 operation(s) for cip indexing services.
  name: EPA — U.S. Environmental Protection Agency CIP Indexing Services API
  slug: epa-cip-indexing-services-api
- description: The Codes & Descriptions API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for codes & descriptions.
  name: EPA — U.S. Environmental Protection Agency Codes & Descriptions API
  slug: epa-codes-descriptions-api
- description: The Comments API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for comments.
  name: EPA — U.S. Environmental Protection Agency Comments API
  slug: epa-comments-api
- description: The Components API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for components.
  name: EPA — U.S. Environmental Protection Agency Components API
  slug: epa-components-api
- description: The Config API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for config.
  name: EPA — U.S. Environmental Protection Agency Config API
  slug: epa-config-api
- description: The Configurations API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for configurations.
  name: EPA — U.S. Environmental Protection Agency Configurations API
  slug: epa-configurations-api
- description: The Contact API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for contact.
  name: EPA — U.S. Environmental Protection Agency Contact API
  slug: epa-contact-api
- description: The Control Codes API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for control codes.
  name: EPA — U.S. Environmental Protection Agency Control Codes API
  slug: epa-control-codes-api
- description: The Custom Search API from EPA — U.S. Environmental Protection Agency — 3 operation(s) for custom search.
  name: EPA — U.S. Environmental Protection Agency Custom Search API
  slug: epa-custom-search-api
- description: The Cycle Time Injection API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for cycle time injection.
  name: EPA — U.S. Environmental Protection Agency Cycle Time Injection API
  slug: epa-cycle-time-injection-api
- description: The Cycle Time Summary API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for cycle time summary.
  name: EPA — U.S. Environmental Protection Agency Cycle Time Summary API
  slug: epa-cycle-time-summary-api
- description: Daily aggregated values.
  name: EPA — U.S. Environmental Protection Agency Daily Data API
  slug: epa-daily-data-api
- description: Generic Envirofacts REST data service supporting any program.table.
  name: EPA — U.S. Environmental Protection Agency Data Service API
  slug: epa-data-service-api
- description: The Defaults API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for defaults.
  name: EPA — U.S. Environmental Protection Agency Defaults API
  slug: epa-defaults-api
- description: The Detailed Facility Report API from EPA — U.S. Environmental Protection Agency — 47 operation(s) for detailed facility report.
  name: EPA — U.S. Environmental Protection Agency Detailed Facility Report API
  slug: epa-detailed-facility-report-api
- description: The Effluent Charts API from EPA — U.S. Environmental Protection Agency — 3 operation(s) for effluent charts.
  name: EPA — U.S. Environmental Protection Agency Effluent Charts API
  slug: epa-effluent-charts-api
- description: The Emissions API from EPA — U.S. Environmental Protection Agency — 7 operation(s) for emissions.
  name: EPA — U.S. Environmental Protection Agency Emissions API
  slug: epa-emissions-api
- description: The Emissions Compliance API from EPA — U.S. Environmental Protection Agency — 4 operation(s) for emissions compliance.
  name: EPA — U.S. Environmental Protection Agency Emissions Compliance API
  slug: epa-emissions-compliance-api
- description: The Emissions Views API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for emissions views.
  name: EPA — U.S. Environmental Protection Agency Emissions Views API
  slug: epa-emissions-views-api
- description: The Facilities API from EPA — U.S. Environmental Protection Agency — 12 operation(s) for facilities.
  name: EPA — U.S. Environmental Protection Agency Facilities API
  slug: epa-facilities-api
- description: The Facility Info API from EPA — U.S. Environmental Protection Agency — 7 operation(s) for facility info.
  name: EPA — U.S. Environmental Protection Agency Facility Info API
  slug: epa-facility-info-api
- description: The Facility Information API from EPA — U.S. Environmental Protection Agency — 7 operation(s) for facility information.
  name: EPA — U.S. Environmental Protection Agency Facility Information API
  slug: epa-facility-information-api
- description: The Flow Rata Run API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for flow rata run.
  name: EPA — U.S. Environmental Protection Agency Flow Rata Run API
  slug: epa-flow-rata-run-api
- description: The Flow To Load Check API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for flow to load check.
  name: EPA — U.S. Environmental Protection Agency Flow To Load Check API
  slug: epa-flow-to-load-check-api
- description: The Flow To Load Reference API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for flow to load reference.
  name: EPA — U.S. Environmental Protection Agency Flow To Load Reference API
  slug: epa-flow-to-load-reference-api
- description: The Formio API from EPA — U.S. Environmental Protection Agency — 43 operation(s) for formio.
  name: EPA — U.S. Environmental Protection Agency Formio API
  slug: epa-formio-api
- description: The Formulas API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for formulas.
  name: EPA — U.S. Environmental Protection Agency Formulas API
  slug: epa-formulas-api
- description: The Fuel Flow To Load Baseline API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for fuel flow to load baseline.
  name: EPA — U.S. Environmental Protection Agency Fuel Flow To Load Baseline API
  slug: epa-fuel-flow-to-load-baseline-api
- description: The Fuel Flow To Load Test API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for fuel flow to load test.
  name: EPA — U.S. Environmental Protection Agency Fuel Flow To Load Test API
  slug: epa-fuel-flow-to-load-test-api
- description: The Fuel Flowmeter Accuracy API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for fuel flowmeter accuracy.
  name: EPA — U.S. Environmental Protection Agency Fuel Flowmeter Accuracy API
  slug: epa-fuel-flowmeter-accuracy-api
- description: The Fuel Type Codes API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for fuel type codes.
  name: EPA — U.S. Environmental Protection Agency Fuel Type Codes API
  slug: epa-fuel-type-codes-api
- description: The Glossary API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for glossary.
  name: EPA — U.S. Environmental Protection Agency Glossary API
  slug: epa-glossary-api
- description: GraphQL endpoint for complex queries beyond REST capabilities.
  name: EPA — U.S. Environmental Protection Agency GraphQL API
  slug: epa-graphql-api
- description: The Health API from EPA — U.S. Environmental Protection Agency — 8 operation(s) for health.
  name: EPA — U.S. Environmental Protection Agency Health API
  slug: epa-health-api
- description: The Help API from EPA — U.S. Environmental Protection Agency — 5 operation(s) for help.
  name: EPA — U.S. Environmental Protection Agency Help API
  slug: epa-help-api
- description: The Hg Injection API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for hg injection.
  name: EPA — U.S. Environmental Protection Agency Hg Injection API
  slug: epa-hg-injection-api
- description: The Hg Summary API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for hg summary.
  name: EPA — U.S. Environmental Protection Agency Hg Summary API
  slug: epa-hg-summary-api
- description: The How's My Waterway API from EPA — U.S. Environmental Protection Agency — 3 operation(s) for how's my waterway.
  name: EPA — U.S. Environmental Protection Agency How's My Waterway API
  slug: epa-how-s-my-waterway-api
- description: The LEE Qualifications API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for lee qualifications.
  name: EPA — U.S. Environmental Protection Agency LEE Qualifications API
  slug: epa-lee-qualifications-api
- description: The Linearity Injection API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for linearity injection.
  name: EPA — U.S. Environmental Protection Agency Linearity Injection API
  slug: epa-linearity-injection-api
- description: The Linearity Summary API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for linearity summary.
  name: EPA — U.S. Environmental Protection Agency Linearity Summary API
  slug: epa-linearity-summary-api
- description: Reference lookups (states, counties, sites, CBSAs, parameter classes, agencies).
  name: EPA — U.S. Environmental Protection Agency Lists API
  slug: epa-lists-api
- description: The LME Qualifications API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for lme qualifications.
  name: EPA — U.S. Environmental Protection Agency LME Qualifications API
  slug: epa-lme-qualifications-api
- description: The Loads API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for loads.
  name: EPA — U.S. Environmental Protection Agency Loads API
  slug: epa-loads-api
- description: The Locations API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for locations.
  name: EPA — U.S. Environmental Protection Agency Locations API
  slug: epa-locations-api
- description: The Login API from EPA — U.S. Environmental Protection Agency — 3 operation(s) for login.
  name: EPA — U.S. Environmental Protection Agency Login API
  slug: epa-login-api
- description: The Logout API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for logout.
  name: EPA — U.S. Environmental Protection Agency Logout API
  slug: epa-logout-api
- description: The Lookups API from EPA — U.S. Environmental Protection Agency — 10 operation(s) for lookups.
  name: EPA — U.S. Environmental Protection Agency Lookups API
  slug: epa-lookups-api
- description: The MATS Methods API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for mats methods.
  name: EPA — U.S. Environmental Protection Agency MATS Methods API
  slug: epa-mats-methods-api
- description: API availability, change history, field definitions, known issues.
  name: EPA — U.S. Environmental Protection Agency Meta Data API
  slug: epa-meta-data-api
- description: The Metadata API from EPA — U.S. Environmental Protection Agency — 7 operation(s) for metadata.
  name: EPA — U.S. Environmental Protection Agency Metadata API
  slug: epa-metadata-api
- description: The Methods API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for methods.
  name: EPA — U.S. Environmental Protection Agency Methods API
  slug: epa-methods-api
- description: Monitor metadata filtered by site, county, state, bounding box, or CBSA.
  name: EPA — U.S. Environmental Protection Agency Monitors API
  slug: epa-monitors-api
- description: The Online Offline Calibration API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for online offline calibration.
  name: EPA — U.S. Environmental Protection Agency Online Offline Calibration API
  slug: epa-online-offline-calibration-api
- description: The PCT Qualifications API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for pct qualifications.
  name: EPA — U.S. Environmental Protection Agency PCT Qualifications API
  slug: epa-pct-qualifications-api
- description: The Plans API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for plans.
  name: EPA — U.S. Environmental Protection Agency Plans API
  slug: epa-plans-api
- description: The Point Source Categories API from EPA — U.S. Environmental Protection Agency — 7 operation(s) for point source categories.
  name: EPA — U.S. Environmental Protection Agency Point Source Categories API
  slug: epa-point-source-categories-api
- description: The Pollutants API from EPA — U.S. Environmental Protection Agency — 6 operation(s) for pollutants.
  name: EPA — U.S. Environmental Protection Agency Pollutants API
  slug: epa-pollutants-api
- description: The Program Codes API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for program codes.
  name: EPA — U.S. Environmental Protection Agency Program Codes API
  slug: epa-program-codes-api
- description: The Protocol Gas API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for protocol gas.
  name: EPA — U.S. Environmental Protection Agency Protocol Gas API
  slug: epa-protocol-gas-api
- description: The QA Certification API from EPA — U.S. Environmental Protection Agency — 4 operation(s) for qa certification.
  name: EPA — U.S. Environmental Protection Agency QA Certification API
  slug: epa-qa-certification-api
- description: The QA Certification Event API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for qa certification event.
  name: EPA — U.S. Environmental Protection Agency QA Certification Event API
  slug: epa-qa-certification-event-api
- description: The Qualifications API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for qualifications.
  name: EPA — U.S. Environmental Protection Agency Qualifications API
  slug: epa-qualifications-api
- description: QA performance evaluations, blanks, audits, collocated assessments.
  name: EPA — U.S. Environmental Protection Agency Quality Assurance API
  slug: epa-quality-assurance-api
- description: Quarterly aggregated values.
  name: EPA — U.S. Environmental Protection Agency Quarterly Data API
  slug: epa-quarterly-data-api
- description: The Rata API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for rata.
  name: EPA — U.S. Environmental Protection Agency Rata API
  slug: epa-rata-api
- description: The Rata Run API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for rata run.
  name: EPA — U.S. Environmental Protection Agency Rata Run API
  slug: epa-rata-run-api
- description: The Rata Summary API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for rata summary.
  name: EPA — U.S. Environmental Protection Agency Rata Summary API
  slug: epa-rata-summary-api
- description: The Rata Traverse API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for rata traverse.
  name: EPA — U.S. Environmental Protection Agency Rata Traverse API
  slug: epa-rata-traverse-api
- description: The Rectangular Duct WAF API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for rectangular duct waf.
  name: EPA — U.S. Environmental Protection Agency Rectangular Duct WAF API
  slug: epa-rectangular-duct-waf-api
- description: The Relationships API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for relationships.
  name: EPA — U.S. Environmental Protection Agency Relationships API
  slug: epa-relationships-api
- description: The Reporting Frequencies API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for reporting frequencies.
  name: EPA — U.S. Environmental Protection Agency Reporting Frequencies API
  slug: epa-reporting-frequencies-api
- description: The Reporting Periods API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for reporting periods.
  name: EPA — U.S. Environmental Protection Agency Reporting Periods API
  slug: epa-reporting-periods-api
- description: The Reports API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for reports.
  name: EPA — U.S. Environmental Protection Agency Reports API
  slug: epa-reports-api
- description: The Resource Conservation and Recovery Act API from EPA — U.S. Environmental Protection Agency — 7 operation(s) for resource conservation and recovery act.
  name: EPA — U.S. Environmental Protection Agency Resource Conservation and Recovery Act API
  slug: epa-resource-conservation-and-recovery-act-api
- description: The Safe Drinking Water API from EPA — U.S. Environmental Protection Agency — 3 operation(s) for safe drinking water.
  name: EPA — U.S. Environmental Protection Agency Safe Drinking Water API
  slug: epa-safe-drinking-water-api
- description: Raw sample observations.
  name: EPA — U.S. Environmental Protection Agency Sample Data API
  slug: epa-sample-data-api
- description: Account registration.
  name: EPA — U.S. Environmental Protection Agency Sign Up API
  slug: epa-sign-up-api
- description: The Spans API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for spans.
  name: EPA — U.S. Environmental Protection Agency Spans API
  slug: epa-spans-api
- description: The Status API from EPA — U.S. Environmental Protection Agency — 12 operation(s) for status.
  name: EPA — U.S. Environmental Protection Agency Status API
  slug: epa-status-api
- description: The Support API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for support.
  name: EPA — U.S. Environmental Protection Agency Support API
  slug: epa-support-api
- description: The System Components API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for system components.
  name: EPA — U.S. Environmental Protection Agency System Components API
  slug: epa-system-components-api
- description: The System Fuel Flows API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for system fuel flows.
  name: EPA — U.S. Environmental Protection Agency System Fuel Flows API
  slug: epa-system-fuel-flows-api
- description: The Systems API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for systems.
  name: EPA — U.S. Environmental Protection Agency Systems API
  slug: epa-systems-api
- description: The Test Extension Exemption API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for test extension exemption.
  name: EPA — U.S. Environmental Protection Agency Test Extension Exemption API
  slug: epa-test-extension-exemption-api
- description: The Test Qualification API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for test qualification.
  name: EPA — U.S. Environmental Protection Agency Test Qualification API
  slug: epa-test-qualification-api
- description: The Test Summary API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for test summary.
  name: EPA — U.S. Environmental Protection Agency Test Summary API
  slug: epa-test-summary-api
- description: Raw transaction-format exports.
  name: EPA — U.S. Environmental Protection Agency Transactions API
  slug: epa-transactions-api
- description: The Transmitter Transducer Accuracy API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for transmitter transducer accuracy.
  name: EPA — U.S. Environmental Protection Agency Transmitter Transducer Accuracy API
  slug: epa-transmitter-transducer-accuracy-api
- description: The Treatment Technologies API from EPA — U.S. Environmental Protection Agency — 6 operation(s) for treatment technologies.
  name: EPA — U.S. Environmental Protection Agency Treatment Technologies API
  slug: epa-treatment-technologies-api
- description: The Unit Capacities API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for unit capacities.
  name: EPA — U.S. Environmental Protection Agency Unit Capacities API
  slug: epa-unit-capacities-api
- description: The Unit Controls API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for unit controls.
  name: EPA — U.S. Environmental Protection Agency Unit Controls API
  slug: epa-unit-controls-api
- description: The Unit Default Test API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for unit default test.
  name: EPA — U.S. Environmental Protection Agency Unit Default Test API
  slug: epa-unit-default-test-api
- description: The Unit Default Test Run API from EPA — U.S. Environmental Protection Agency — 2 operation(s) for unit default test run.
  name: EPA — U.S. Environmental Protection Agency Unit Default Test Run API
  slug: epa-unit-default-test-run-api
- description: The Unit Fuels API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for unit fuels.
  name: EPA — U.S. Environmental Protection Agency Unit Fuels API
  slug: epa-unit-fuels-api
- description: The Unit Programs API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for unit programs.
  name: EPA — U.S. Environmental Protection Agency Unit Programs API
  slug: epa-unit-programs-api
- description: The Unit Type Codes API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for unit type codes.
  name: EPA — U.S. Environmental Protection Agency Unit Type Codes API
  slug: epa-unit-type-codes-api
- description: The Units API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for units.
  name: EPA — U.S. Environmental Protection Agency Units API
  slug: epa-units-api
- description: The User API from EPA — U.S. Environmental Protection Agency — 1 operation(s) for user.
  name: EPA — U.S. Environmental Protection Agency User API
  slug: epa-user-api
- description: The Utility Services API from EPA — U.S. Environmental Protection Agency — 5 operation(s) for utility services.
  name: EPA — U.S. Environmental Protection Agency Utility Services API
  slug: epa-utility-services-api
- description: UV index hourly and daily forecast endpoints.
  name: EPA — U.S. Environmental Protection Agency UV Index API
  slug: epa-uv-index-api
artifact_total: 2289
collections:
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes API
  slug: postman-epa-account-type-codes-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Accounts API
  slug: postman-epa-accounts-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Air Emission Testing API
  slug: postman-epa-air-emission-testing-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Allowance Compliance API
  slug: postman-epa-allowance-compliance-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Allowance Holdings API
  slug: postman-epa-allowance-holdings-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Allowance Transactions API
  slug: postman-epa-allowance-transactions-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Analysis Services API
  slug: postman-epa-analysis-services-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Analyzer Ranges API
  slug: postman-epa-analyzer-ranges-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Annual Data API
  slug: postman-epa-annual-data-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Appendix E Correlation Test Run API
  slug: postman-epa-appendix-e-correlation-test-run-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Appendix E Correlation Test Summary API
  slug: postman-epa-appendix-e-correlation-test-summary-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Appendix E Heat Input From Gas API
  slug: postman-epa-appendix-e-heat-input-from-gas-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Appendix E Heat Input From Oil API
  slug: postman-epa-appendix-e-heat-input-from-oil-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Apportioned Annual Emissions API
  slug: postman-epa-apportioned-annual-emissions-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Apportioned Daily Emissions API
  slug: postman-epa-apportioned-daily-emissions-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Apportioned Emissions API
  slug: postman-epa-apportioned-emissions-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Apportioned Hourly Emissions API
  slug: postman-epa-apportioned-hourly-emissions-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Apportioned Hourly MATS Emissions API
  slug: postman-epa-apportioned-hourly-mats-emissions-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Apportioned MATS Emissions API
  slug: postman-epa-apportioned-mats-emissions-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Apportioned Monthly Emissions API
  slug: postman-epa-apportioned-monthly-emissions-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Apportioned Ozone Emissions API
  slug: postman-epa-apportioned-ozone-emissions-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Apportioned Quarterly Emissions API
  slug: postman-epa-apportioned-quarterly-emissions-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Attributes API
  slug: postman-epa-attributes-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Bap API
  slug: postman-epa-bap-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Bulk Files API
  slug: postman-epa-bulk-files-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Calibration Injection API
  slug: postman-epa-calibration-injection-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Case Enforcement API
  slug: postman-epa-case-enforcement-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes CIP Indexing Services API
  slug: postman-epa-cip-indexing-services-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Codes & Descriptions API
  slug: postman-epa-codes-descriptions-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Comments API
  slug: postman-epa-comments-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Components API
  slug: postman-epa-components-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Config API
  slug: postman-epa-config-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Configurations API
  slug: postman-epa-configurations-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Contact API
  slug: postman-epa-contact-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Control Codes API
  slug: postman-epa-control-codes-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Custom Search API
  slug: postman-epa-custom-search-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Cycle Time Injection API
  slug: postman-epa-cycle-time-injection-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Cycle Time Summary API
  slug: postman-epa-cycle-time-summary-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Daily Data API
  slug: postman-epa-daily-data-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Data Service API
  slug: postman-epa-data-service-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Defaults API
  slug: postman-epa-defaults-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Detailed Facility Report API
  slug: postman-epa-detailed-facility-report-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Effluent Charts API
  slug: postman-epa-effluent-charts-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Emissions API
  slug: postman-epa-emissions-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Emissions Compliance API
  slug: postman-epa-emissions-compliance-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Emissions Views API
  slug: postman-epa-emissions-views-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Facilities API
  slug: postman-epa-facilities-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Facility Info API
  slug: postman-epa-facility-info-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Facility Information API
  slug: postman-epa-facility-information-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Flow Rata Run API
  slug: postman-epa-flow-rata-run-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Flow To Load Check API
  slug: postman-epa-flow-to-load-check-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Flow To Load Reference API
  slug: postman-epa-flow-to-load-reference-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Formio API
  slug: postman-epa-formio-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Formulas API
  slug: postman-epa-formulas-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Fuel Flow To Load Baseline API
  slug: postman-epa-fuel-flow-to-load-baseline-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Fuel Flow To Load Test API
  slug: postman-epa-fuel-flow-to-load-test-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Fuel Flowmeter Accuracy API
  slug: postman-epa-fuel-flowmeter-accuracy-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Fuel Type Codes API
  slug: postman-epa-fuel-type-codes-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Glossary API
  slug: postman-epa-glossary-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes GraphQL API
  slug: postman-epa-graphql-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Health API
  slug: postman-epa-health-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Help API
  slug: postman-epa-help-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Hg Injection API
  slug: postman-epa-hg-injection-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Hg Summary API
  slug: postman-epa-hg-summary-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes How's My Waterway API
  slug: postman-epa-how-s-my-waterway-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes LEE Qualifications API
  slug: postman-epa-lee-qualifications-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Linearity Injection API
  slug: postman-epa-linearity-injection-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Linearity Summary API
  slug: postman-epa-linearity-summary-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Lists API
  slug: postman-epa-lists-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes LME Qualifications API
  slug: postman-epa-lme-qualifications-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Loads API
  slug: postman-epa-loads-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Locations API
  slug: postman-epa-locations-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Login API
  slug: postman-epa-login-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Logout API
  slug: postman-epa-logout-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Lookups API
  slug: postman-epa-lookups-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes MATS Methods API
  slug: postman-epa-mats-methods-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Meta Data API
  slug: postman-epa-meta-data-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Metadata API
  slug: postman-epa-metadata-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Methods API
  slug: postman-epa-methods-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Monitors API
  slug: postman-epa-monitors-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Online Offline Calibration API
  slug: postman-epa-online-offline-calibration-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes PCT Qualifications API
  slug: postman-epa-pct-qualifications-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Plans API
  slug: postman-epa-plans-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Point Source Categories API
  slug: postman-epa-point-source-categories-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Pollutants API
  slug: postman-epa-pollutants-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Program Codes API
  slug: postman-epa-program-codes-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Protocol Gas API
  slug: postman-epa-protocol-gas-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes QA Certification API
  slug: postman-epa-qa-certification-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes QA Certification Event API
  slug: postman-epa-qa-certification-event-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Qualifications API
  slug: postman-epa-qualifications-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Quality Assurance API
  slug: postman-epa-quality-assurance-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Quarterly Data API
  slug: postman-epa-quarterly-data-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Rata API
  slug: postman-epa-rata-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Rata Run API
  slug: postman-epa-rata-run-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Rata Summary API
  slug: postman-epa-rata-summary-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Rata Traverse API
  slug: postman-epa-rata-traverse-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Rectangular Duct WAF API
  slug: postman-epa-rectangular-duct-waf-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Relationships API
  slug: postman-epa-relationships-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Reporting Frequencies API
  slug: postman-epa-reporting-frequencies-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Reporting Periods API
  slug: postman-epa-reporting-periods-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Reports API
  slug: postman-epa-reports-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Resource Conservation and Recovery Act API
  slug: postman-epa-resource-conservation-and-recovery-act-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Safe Drinking Water API
  slug: postman-epa-safe-drinking-water-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Sample Data API
  slug: postman-epa-sample-data-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Sign Up API
  slug: postman-epa-sign-up-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Spans API
  slug: postman-epa-spans-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Status API
  slug: postman-epa-status-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Support API
  slug: postman-epa-support-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes System Components API
  slug: postman-epa-system-components-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes System Fuel Flows API
  slug: postman-epa-system-fuel-flows-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Systems API
  slug: postman-epa-systems-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Test Extension Exemption API
  slug: postman-epa-test-extension-exemption-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Test Qualification API
  slug: postman-epa-test-qualification-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Test Summary API
  slug: postman-epa-test-summary-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Transactions API
  slug: postman-epa-transactions-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Transmitter Transducer Accuracy API
  slug: postman-epa-transmitter-transducer-accuracy-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Treatment Technologies API
  slug: postman-epa-treatment-technologies-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Unit Capacities API
  slug: postman-epa-unit-capacities-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Unit Controls API
  slug: postman-epa-unit-controls-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Unit Default Test API
  slug: postman-epa-unit-default-test-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Unit Default Test Run API
  slug: postman-epa-unit-default-test-run-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Unit Fuels API
  slug: postman-epa-unit-fuels-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Unit Programs API
  slug: postman-epa-unit-programs-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Unit Type Codes API
  slug: postman-epa-unit-type-codes-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Units API
  slug: postman-epa-units-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes User API
  slug: postman-epa-user-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes Utility Services API
  slug: postman-epa-utility-services-api
- collection_type: postman
  name: EPA Air Quality System (AQS) Account Type Codes UV Index API
  slug: postman-epa-uv-index-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: EPA Air Quality System (AQS) API
  slug: open-aqs
- collection_type: open
  name: Account Management OpenAPI Specification
  slug: open-cam-account
- collection_type: open
  name: CAMD Administrative & General Services OpenAPI Specification
  slug: open-cam-camd-services
- collection_type: open
  name: Emissions Management OpenAPI Specification
  slug: open-cam-emissions
- collection_type: open
  name: Facilities Management OpenAPI Specification
  slug: open-cam-facilities
- collection_type: open
  name: Master Data Management OpenAPI Specification
  slug: open-cam-master-data
- collection_type: open
  name: Monitor Plan Management OpenAPI Specification
  slug: open-cam-monitor-plan
- collection_type: open
  name: QA Certification Management OpenAPI Specification
  slug: open-cam-qa-cert
- collection_type: open
  name: Streaming Services OpenAPI Specification
  slug: open-cam-streaming
- collection_type: open
  name: CIP-service Indexing API
  slug: open-cip-service
- collection_type: open
  name: epa-csb-server
  slug: open-csb-rebate
- collection_type: open
  name: U.S. EPA Enforcement and Compliance History Online (ECHO) - Clean Air Act
  slug: open-echo-air
- collection_type: open
  name: U.S. EPA Enforcement and Compliance History Online (ECHO) - All Data
  slug: open-echo-all
- collection_type: open
  name: U.S. EPA Enforcement and Compliance History Online (ECHO) - Enforcement Case Search
  slug: open-echo-case
- collection_type: open
  name: U.S. EPA Enforcement and Compliance History Online (ECHO) - Clean Water Act (CWA) Rest Services
  slug: open-echo-cwa
- collection_type: open
  name: U.S. EPA Enforcement and Compliance History Online (ECHO) - Detailed Facility Report (DFR)
  slug: open-echo-dfr
- collection_type: open
  name: U.S. EPA Enforcement and Compliance History Online (ECHO) - Effluent Charting and Reporting
  slug: open-echo-effluent
- collection_type: open
  name: U.S. EPA Enforcement and Compliance History Online (ECHO) - Resource Conservation and Recovery Act
  slug: open-echo-rcra
- collection_type: open
  name: U.S. EPA Enforcement and Compliance History Online (ECHO) - Safe Drinking Water Act
  slug: open-echo-sdw
- collection_type: open
  name: U.S. EPA WaterSense
  slug: open-elg-search
- collection_type: open
  name: EPA Envirofacts Data Service API
  slug: open-envirofacts
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes API
  slug: open-epa-account-type-codes-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Accounts API
  slug: open-epa-accounts-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Air Emission Testing API
  slug: open-epa-air-emission-testing-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Allowance Compliance API
  slug: open-epa-allowance-compliance-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Allowance Holdings API
  slug: open-epa-allowance-holdings-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Allowance Transactions API
  slug: open-epa-allowance-transactions-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Analysis Services API
  slug: open-epa-analysis-services-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Analyzer Ranges API
  slug: open-epa-analyzer-ranges-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Annual Data API
  slug: open-epa-annual-data-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Appendix E Correlation Test Run API
  slug: open-epa-appendix-e-correlation-test-run-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Appendix E Correlation Test Summary API
  slug: open-epa-appendix-e-correlation-test-summary-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Appendix E Heat Input From Gas API
  slug: open-epa-appendix-e-heat-input-from-gas-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Appendix E Heat Input From Oil API
  slug: open-epa-appendix-e-heat-input-from-oil-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Apportioned Annual Emissions API
  slug: open-epa-apportioned-annual-emissions-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Apportioned Daily Emissions API
  slug: open-epa-apportioned-daily-emissions-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Apportioned Emissions API
  slug: open-epa-apportioned-emissions-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Apportioned Hourly Emissions API
  slug: open-epa-apportioned-hourly-emissions-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Apportioned Hourly MATS Emissions API
  slug: open-epa-apportioned-hourly-mats-emissions-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Apportioned MATS Emissions API
  slug: open-epa-apportioned-mats-emissions-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Apportioned Monthly Emissions API
  slug: open-epa-apportioned-monthly-emissions-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Apportioned Ozone Emissions API
  slug: open-epa-apportioned-ozone-emissions-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Apportioned Quarterly Emissions API
  slug: open-epa-apportioned-quarterly-emissions-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Attributes API
  slug: open-epa-attributes-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Bap API
  slug: open-epa-bap-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Bulk Files API
  slug: open-epa-bulk-files-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Calibration Injection API
  slug: open-epa-calibration-injection-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Case Enforcement API
  slug: open-epa-case-enforcement-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes CIP Indexing Services API
  slug: open-epa-cip-indexing-services-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Codes & Descriptions API
  slug: open-epa-codes-descriptions-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Comments API
  slug: open-epa-comments-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Components API
  slug: open-epa-components-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Config API
  slug: open-epa-config-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Configurations API
  slug: open-epa-configurations-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Contact API
  slug: open-epa-contact-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Control Codes API
  slug: open-epa-control-codes-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Custom Search API
  slug: open-epa-custom-search-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Cycle Time Injection API
  slug: open-epa-cycle-time-injection-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Cycle Time Summary API
  slug: open-epa-cycle-time-summary-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Daily Data API
  slug: open-epa-daily-data-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Data Service API
  slug: open-epa-data-service-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Defaults API
  slug: open-epa-defaults-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Detailed Facility Report API
  slug: open-epa-detailed-facility-report-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Effluent Charts API
  slug: open-epa-effluent-charts-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Emissions API
  slug: open-epa-emissions-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Emissions Compliance API
  slug: open-epa-emissions-compliance-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Emissions Views API
  slug: open-epa-emissions-views-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Facilities API
  slug: open-epa-facilities-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Facility Info API
  slug: open-epa-facility-info-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Facility Information API
  slug: open-epa-facility-information-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Flow Rata Run API
  slug: open-epa-flow-rata-run-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Flow To Load Check API
  slug: open-epa-flow-to-load-check-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Flow To Load Reference API
  slug: open-epa-flow-to-load-reference-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Formio API
  slug: open-epa-formio-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Formulas API
  slug: open-epa-formulas-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Fuel Flow To Load Baseline API
  slug: open-epa-fuel-flow-to-load-baseline-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Fuel Flow To Load Test API
  slug: open-epa-fuel-flow-to-load-test-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Fuel Flowmeter Accuracy API
  slug: open-epa-fuel-flowmeter-accuracy-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Fuel Type Codes API
  slug: open-epa-fuel-type-codes-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Glossary API
  slug: open-epa-glossary-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes GraphQL API
  slug: open-epa-graphql-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Health API
  slug: open-epa-health-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Help API
  slug: open-epa-help-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Hg Injection API
  slug: open-epa-hg-injection-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Hg Summary API
  slug: open-epa-hg-summary-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes How's My Waterway API
  slug: open-epa-how-s-my-waterway-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes LEE Qualifications API
  slug: open-epa-lee-qualifications-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Linearity Injection API
  slug: open-epa-linearity-injection-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Linearity Summary API
  slug: open-epa-linearity-summary-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Lists API
  slug: open-epa-lists-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes LME Qualifications API
  slug: open-epa-lme-qualifications-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Loads API
  slug: open-epa-loads-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Locations API
  slug: open-epa-locations-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Login API
  slug: open-epa-login-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Logout API
  slug: open-epa-logout-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Lookups API
  slug: open-epa-lookups-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes MATS Methods API
  slug: open-epa-mats-methods-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Meta Data API
  slug: open-epa-meta-data-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Metadata API
  slug: open-epa-metadata-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Methods API
  slug: open-epa-methods-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Monitors API
  slug: open-epa-monitors-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Online Offline Calibration API
  slug: open-epa-online-offline-calibration-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes PCT Qualifications API
  slug: open-epa-pct-qualifications-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Plans API
  slug: open-epa-plans-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Point Source Categories API
  slug: open-epa-point-source-categories-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Pollutants API
  slug: open-epa-pollutants-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Program Codes API
  slug: open-epa-program-codes-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Protocol Gas API
  slug: open-epa-protocol-gas-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes QA Certification API
  slug: open-epa-qa-certification-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes QA Certification Event API
  slug: open-epa-qa-certification-event-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Qualifications API
  slug: open-epa-qualifications-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Quality Assurance API
  slug: open-epa-quality-assurance-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Quarterly Data API
  slug: open-epa-quarterly-data-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Rata API
  slug: open-epa-rata-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Rata Run API
  slug: open-epa-rata-run-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Rata Summary API
  slug: open-epa-rata-summary-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Rata Traverse API
  slug: open-epa-rata-traverse-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Rectangular Duct WAF API
  slug: open-epa-rectangular-duct-waf-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Relationships API
  slug: open-epa-relationships-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Reporting Frequencies API
  slug: open-epa-reporting-frequencies-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Reporting Periods API
  slug: open-epa-reporting-periods-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Reports API
  slug: open-epa-reports-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Resource Conservation and Recovery Act API
  slug: open-epa-resource-conservation-and-recovery-act-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Safe Drinking Water API
  slug: open-epa-safe-drinking-water-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Sample Data API
  slug: open-epa-sample-data-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Sign Up API
  slug: open-epa-sign-up-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Spans API
  slug: open-epa-spans-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Status API
  slug: open-epa-status-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Support API
  slug: open-epa-support-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes System Components API
  slug: open-epa-system-components-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes System Fuel Flows API
  slug: open-epa-system-fuel-flows-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Systems API
  slug: open-epa-systems-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Test Extension Exemption API
  slug: open-epa-test-extension-exemption-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Test Qualification API
  slug: open-epa-test-qualification-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Test Summary API
  slug: open-epa-test-summary-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Transactions API
  slug: open-epa-transactions-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Transmitter Transducer Accuracy API
  slug: open-epa-transmitter-transducer-accuracy-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Treatment Technologies API
  slug: open-epa-treatment-technologies-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Unit Capacities API
  slug: open-epa-unit-capacities-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Unit Controls API
  slug: open-epa-unit-controls-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Unit Default Test API
  slug: open-epa-unit-default-test-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Unit Default Test Run API
  slug: open-epa-unit-default-test-run-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Unit Fuels API
  slug: open-epa-unit-fuels-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Unit Programs API
  slug: open-epa-unit-programs-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Unit Type Codes API
  slug: open-epa-unit-type-codes-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Units API
  slug: open-epa-units-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes User API
  slug: open-epa-user-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes Utility Services API
  slug: open-epa-utility-services-api
- collection_type: open
  name: EPA Air Quality System (AQS) Account Type Codes UV Index API
  slug: open-epa-uv-index-api
- collection_type: open
  name: US EPA How's My Waterway
  slug: open-mywaterway
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/epa-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/USEPA/rExpertQuery/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/USEPA/rExpertQuery/blob/develop/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/epa--us-environmental-protection-agency/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/epa-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/epa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/epa-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.epa.gov
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.epa.gov/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.epa.gov/data/application-programming-interface-api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.epa.gov/data
- group: docs
  title: ''
  type: Documentation
  url: https://www.epa.gov/developers/data-data-products
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/USEPA
- group: company
  title: ''
  type: Blog
  url: https://www.epa.gov/newsroom
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/USEPAgov
- group: other
  title: ''
  type: X
  url: https://twitter.com/EPA
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/u-s--environmental-protection-agency/
- group: operate
  title: ''
  type: Support
  url: https://www.epa.gov/home/forms/contact-epa
- group: operate
  title: ''
  type: Contact
  url: https://www.epa.gov/aboutepa/forms/contact-us-about-epa
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.epa.gov/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.epa.gov/privacy/privacy-and-security-notice
- group: operate
  title: ''
  type: StatusPage
  url: https://status.epa.gov/
- group: company
  title: ''
  type: Newsletter
  url: https://www.epa.gov/newsroom/email-subscriptions-epa-news-releases
- group: auth
  title: ''
  type: Compliance
  url: https://echo.epa.gov/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/epa
- group: design
  title: ''
  type: SpectralRules
  url: rules/epa-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/epa-vocabulary.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/epa-rate-limits.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/epa-context.jsonld
created: '2026-05-28'
description: Web services, data products, and open data spanning the U.S. Environmental Protection Agency. Programmatic access to air quality, water quality, hazardous waste, toxic releases, facility compliance, power-sector emissions, computational toxicology, and watershed assessments through dozens of public APIs.
examples:
- key_count: 2
  name: Aqs Envelope Example
  slug: aqs-envelope-example
- key_count: 5
  name: Aqs Header Example
  slug: aqs-header-example
- key_count: 10
  name: Cam Account Account Attributes Dto Example
  slug: cam-account-account-attributes-dto-example
- key_count: 2
  name: Cam Account Account Dto Example
  slug: cam-account-account-dto-example
- key_count: 22
  name: Cam Account Allowance Compliance Dto Example
  slug: cam-account-allowance-compliance-dto-example
- key_count: 12
  name: Cam Account Allowance Holdings Dto Example
  slug: cam-account-allowance-holdings-dto-example
- key_count: 27
  name: Cam Account Allowance Transactions Dto Example
  slug: cam-account-allowance-transactions-dto-example
- key_count: 6
  name: Cam Account Applicable Account Attributes Dto Example
  slug: cam-account-applicable-account-attributes-dto-example
- key_count: 5
  name: Cam Account Applicable Allowance Compliance Attributes Dto Example
  slug: cam-account-applicable-allowance-compliance-attributes-dto-example
- key_count: 7
  name: Cam Account Applicable Allowance Holdings Attributes Dto Example
  slug: cam-account-applicable-allowance-holdings-attributes-dto-example
- key_count: 13
  name: Cam Account Applicable Allowance Transactions Attributes Dto Example
  slug: cam-account-applicable-allowance-transactions-attributes-dto-example
- key_count: 4
  name: Cam Account Applicable Compliance Attributes Dto Example
  slug: cam-account-applicable-compliance-attributes-dto-example
- key_count: 12
  name: Cam Account Emissions Compliance Dto Example
  slug: cam-account-emissions-compliance-dto-example
- key_count: 2
  name: Cam Account Owner Operators Dto Example
  slug: cam-account-owner-operators-dto-example
- key_count: 8
  name: Cam Camd Services Bulk File Dto Example
  slug: cam-camd-services-bulk-file-dto-example
- key_count: 2
  name: Cam Camd Services Email Recipient List Request Dto Example
  slug: cam-camd-services-email-recipient-list-request-dto-example
- key_count: 3
  name: Cam Camd Services Email Recipient List Response Dto Example
  slug: cam-camd-services-email-recipient-list-response-dto-example
- key_count: 2
  name: Cam Camd Services Report Column Dto Example
  slug: cam-camd-services-report-column-dto-example
- key_count: 4
  name: Cam Camd Services Report Detail Dto Example
  slug: cam-camd-services-report-detail-dto-example
- key_count: 3
  name: Cam Camd Services Report Dto Example
  slug: cam-camd-services-report-dto-example
- key_count: 7
  name: Cam Emissions Annual Apportioned Emissions Aggregation Dto Example
  slug: cam-emissions-annual-apportioned-emissions-aggregation-dto-example
- key_count: 10
  name: Cam Emissions Annual Apportioned Emissions Facility Aggregation Dto Example
  slug: cam-emissions-annual-apportioned-emissions-facility-aggregation-dto-example
- key_count: 8
  name: Cam Emissions Annual Apportioned Emissions State Aggregation Dto Example
  slug: cam-emissions-annual-apportioned-emissions-state-aggregation-dto-example
- key_count: 26
  name: Cam Emissions Annual Unit Data View Example
  slug: cam-emissions-annual-unit-data-view-example
- key_count: 7
  name: Cam Emissions Applicable Apportioned Emissions Attributes Dto Example
  slug: cam-emissions-applicable-apportioned-emissions-attributes-dto-example
- key_count: 10
  name: Cam Emissions Daily Apportioned Emissions Facility Aggregation Dto Example
  slug: cam-emissions-daily-apportioned-emissions-facility-aggregation-dto-example
- key_count: 7
  name: Cam Emissions Daily Apportioned Emissions National Aggregation Dto Example
  slug: cam-emissions-daily-apportioned-emissions-national-aggregation-dto-example
- key_count: 8
  name: Cam Emissions Daily Apportioned Emissions State Aggregation Dto Example
  slug: cam-emissions-daily-apportioned-emissions-state-aggregation-dto-example
- key_count: 25
  name: Cam Emissions Day Unit Data View Example
  slug: cam-emissions-day-unit-data-view-example
- key_count: 15
  name: Cam Emissions Emissions Review Dto Example
  slug: cam-emissions-emissions-review-dto-example
- key_count: 4
  name: Cam Emissions Emissions Submissions Progress Dto Example
  slug: cam-emissions-emissions-submissions-progress-dto-example
- key_count: 2
  name: Cam Emissions Emissions View Dto Example
  slug: cam-emissions-emissions-view-dto-example
- key_count: 34
  name: Cam Emissions Hour Unit Data View Example
  slug: cam-emissions-hour-unit-data-view-example
- key_count: 30
  name: Cam Emissions Hour Unit Mats Data View Example
  slug: cam-emissions-hour-unit-mats-data-view-example
- key_count: 34
  name: Cam Emissions Hourly Apportioned Emissions Dto Example
  slug: cam-emissions-hourly-apportioned-emissions-dto-example
- key_count: 11
  name: Cam Emissions Hourly Apportioned Emissions Facility Aggregation Dto Example
  slug: cam-emissions-hourly-apportioned-emissions-facility-aggregation-dto-example
- key_count: 8
  name: Cam Emissions Hourly Apportioned Emissions National Aggregation Dto Example
  slug: cam-emissions-hourly-apportioned-emissions-national-aggregation-dto-example
- key_count: 9
  name: Cam Emissions Hourly Apportioned Emissions State Aggregation Dto Example
  slug: cam-emissions-hourly-apportioned-emissions-state-aggregation-dto-example
- key_count: 30
  name: Cam Emissions Hourly Mats Apportioned Emissions Dto Example
  slug: cam-emissions-hourly-mats-apportioned-emissions-dto-example
- key_count: 26
  name: Cam Emissions Month Unit Data View Example
  slug: cam-emissions-month-unit-data-view-example
- key_count: 11
  name: Cam Emissions Monthly Apportioned Emissions Facility Aggregation Dto Example
  slug: cam-emissions-monthly-apportioned-emissions-facility-aggregation-dto-example
- key_count: 8
  name: Cam Emissions Monthly Apportioned Emissions National Aggregation Dto Example
  slug: cam-emissions-monthly-apportioned-emissions-national-aggregation-dto-example
- key_count: 9
  name: Cam Emissions Monthly Apportioned Emissions State Aggregation Dto Example
  slug: cam-emissions-monthly-apportioned-emissions-state-aggregation-dto-example
- key_count: 10
  name: Cam Emissions Ozone Apportioned Emissions Facility Aggregation Dto Example
  slug: cam-emissions-ozone-apportioned-emissions-facility-aggregation-dto-example
- key_count: 7
  name: Cam Emissions Ozone Apportioned Emissions National Aggregation Dto Example
  slug: cam-emissions-ozone-apportioned-emissions-national-aggregation-dto-example
- key_count: 8
  name: Cam Emissions Ozone Apportioned Emissions State Aggregation Dto Example
  slug: cam-emissions-ozone-apportioned-emissions-state-aggregation-dto-example
- key_count: 26
  name: Cam Emissions Ozone Unit Data View Example
  slug: cam-emissions-ozone-unit-data-view-example
- key_count: 27
  name: Cam Emissions Quarter Unit Data View Example
  slug: cam-emissions-quarter-unit-data-view-example
- key_count: 11
  name: Cam Emissions Quarterly Apportioned Emissions Facility Aggregation Dto Example
  slug: cam-emissions-quarterly-apportioned-emissions-facility-aggregation-dto-example
- key_count: 8
  name: Cam Emissions Quarterly Apportioned Emissions National Aggregation Dto Example
  slug: cam-emissions-quarterly-apportioned-emissions-national-aggregation-dto-example
- key_count: 9
  name: Cam Emissions Quarterly Apportioned Emissions State Aggregation Dto Example
  slug: cam-emissions-quarterly-apportioned-emissions-state-aggregation-dto-example
- key_count: 8
  name: Cam Facilities Applicable Facility Attributes Dto Example
  slug: cam-facilities-applicable-facility-attributes-dto-example
- key_count: 30
  name: Cam Facilities Facility Attributes Dto Example
  slug: cam-facilities-facility-attributes-dto-example
- key_count: 5
  name: Cam Facilities Facility Dto Example
  slug: cam-facilities-facility-dto-example
- key_count: 4
  name: Cam Master Data Account Type Dto Example
  slug: cam-master-data-account-type-dto-example
- key_count: 2
  name: Cam Master Data Code Table Dto Example
  slug: cam-master-data-code-table-dto-example
- key_count: 4
  name: Cam Master Data Control Technology Dto Example
  slug: cam-master-data-control-technology-dto-example
- key_count: 4
  name: Cam Master Data Data Column Dto Example
  slug: cam-master-data-data-column-dto-example
- key_count: 5
  name: Cam Master Data Data Set Dto Example
  slug: cam-master-data-data-set-dto-example
- key_count: 4
  name: Cam Master Data Data Table Dto Example
  slug: cam-master-data-data-table-dto-example
- key_count: 4
  name: Cam Master Data Fuel Type Dto Example
  slug: cam-master-data-fuel-type-dto-example
- key_count: 12
  name: Cam Master Data Program Dto Example
  slug: cam-master-data-program-dto-example
- key_count: 8
  name: Cam Master Data Reporting Period Dto Example
  slug: cam-master-data-reporting-period-dto-example
- key_count: 5
  name: Cam Master Data Unit Type Dto Example
  slug: cam-master-data-unit-type-dto-example
- key_count: 12
  name: Cam Monitor Plan Analyzer Range Dto Example
  slug: cam-monitor-plan-analyzer-range-dto-example
- key_count: 12
  name: Cam Monitor Plan Analyzer Range Example
  slug: cam-monitor-plan-analyzer-range-example
- key_count: 14
  name: Cam Monitor Plan Component Dto Example
  slug: cam-monitor-plan-component-dto-example
- key_count: 16
  name: Cam Monitor Plan Component Example
  slug: cam-monitor-plan-component-example
- key_count: 19
  name: Cam Monitor Plan Duct Waf Dto Example
  slug: cam-monitor-plan-duct-waf-dto-example
- key_count: 19
  name: Cam Monitor Plan Duct Waf Example
  slug: cam-monitor-plan-duct-waf-example
- key_count: 10
  name: Cam Monitor Plan Emission Evaluation Example
  slug: cam-monitor-plan-emission-evaluation-example
- key_count: 2
  name: Cam Monitor Plan Last Updated Config Dto Example
  slug: cam-monitor-plan-last-updated-config-dto-example
- key_count: 12
  name: Cam Monitor Plan Leequalification Dto Example
  slug: cam-monitor-plan-leequalification-dto-example
- key_count: 13
  name: Cam Monitor Plan Leequalification Example
  slug: cam-monitor-plan-leequalification-example
- key_count: 9
  name: Cam Monitor Plan Lmequalification Dto Example
  slug: cam-monitor-plan-lmequalification-dto-example
- key_count: 10
  name: Cam Monitor Plan Lmequalification Example
  slug: cam-monitor-plan-lmequalification-example
- key_count: 12
  name: Cam Monitor Plan Mats Method Dto Example
  slug: cam-monitor-plan-mats-method-dto-example
- key_count: 12
  name: Cam Monitor Plan Mats Method Example
  slug: cam-monitor-plan-mats-method-example
- key_count: 16
  name: Cam Monitor Plan Monitor Attribute Dto Example
  slug: cam-monitor-plan-monitor-attribute-dto-example
- key_count: 16
  name: Cam Monitor Plan Monitor Attribute Example
  slug: cam-monitor-plan-monitor-attribute-example
- key_count: 18
  name: Cam Monitor Plan Monitor Default Dto Example
  slug: cam-monitor-plan-monitor-default-dto-example
- key_count: 18
  name: Cam Monitor Plan Monitor Default Example
  slug: cam-monitor-plan-monitor-default-example
- key_count: 14
  name: Cam Monitor Plan Monitor Formula Dto Example
  slug: cam-monitor-plan-monitor-formula-dto-example
- key_count: 14
  name: Cam Monitor Plan Monitor Formula Example
  slug: cam-monitor-plan-monitor-formula-example
- key_count: 18
  name: Cam Monitor Plan Monitor Load Dto Example
  slug: cam-monitor-plan-monitor-load-dto-example
- key_count: 18
  name: Cam Monitor Plan Monitor Load Example
  slug: cam-monitor-plan-monitor-load-example
- key_count: 25
  name: Cam Monitor Plan Monitor Location Dto Example
  slug: cam-monitor-plan-monitor-location-dto-example
- key_count: 17
  name: Cam Monitor Plan Monitor Location Example
  slug: cam-monitor-plan-monitor-location-example
- key_count: 14
  name: Cam Monitor Plan Monitor Method Dto Example
  slug: cam-monitor-plan-monitor-method-dto-example
- key_count: 14
  name: Cam Monitor Plan Monitor Method Example
  slug: cam-monitor-plan-monitor-method-example
- key_count: 9
  name: Cam Monitor Plan Monitor Plan Comment Dto Example
  slug: cam-monitor-plan-monitor-plan-comment-dto-example
- key_count: 9
  name: Cam Monitor Plan Monitor Plan Comment Example
  slug: cam-monitor-plan-monitor-plan-comment-example
- key_count: 33
  name: Cam Monitor Plan Monitor Plan Dto Example
  slug: cam-monitor-plan-monitor-plan-dto-example
- key_count: 26
  name: Cam Monitor Plan Monitor Plan Example
  slug: cam-monitor-plan-monitor-plan-example
- key_count: 9
  name: Cam Monitor Plan Monitor Plan Reporting Freq Dto Example
  slug: cam-monitor-plan-monitor-plan-reporting-freq-dto-example
- key_count: 11
  name: Cam Monitor Plan Monitor Plan Reporting Frequency Example
  slug: cam-monitor-plan-monitor-plan-reporting-frequency-example
- key_count: 12
  name: Cam Monitor Plan Monitor Qualification Dto Example
  slug: cam-monitor-plan-monitor-qualification-dto-example
- key_count: 12
  name: Cam Monitor Plan Monitor Qualification Example
  slug: cam-monitor-plan-monitor-qualification-example
- key_count: 23
  name: Cam Monitor Plan Monitor Span Dto Example
  slug: cam-monitor-plan-monitor-span-dto-example
- key_count: 23
  name: Cam Monitor Plan Monitor Span Example
  slug: cam-monitor-plan-monitor-span-example
- key_count: 16
  name: Cam Monitor Plan Monitor System Dto Example
  slug: cam-monitor-plan-monitor-system-dto-example
- key_count: 16
  name: Cam Monitor Plan Monitor System Example
  slug: cam-monitor-plan-monitor-system-example
- key_count: 16
  name: Cam Monitor Plan Pctqualification Dto Example
  slug: cam-monitor-plan-pctqualification-dto-example
- key_count: 17
  name: Cam Monitor Plan Pctqualification Example
  slug: cam-monitor-plan-pctqualification-example
- key_count: 10
  name: Cam Monitor Plan Plant Example
  slug: cam-monitor-plan-plant-example
- key_count: 26
  name: Cam Monitor Plan Program Code Example
  slug: cam-monitor-plan-program-code-example
- key_count: 15
  name: Cam Monitor Plan Program Example
  slug: cam-monitor-plan-program-example
- key_count: 6
  name: Cam Monitor Plan Reporting Freq Dto Example
  slug: cam-monitor-plan-reporting-freq-dto-example
- key_count: 8
  name: Cam Monitor Plan Reporting Period Example
  slug: cam-monitor-plan-reporting-period-example
- key_count: 8
  name: Cam Monitor Plan Stack Pipe Example
  slug: cam-monitor-plan-stack-pipe-example
- key_count: 12
  name: Cam Monitor Plan System Component Dto Example
  slug: cam-monitor-plan-system-component-dto-example
- key_count: 12
  name: Cam Monitor Plan System Component Example
  slug: cam-monitor-plan-system-component-example
- key_count: 15
  name: Cam Monitor Plan System Fuel Flow Dto Example
  slug: cam-monitor-plan-system-fuel-flow-dto-example
- key_count: 13
  name: Cam Monitor Plan System Fuel Flow Example
  slug: cam-monitor-plan-system-fuel-flow-example
- key_count: 8
  name: Cam Monitor Plan Unit Boiler Type Example
  slug: cam-monitor-plan-unit-boiler-type-example
- key_count: 14
  name: Cam Monitor Plan Unit Capacity Dto Example
  slug: cam-monitor-plan-unit-capacity-dto-example
- key_count: 9
  name: Cam Monitor Plan Unit Capacity Example
  slug: cam-monitor-plan-unit-capacity-example
- key_count: 13
  name: Cam Monitor Plan Unit Control Dto Example
  slug: cam-monitor-plan-unit-control-dto-example
- key_count: 14
  name: Cam Monitor Plan Unit Control Example
  slug: cam-monitor-plan-unit-control-example
- key_count: 18
  name: Cam Monitor Plan Unit Dto Example
  slug: cam-monitor-plan-unit-dto-example
- key_count: 19
  name: Cam Monitor Plan Unit Example
  slug: cam-monitor-plan-unit-example
- key_count: 15
  name: Cam Monitor Plan Unit Fuel Dto Example
  slug: cam-monitor-plan-unit-fuel-dto-example
- key_count: 15
  name: Cam Monitor Plan Unit Fuel Example
  slug: cam-monitor-plan-unit-fuel-example
- key_count: 6
  name: Cam Monitor Plan Unit Op Status Example
  slug: cam-monitor-plan-unit-op-status-example
- key_count: 13
  name: Cam Monitor Plan Unit Program Dto Example
  slug: cam-monitor-plan-unit-program-dto-example
- key_count: 23
  name: Cam Monitor Plan Unit Program Example
  slug: cam-monitor-plan-unit-program-example
- key_count: 11
  name: Cam Monitor Plan Unit Stack Configuration Dto Example
  slug: cam-monitor-plan-unit-stack-configuration-dto-example
- key_count: 10
  name: Cam Monitor Plan Unit Stack Configuration Example
  slug: cam-monitor-plan-unit-stack-configuration-example
- key_count: 14
  name: Cam Qa Cert Air Emission Testing Dto Example
  slug: cam-qa-cert-air-emission-testing-dto-example
- key_count: 11
  name: Cam Qa Cert App Ecorrelation Test Run Base Dto Example
  slug: cam-qa-cert-app-ecorrelation-test-run-base-dto-example
- key_count: 20
  name: Cam Qa Cert App Ecorrelation Test Run Dto Example
  slug: cam-qa-cert-app-ecorrelation-test-run-dto-example
- key_count: 18
  name: Cam Qa Cert App Ecorrelation Test Run Record Dto Example
  slug: cam-qa-cert-app-ecorrelation-test-run-record-dto-example
- key_count: 12
  name: Cam Qa Cert App Ecorrelation Test Summary Dto Example
  slug: cam-qa-cert-app-ecorrelation-test-summary-dto-example
- key_count: 11
  name: Cam Qa Cert App Ecorrelation Test Summary Record Dto Example
  slug: cam-qa-cert-app-ecorrelation-test-summary-record-dto-example
- key_count: 10
  name: Cam Qa Cert App Eheat Input From Gas Dto Example
  slug: cam-qa-cert-app-eheat-input-from-gas-dto-example
- key_count: 10
  name: Cam Qa Cert App Eheat Input From Gas Record Dto Example
  slug: cam-qa-cert-app-eheat-input-from-gas-record-dto-example
- key_count: 16
  name: Cam Qa Cert App Eheat Input From Oil Dto Example
  slug: cam-qa-cert-app-eheat-input-from-oil-dto-example
- key_count: 16
  name: Cam Qa Cert App Eheat Input From Oil Record Dto Example
  slug: cam-qa-cert-app-eheat-input-from-oil-record-dto-example
- key_count: 25
  name: Cam Qa Cert Calibration Injection Dto Example
  slug: cam-qa-cert-calibration-injection-dto-example
- key_count: 22
  name: Cam Qa Cert Cert Event Review And Submit Dto Example
  slug: cam-qa-cert-cert-event-review-and-submit-dto-example
- key_count: 17
  name: Cam Qa Cert Cycle Time Injection Dto Example
  slug: cam-qa-cert-cycle-time-injection-dto-example
- key_count: 17
  name: Cam Qa Cert Cycle Time Injection Record Dto Example
  slug: cam-qa-cert-cycle-time-injection-record-dto-example
- key_count: 8
  name: Cam Qa Cert Cycle Time Summary Dto Example
  slug: cam-qa-cert-cycle-time-summary-dto-example
- key_count: 23
  name: Cam Qa Cert Flow Rata Run Dto Example
  slug: cam-qa-cert-flow-rata-run-dto-example
- key_count: 16
  name: Cam Qa Cert Flow To Load Check Dto Example
  slug: cam-qa-cert-flow-to-load-check-dto-example
- key_count: 16
  name: Cam Qa Cert Flow To Load Check Record Dto Example
  slug: cam-qa-cert-flow-to-load-check-record-dto-example
- key_count: 17
  name: Cam Qa Cert Flow To Load Reference Dto Example
  slug: cam-qa-cert-flow-to-load-reference-dto-example
- key_count: 17
  name: Cam Qa Cert Flow To Load Reference Record Dto Example
  slug: cam-qa-cert-flow-to-load-reference-record-dto-example
- key_count: 17
  name: Cam Qa Cert Fuel Flow To Load Baseline Dto Example
  slug: cam-qa-cert-fuel-flow-to-load-baseline-dto-example
- key_count: 11
  name: Cam Qa Cert Fuel Flow To Load Test Dto Example
  slug: cam-qa-cert-fuel-flow-to-load-test-dto-example
- key_count: 11
  name: Cam Qa Cert Fuel Flowmeter Accuracy Dto Example
  slug: cam-qa-cert-fuel-flowmeter-accuracy-dto-example
- key_count: 11
  name: Cam Qa Cert Fuel Flowmeter Accuracy Record Dto Example
  slug: cam-qa-cert-fuel-flowmeter-accuracy-record-dto-example
- key_count: 10
  name: Cam Qa Cert Hg Injection Dto Example
  slug: cam-qa-cert-hg-injection-dto-example
- key_count: 10
  name: Cam Qa Cert Hg Injection Record Dto Example
  slug: cam-qa-cert-hg-injection-record-dto-example
- key_count: 15
  name: Cam Qa Cert Hg Summary Dto Example
  slug: cam-qa-cert-hg-summary-dto-example
- key_count: 10
  name: Cam Qa Cert Linearity Injection Dto Example
  slug: cam-qa-cert-linearity-injection-dto-example
- key_count: 10
  name: Cam Qa Cert Linearity Injection Record Dto Example
  slug: cam-qa-cert-linearity-injection-record-dto-example
- key_count: 15
  name: Cam Qa Cert Linearity Summary Dto Example
  slug: cam-qa-cert-linearity-summary-dto-example
- key_count: 14
  name: Cam Qa Cert Linearity Summary Record Dto Example
  slug: cam-qa-cert-linearity-summary-record-dto-example
- key_count: 30
  name: Cam Qa Cert Online Offline Calibration Dto Example
  slug: cam-qa-cert-online-offline-calibration-dto-example
- key_count: 30
  name: Cam Qa Cert Online Offline Calibration Record Dto Example
  slug: cam-qa-cert-online-offline-calibration-record-dto-example
- key_count: 10
  name: Cam Qa Cert Protocol Gas Dto Example
  slug: cam-qa-cert-protocol-gas-dto-example
- key_count: 10
  name: Cam Qa Cert Protocol Gas Record Dto Example
  slug: cam-qa-cert-protocol-gas-record-dto-example
- key_count: 4
  name: Cam Qa Cert Qacertification Dto Example
  slug: cam-qa-cert-qacertification-dto-example
- key_count: 28
  name: Cam Qa Cert Qacertification Event Dto Example
  slug: cam-qa-cert-qacertification-event-dto-example
- key_count: 14
  name: Cam Qa Cert Rata Dto Example
  slug: cam-qa-cert-rata-dto-example
- key_count: 13
  name: Cam Qa Cert Rata Record Dto Example
  slug: cam-qa-cert-rata-record-dto-example
- key_count: 18
  name: Cam Qa Cert Rata Run Dto Example
  slug: cam-qa-cert-rata-run-dto-example
- key_count: 37
  name: Cam Qa Cert Rata Summary Dto Example
  slug: cam-qa-cert-rata-summary-dto-example
- key_count: 36
  name: Cam Qa Cert Rata Summary Record Dto Example
  slug: cam-qa-cert-rata-summary-record-dto-example
- key_count: 21
  name: Cam Qa Cert Rata Traverse Dto Example
  slug: cam-qa-cert-rata-traverse-dto-example
- key_count: 21
  name: Cam Qa Cert Rata Traverse Record Dto Example
  slug: cam-qa-cert-rata-traverse-record-dto-example
- key_count: 19
  name: Cam Qa Cert Review And Submit Test Summary Dto Example
  slug: cam-qa-cert-review-and-submit-test-summary-dto-example
- key_count: 21
  name: Cam Qa Cert Tee Review And Submit Dto Example
  slug: cam-qa-cert-tee-review-and-submit-dto-example
- key_count: 23
  name: Cam Qa Cert Test Extension Exemption Dto Example
  slug: cam-qa-cert-test-extension-exemption-dto-example
- key_count: 23
  name: Cam Qa Cert Test Extension Exemption Record Dto Example
  slug: cam-qa-cert-test-extension-exemption-record-dto-example
- key_count: 11
  name: Cam Qa Cert Test Qualification Dto Example
  slug: cam-qa-cert-test-qualification-dto-example
- key_count: 11
  name: Cam Qa Cert Test Qualification Record Dto Example
  slug: cam-qa-cert-test-qualification-record-dto-example
- key_count: 51
  name: Cam Qa Cert Test Summary Dto Example
  slug: cam-qa-cert-test-summary-dto-example
- key_count: 34
  name: Cam Qa Cert Test Summary Record Dto Example
  slug: cam-qa-cert-test-summary-record-dto-example
- key_count: 11
  name: Cam Qa Cert Transmitter Transducer Accuracy Dto Example
  slug: cam-qa-cert-transmitter-transducer-accuracy-dto-example
- key_count: 13
  name: Cam Qa Cert Unit Default Test Dto Example
  slug: cam-qa-cert-unit-default-test-dto-example
- key_count: 12
  name: Cam Qa Cert Unit Default Test Record Dto Example
  slug: cam-qa-cert-unit-default-test-record-dto-example
- key_count: 16
  name: Cam Qa Cert Unit Default Test Run Dto Example
  slug: cam-qa-cert-unit-default-test-run-dto-example
- key_count: 16
  name: Cam Qa Cert Unit Default Test Run Record Dto Example
  slug: cam-qa-cert-unit-default-test-run-record-dto-example
- key_count: 10
  name: Cam Streaming Account Attributes Dto Example
  slug: cam-streaming-account-attributes-dto-example
- key_count: 22
  name: Cam Streaming Allowance Compliance Dto Example
  slug: cam-streaming-allowance-compliance-dto-example
- key_count: 12
  name: Cam Streaming Allowance Holdings Dto Example
  slug: cam-streaming-allowance-holdings-dto-example
- key_count: 27
  name: Cam Streaming Allowance Transactions Dto Example
  slug: cam-streaming-allowance-transactions-dto-example
- key_count: 7
  name: Cam Streaming Annual Apportioned Emissions Aggregation Dto Example
  slug: cam-streaming-annual-apportioned-emissions-aggregation-dto-example
- key_count: 29
  name: Cam Streaming Annual Apportioned Emissions Dto Example
  slug: cam-streaming-annual-apportioned-emissions-dto-example
- key_count: 10
  name: Cam Streaming Annual Apportioned Emissions Facility Aggregation Dto Example
  slug: cam-streaming-annual-apportioned-emissions-facility-aggregation-dto-example
- key_count: 8
  name: Cam Streaming Annual Apportioned Emissions State Aggregation Dto Example
  slug: cam-streaming-annual-apportioned-emissions-state-aggregation-dto-example
- key_count: 27
  name: Cam Streaming Daily Apportioned Emissions Dto Example
  slug: cam-streaming-daily-apportioned-emissions-dto-example
- key_count: 10
  name: Cam Streaming Daily Apportioned Emissions Facility Aggregation Dto Example
  slug: cam-streaming-daily-apportioned-emissions-facility-aggregation-dto-example
- key_count: 7
  name: Cam Streaming Daily Apportioned Emissions National Aggregation Dto Example
  slug: cam-streaming-daily-apportioned-emissions-national-aggregation-dto-example
- key_count: 8
  name: Cam Streaming Daily Apportioned Emissions State Aggregation Dto Example
  slug: cam-streaming-daily-apportioned-emissions-state-aggregation-dto-example
- key_count: 10
  name: Cam Streaming Derived Hourly Value Base Dto Example
  slug: cam-streaming-derived-hourly-value-base-dto-example
- key_count: 12
  name: Cam Streaming Emissions Compliance Dto Example
  slug: cam-streaming-emissions-compliance-dto-example
- key_count: 30
  name: Cam Streaming Facility Attributes Dto Example
  slug: cam-streaming-facility-attributes-dto-example
- key_count: 34
  name: Cam Streaming Hourly Apportioned Emissions Dto Example
  slug: cam-streaming-hourly-apportioned-emissions-dto-example
- key_count: 11
  name: Cam Streaming Hourly Apportioned Emissions Facility Aggregation Dto Example
  slug: cam-streaming-hourly-apportioned-emissions-facility-aggregation-dto-example
- key_count: 8
  name: Cam Streaming Hourly Apportioned Emissions National Aggregation Dto Example
  slug: cam-streaming-hourly-apportioned-emissions-national-aggregation-dto-example
- key_count: 9
  name: Cam Streaming Hourly Apportioned Emissions State Aggregation Dto Example
  slug: cam-streaming-hourly-apportioned-emissions-state-aggregation-dto-example
- key_count: 31
  name: Cam Streaming Hourly Mats Apportioned Emissions Dto Example
  slug: cam-streaming-hourly-mats-apportioned-emissions-dto-example
- key_count: 11
  name: Cam Streaming Hourly Operating Dto Example
  slug: cam-streaming-hourly-operating-dto-example
- key_count: 28
  name: Cam Streaming Monthly Apportioned Emissions Dto Example
  slug: cam-streaming-monthly-apportioned-emissions-dto-example
- key_count: 11
  name: Cam Streaming Monthly Apportioned Emissions Facility Aggregation Dto Example
  slug: cam-streaming-monthly-apportioned-emissions-facility-aggregation-dto-example
- key_count: 8
  name: Cam Streaming Monthly Apportioned Emissions National Aggregation Dto Example
  slug: cam-streaming-monthly-apportioned-emissions-national-aggregation-dto-example
- key_count: 9
  name: Cam Streaming Monthly Apportioned Emissions State Aggregation Dto Example
  slug: cam-streaming-monthly-apportioned-emissions-state-aggregation-dto-example
- key_count: 29
  name: Cam Streaming Ozone Apportioned Emissions Dto Example
  slug: cam-streaming-ozone-apportioned-emissions-dto-example
- key_count: 10
  name: Cam Streaming Ozone Apportioned Emissions Facility Aggregation Dto Example
  slug: cam-streaming-ozone-apportioned-emissions-facility-aggregation-dto-example
- key_count: 7
  name: Cam Streaming Ozone Apportioned Emissions National Aggregation Dto Example
  slug: cam-streaming-ozone-apportioned-emissions-national-aggregation-dto-example
- key_count: 8
  name: Cam Streaming Ozone Apportioned Emissions State Aggregation Dto Example
  slug: cam-streaming-ozone-apportioned-emissions-state-aggregation-dto-example
- key_count: 28
  name: Cam Streaming Quarterly Apportioned Emissions Dto Example
  slug: cam-streaming-quarterly-apportioned-emissions-dto-example
- key_count: 11
  name: Cam Streaming Quarterly Apportioned Emissions Facility Aggregation Dto Example
  slug: cam-streaming-quarterly-apportioned-emissions-facility-aggregation-dto-example
- key_count: 8
  name: Cam Streaming Quarterly Apportioned Emissions National Aggregation Dto Example
  slug: cam-streaming-quarterly-apportioned-emissions-national-aggregation-dto-example
- key_count: 9
  name: Cam Streaming Quarterly Apportioned Emissions State Aggregation Dto Example
  slug: cam-streaming-quarterly-apportioned-emissions-state-aggregation-dto-example
- key_count: 10
  name: Cam Streaming Summary Value Base Dto Example
  slug: cam-streaming-summary-value-base-dto-example
- key_count: 9
  name: Cam Streaming Supplemental Operating Dto Example
  slug: cam-streaming-supplemental-operating-dto-example
- key_count: 2
  name: Cip Service Cipsrv Domains Example
  slug: cip-service-cipsrv-domains-example
- key_count: 3
  name: Cip Service Cipsrv Domains State Example
  slug: cip-service-cipsrv-domains-state-example
- key_count: 4
  name: Cip Service Cipsrv Domains Tribe Example
  slug: cip-service-cipsrv-domains-tribe-example
- key_count: 29
  name: Cip Service Cipsrv Index Rb Example
  slug: cip-service-cipsrv-index-rb-example
- key_count: 13
  name: Cip Service Cipsrv Index Resp Example
  slug: cip-service-cipsrv-index-resp-example
- key_count: 6
  name: Cip Service Cipsrv Registry Components Example
  slug: cip-service-cipsrv-registry-components-example
- key_count: 4
  name: Cip Service Cipsrv Registry Example
  slug: cip-service-cipsrv-registry-example
- key_count: 20
  name: Cip Service Delineate Rb Example
  slug: cip-service-delineate-rb-example
- key_count: 7
  name: Cip Service Delineate Resp Example
  slug: cip-service-delineate-resp-example
- key_count: 4
  name: Cip Service Delineated Area Properties Example
  slug: cip-service-delineated-area-properties-example
- key_count: 3
  name: Cip Service End Point Properties Example
  slug: cip-service-end-point-properties-example
- key_count: 8
  name: Cip Service Event Feature Properties Example
  slug: cip-service-event-feature-properties-example
- key_count: 6
  name: Cip Service Flow Accumulation Rb Example
  slug: cip-service-flow-accumulation-rb-example
- key_count: 11
  name: Cip Service Flow Accumulation Resp Example
  slug: cip-service-flow-accumulation-resp-example
- key_count: 5
  name: Cip Service Geojson Feature Example
  slug: cip-service-geojson-feature-example
- key_count: 2
  name: Cip Service Geojson Featurecollection Example
  slug: cip-service-geojson-featurecollection-example
- key_count: 2
  name: Cip Service Geojson Geometry Example
  slug: cip-service-geojson-geometry-example
- key_count: 4
  name: Cip Service Indexed Catchment Properties Example
  slug: cip-service-indexed-catchment-properties-example
- key_count: 6
  name: Cip Service Indexed Flowline Properties Example
  slug: cip-service-indexed-flowline-properties-example
- key_count: 1
  name: Cip Service Indexing Line Properties Example
  slug: cip-service-indexing-line-properties-example
- key_count: 1
  name: Cip Service Indexing Summary Example
  slug: cip-service-indexing-summary-example
- key_count: 41
  name: Cip Service Linked Data Wqp Example
  slug: cip-service-linked-data-wqp-example
- key_count: 17
  name: Cip Service Navigate Rb Example
  slug: cip-service-navigate-rb-example
- key_count: 5
  name: Cip Service Navigate Resp Example
  slug: cip-service-navigate-resp-example
- key_count: 20
  name: Cip Service Navigated Flowline Properties Example
  slug: cip-service-navigated-flowline-properties-example
- key_count: 13
  name: Cip Service Pointindexing Rb Example
  slug: cip-service-pointindexing-rb-example
- key_count: 11
  name: Cip Service Pointindexing Resp Example
  slug: cip-service-pointindexing-resp-example
- key_count: 1
  name: Cip Service Randomcatchment Rb Example
  slug: cip-service-randomcatchment-rb-example
- key_count: 1
  name: Cip Service Randomcatchment Resp Example
  slug: cip-service-randomcatchment-resp-example
- key_count: 1
  name: Cip Service Randomhuc12 Rb Example
  slug: cip-service-randomhuc12-rb-example
- key_count: 1
  name: Cip Service Randomhuc12 Resp Example
  slug: cip-service-randomhuc12-resp-example
- key_count: 1
  name: Cip Service Randomnav Rb Example
  slug: cip-service-randomnav-rb-example
- key_count: 1
  name: Cip Service Randomnav Resp Example
  slug: cip-service-randomnav-resp-example
- key_count: 1
  name: Cip Service Randompoint Rb Example
  slug: cip-service-randompoint-rb-example
- key_count: 1
  name: Cip Service Randompoint Resp Example
  slug: cip-service-randompoint-resp-example
- key_count: 1
  name: Cip Service Randomppnav Rb Example
  slug: cip-service-randomppnav-rb-example
- key_count: 2
  name: Cip Service Randomppnav Resp Example
  slug: cip-service-randomppnav-resp-example
- key_count: 49
  name: Cip Service Upstreamdownstream Rb Example
  slug: cip-service-upstreamdownstream-rb-example
- key_count: 27
  name: Cip Service Upstreamdownstream Resp Example
  slug: cip-service-upstreamdownstream-resp-example
- key_count: 3
  name: Csb Rebate Formio Schema And Submission Example
  slug: csb-rebate-formio-schema-and-submission-example
- key_count: 17
  name: Echo Air Air00 Example
  slug: echo-air-air00-example
- key_count: 1
  name: Echo Air Air01 Example
  slug: echo-air-air01-example
- key_count: 10
  name: Echo Air Air02 Example
  slug: echo-air-air02-example
- key_count: 143
  name: Echo Air Air03 Example
  slug: echo-air-air03-example
- key_count: 4
  name: Echo Air Air04 Example
  slug: echo-air-air04-example
- key_count: 15
  name: Echo Air Air05 Example
  slug: echo-air-air05-example
- key_count: 144
  name: Echo Air Air06 Example
  slug: echo-air-air06-example
- key_count: 19
  name: Echo Air Air08 Example
  slug: echo-air-air08-example
- key_count: 3
  name: Echo Air Air09 Example
  slug: echo-air-air09-example
- key_count: 141
  name: Echo Air Air10 Example
  slug: echo-air-air10-example
- key_count: 4
  name: Echo Air Air11 Example
  slug: echo-air-air11-example
- key_count: 5
  name: Echo Air Air12 Example
  slug: echo-air-air12-example
- key_count: 2
  name: Echo Air Geo Example
  slug: echo-air-geo-example
- key_count: 2
  name: Echo Air Meta1 Example
  slug: echo-air-meta1-example
- key_count: 6
  name: Echo Air Meta3 Example
  slug: echo-air-meta3-example
- key_count: 2
  name: Echo Air Qp0 Example
  slug: echo-air-qp0-example
- key_count: 13
  name: Echo All Echo01 Example
  slug: echo-all-echo01-example
- key_count: 4
  name: Echo All Echo02 Example
  slug: echo-all-echo02-example
- key_count: 193
  name: Echo All Echo03 Example
  slug: echo-all-echo03-example
- key_count: 20
  name: Echo All Echo04 Example
  slug: echo-all-echo04-example
- key_count: 17
  name: Echo All Echo05 Example
  slug: echo-all-echo05-example
- key_count: 1
  name: Echo All Echo06 Example
  slug: echo-all-echo06-example
- key_count: 194
  name: Echo All Echo07 Example
  slug: echo-all-echo07-example
- key_count: 23
  name: Echo All Echo08 Example
  slug: echo-all-echo08-example
- key_count: 3
  name: Echo All Echo09 Example
  slug: echo-all-echo09-example
- key_count: 191
  name: Echo All Echo10 Example
  slug: echo-all-echo10-example
- key_count: 5
  name: Echo All Echo11 Example
  slug: echo-all-echo11-example
- key_count: 2
  name: Echo All Geo Example
  slug: echo-all-geo-example
- key_count: 2
  name: Echo All Meta1 Example
  slug: echo-all-meta1-example
- key_count: 6
  name: Echo All Meta3 Example
  slug: echo-all-meta3-example
- key_count: 2
  name: Echo All Qp0 Example
  slug: echo-all-qp0-example
- key_count: 40
  name: Echo Case Crs0 Cases Example
  slug: echo-case-crs0-cases-example
- key_count: 22
  name: Echo Case Crs0 Cluster Data Example
  slug: echo-case-crs0-cluster-data-example
- key_count: 1
  name: Echo Case Crs0 Cluster Output Example
  slug: echo-case-crs0-cluster-output-example
- key_count: 20
  name: Echo Case Crs0 Get Case Info.Results Example
  slug: echo-case-crs0-get-case-info.results-example
- key_count: 1
  name: Echo Case Crs0 Get Cases From Facility.Case Number Example
  slug: echo-case-crs0-get-cases-from-facility.case-number-example
- key_count: 1
  name: Echo Case Crs0 Get Cases From Facility.Case Numbers Example
  slug: echo-case-crs0-get-cases-from-facility.case-numbers-example
- key_count: 1
  name: Echo Case Crs0 Get Cases From Facility.Results Example
  slug: echo-case-crs0-get-cases-from-facility.results-example
- key_count: 1
  name: Echo Case Crs0 Get Facilities From Case.Registry Id Example
  slug: echo-case-crs0-get-facilities-from-case.registry-id-example
- key_count: 1
  name: Echo Case Crs0 Get Facilities From Case.Registry Ids Example
  slug: echo-case-crs0-get-facilities-from-case.registry-ids-example
- key_count: 1
  name: Echo Case Crs0 Get Facilities From Case.Results Example
  slug: echo-case-crs0-get-facilities-from-case.results-example
- key_count: 7
  name: Echo Case Crs0 Map Data Example
  slug: echo-case-crs0-map-data-example
- key_count: 4
  name: Echo Case Crs0 Map Output Example
  slug: echo-case-crs0-map-output-example
- key_count: 5
  name: Echo Case Crs1 Caeddocuments Example
  slug: echo-case-crs1-caeddocuments-example
- key_count: 22
  name: Echo Case Crs1 Case Information Example
  slug: echo-case-crs1-case-information-example
- key_count: 2
  name: Echo Case Crs1 Case Milestones Example
  slug: echo-case-crs1-case-milestones-example
- key_count: 3
  name: Echo Case Crs1 Citations Example
  slug: echo-case-crs1-citations-example
- key_count: 7
  name: Echo Case Crs1 Compliance Schedules Example
  slug: echo-case-crs1-compliance-schedules-example
- key_count: 4
  name: Echo Case Crs1 Complying Actions Example
  slug: echo-case-crs1-complying-actions-example
- key_count: 3
  name: Echo Case Crs1 Defendants Example
  slug: echo-case-crs1-defendants-example
- key_count: 18
  name: Echo Case Crs1 Enforcement Conclusions Example
  slug: echo-case-crs1-enforcement-conclusions-example
- key_count: 8
  name: Echo Case Crs1 Facilities Example
  slug: echo-case-crs1-facilities-example
- key_count: 5
  name: Echo Case Crs1 Final Order Statuses Example
  slug: echo-case-crs1-final-order-statuses-example
- key_count: 3
  name: Echo Case Crs1 Laws And Sections Example
  slug: echo-case-crs1-laws-and-sections-example
- key_count: 8
  name: Echo Case Crs1 Pollutant Reductions Example
  slug: echo-case-crs1-pollutant-reductions-example
- key_count: 2
  name: Echo Case Crs1 Pollutants Example
  slug: echo-case-crs1-pollutants-example
- key_count: 3
  name: Echo Case Crs1 Program Links Example
  slug: echo-case-crs1-program-links-example
- key_count: 2
  name: Echo Case Crs1 Related Activities Example
  slug: echo-case-crs1-related-activities-example
- key_count: 12
  name: Echo Case Crs1 Results Example
  slug: echo-case-crs1-results-example
- key_count: 5
  name: Echo Case Crs1 Supplemental Environmental Projects Example
  slug: echo-case-crs1-supplemental-environmental-projects-example
- key_count: 20
  name: Echo Case Crs2 Results Example
  slug: echo-case-crs2-results-example
- key_count: 5
  name: Echo Case Crs3 Case Information Example
  slug: echo-case-crs3-case-information-example
- key_count: 5
  name: Echo Case Crs3 Crdefendants Example
  slug: echo-case-crs3-crdefendants-example
- key_count: 3
  name: Echo Case Crs3 Crdetails Example
  slug: echo-case-crs3-crdetails-example
- key_count: 7
  name: Echo Case Crs3 Locations Example
  slug: echo-case-crs3-locations-example
- key_count: 5
  name: Echo Case Crs3 Results Example
  slug: echo-case-crs3-results-example
- key_count: 5
  name: Echo Case Crs5 Results Example
  slug: echo-case-crs5-results-example
- key_count: 2
  name: Echo Case Met1 Example
  slug: echo-case-met1-example
- key_count: 6
  name: Echo Case Met2 Example
  slug: echo-case-met2-example
- key_count: 2
  name: Echo Case Qp0 Example
  slug: echo-case-qp0-example
- key_count: 2
  name: Echo Case Rlk00 Lu Values Example
  slug: echo-case-rlk00-lu-values-example
- key_count: 2
  name: Echo Case Rlk51 Results Example
  slug: echo-case-rlk51-results-example
- key_count: 305
  name: Echo Cwa Cwa01 Example
  slug: echo-cwa-cwa01-example
- key_count: 10
  name: Echo Cwa Cwa02 Example
  slug: echo-cwa-cwa02-example
- key_count: 4
  name: Echo Cwa Cwa03 Example
  slug: echo-cwa-cwa03-example
- key_count: 19
  name: Echo Cwa Cwa04 Example
  slug: echo-cwa-cwa04-example
- key_count: 20
  name: Echo Cwa Cwa05 Example
  slug: echo-cwa-cwa05-example
- key_count: 1
  name: Echo Cwa Cwa06 Example
  slug: echo-cwa-cwa06-example
- key_count: 306
  name: Echo Cwa Cwa07 Example
  slug: echo-cwa-cwa07-example
- key_count: 22
  name: Echo Cwa Cwa08 Example
  slug: echo-cwa-cwa08-example
- key_count: 3
  name: Echo Cwa Cwa09 Example
  slug: echo-cwa-cwa09-example
- key_count: 303
  name: Echo Cwa Cwa10 Example
  slug: echo-cwa-cwa10-example
- key_count: 10
  name: Echo Cwa Cwa11 Example
  slug: echo-cwa-cwa11-example
- key_count: 4
  name: Echo Cwa Cwa12 Example
  slug: echo-cwa-cwa12-example
- key_count: 5
  name: Echo Cwa Cwa13 Example
  slug: echo-cwa-cwa13-example
- key_count: 2
  name: Echo Cwa Geo Example
  slug: echo-cwa-geo-example
- key_count: 2
  name: Echo Cwa Meta1 Example
  slug: echo-cwa-meta1-example
- key_count: 6
  name: Echo Cwa Meta3 Example
  slug: echo-cwa-meta3-example
- key_count: 2
  name: Echo Cwa Qp0 Example
  slug: echo-cwa-qp0-example
- key_count: 2
  name: Echo Cwa Rlup01 Example
  slug: echo-cwa-rlup01-example
- key_count: 2
  name: Echo Cwa Rlup20 Example
  slug: echo-cwa-rlup20-example
- key_count: 2
  name: Echo Cwa Rlup23 Example
  slug: echo-cwa-rlup23-example
- key_count: 2
  name: Echo Cwa Rlup24 Example
  slug: echo-cwa-rlup24-example
- key_count: 2
  name: Echo Cwa Rlup54 Example
  slug: echo-cwa-rlup54-example
- key_count: 2
  name: Echo Cwa Rlup58 Example
  slug: echo-cwa-rlup58-example
- key_count: 2
  name: Echo Cwa Rlup59 Example
  slug: echo-cwa-rlup59-example
- key_count: 2
  name: Echo Cwa Rlup61 Example
  slug: echo-cwa-rlup61-example
- key_count: 2
  name: Echo Cwa Rlup65 Example
  slug: echo-cwa-rlup65-example
- key_count: 2
  name: Echo Cwa Rlup75 Example
  slug: echo-cwa-rlup75-example
- key_count: 2
  name: Echo Cwa Rlup77 Example
  slug: echo-cwa-rlup77-example
- key_count: 1
  name: Echo Dfr Dfr0 Get Aws Docs.Results Example
  slug: echo-dfr-dfr0-get-aws-docs.results-example
- key_count: 2
  name: Echo Dfr Dfr0 Get Cwa Eff Alr Exp.Results Example
  slug: echo-dfr-dfr0-get-cwa-eff-alr-exp.results-example
- key_count: 2
  name: Echo Dfr Dfr0 Get Cwa Eff Compliance Exp.Results Example
  slug: echo-dfr-dfr0-get-cwa-eff-compliance-exp.results-example
- key_count: 1
  name: Echo Dfr Dfr0 Get D80D90S Details.D80 D90S Details Example
  slug: echo-dfr-dfr0-get-d80d90s-details.d80-d90s-details-example
- key_count: 29
  name: Echo Dfr Dfr0 Get D80D90S Details.D80 D90S Details.Sources Example
  slug: echo-dfr-dfr0-get-d80d90s-details.d80-d90s-details.sources-example
- key_count: 2
  name: Echo Dfr Dfr0 Get D80D90S Details.Results Example
  slug: echo-dfr-dfr0-get-d80d90s-details.results-example
- key_count: 2
  name: Echo Dfr Dfr0 Get Ejscreen Indexes.Results Example
  slug: echo-dfr-dfr0-get-ejscreen-indexes.results-example
- key_count: 96
  name: Echo Dfr Dfr0 Qtr12 Header Example
  slug: echo-dfr-dfr0-qtr12-header-example
- key_count: 102
  name: Echo Dfr Dfr0 Qtr12 Header39 Example
  slug: echo-dfr-dfr0-qtr12-header39-example
- key_count: 13
  name: Echo Dfr Dfr0 Qtr12 Status Example
  slug: echo-dfr-dfr0-qtr12-status-example
- key_count: 104
  name: Echo Dfr Dfr0 Qtr13 Header Example
  slug: echo-dfr-dfr0-qtr13-header-example
- key_count: 14
  name: Echo Dfr Dfr0 Qtr13 Status Example
  slug: echo-dfr-dfr0-qtr13-status-example
- key_count: 2
  name: Echo Dfr Dfr001 Results Example
  slug: echo-dfr-dfr001-results-example
- key_count: 2
  name: Echo Dfr Dfr002 Results Example
  slug: echo-dfr-dfr002-results-example
- key_count: 2
  name: Echo Dfr Dfr004 Example
  slug: echo-dfr-dfr004-example
- key_count: 2
  name: Echo Dfr Dfr005 Results Example
  slug: echo-dfr-dfr005-results-example
- key_count: 2
  name: Echo Dfr Dfr006 Results Example
  slug: echo-dfr-dfr006-results-example
- key_count: 2
  name: Echo Dfr Dfr007 Results Example
  slug: echo-dfr-dfr007-results-example
- key_count: 2
  name: Echo Dfr Dfr009 Results Example
  slug: echo-dfr-dfr009-results-example
- key_count: 2
  name: Echo Dfr Dfr010 Results Example
  slug: echo-dfr-dfr010-results-example
- key_count: 2
  name: Echo Dfr Dfr011 Results Example
  slug: echo-dfr-dfr011-results-example
- key_count: 2
  name: Echo Dfr Dfr012 Results Example
  slug: echo-dfr-dfr012-results-example
- key_count: 2
  name: Echo Dfr Dfr013 Results Example
  slug: echo-dfr-dfr013-results-example
- key_count: 2
  name: Echo Dfr Dfr014 Results Example
  slug: echo-dfr-dfr014-results-example
- key_count: 2
  name: Echo Dfr Dfr015 Results Example
  slug: echo-dfr-dfr015-results-example
- key_count: 2
  name: Echo Dfr Dfr017 Results Example
  slug: echo-dfr-dfr017-results-example
- key_count: 5
  name: Echo Dfr Dfr018 Caeddocuments Example
  slug: echo-dfr-dfr018-caeddocuments-example
- key_count: 13
  name: Echo Dfr Dfr018 Ejscreen Indexes Example
  slug: echo-dfr-dfr018-ejscreen-indexes-example
- key_count: 6
  name: Echo Dfr Dfr018 Map Data Example
  slug: echo-dfr-dfr018-map-data-example
- key_count: 1
  name: Echo Dfr Dfr018 Multiple Frsfacilities Example
  slug: echo-dfr-dfr018-multiple-frsfacilities-example
- key_count: 1
  name: Echo Dfr Dfr018 Naics Example
  slug: echo-dfr-dfr018-naics-example
- key_count: 27
  name: Echo Dfr Dfr018 Permits Example
  slug: echo-dfr-dfr018-permits-example
- key_count: 3
  name: Echo Dfr Dfr018 Program Dates Example
  slug: echo-dfr-dfr018-program-dates-example
- key_count: 8
  name: Echo Dfr Dfr018 Registry Ids Example
  slug: echo-dfr-dfr018-registry-ids-example
- key_count: 1
  name: Echo Dfr Dfr018 Reports Example
  slug: echo-dfr-dfr018-reports-example
- key_count: 44
  name: Echo Dfr Dfr018 Results Example
  slug: echo-dfr-dfr018-results-example
- key_count: 11
  name: Echo Dfr Dfr018 Summaries Example
  slug: echo-dfr-dfr018-summaries-example
- key_count: 7
  name: Echo Dfr Dfr018 Web Fire Documents Example
  slug: echo-dfr-dfr018-web-fire-documents-example
- key_count: 2
  name: Echo Dfr Dfr019 Example
  slug: echo-dfr-dfr019-example
- key_count: 49
  name: Echo Dfr Dfr020 .Hpvhistory Example
  slug: echo-dfr-dfr020-.hpvhistory-example
- key_count: 49
  name: Echo Dfr Dfr020 .Permit History Example
  slug: echo-dfr-dfr020-.permit-history-example
- key_count: 5
  name: Echo Dfr Dfr020 Example
  slug: echo-dfr-dfr020-example
- key_count: 14
  name: Echo Dfr Dfr021 Example
  slug: echo-dfr-dfr021-example
- key_count: 53
  name: Echo Dfr Dfr022 Example
  slug: echo-dfr-dfr022-example
- key_count: 53
  name: Echo Dfr Dfr023 Example
  slug: echo-dfr-dfr023-example
- key_count: 13
  name: Echo Dfr Dfr024 Example
  slug: echo-dfr-dfr024-example
- key_count: 2
  name: Echo Dfr Dfr025 Example
  slug: echo-dfr-dfr025-example
- key_count: 1
  name: Echo Dfr Dfr026 Example
  slug: echo-dfr-dfr026-example
- key_count: 2
  name: Echo Dfr Dfr027 Example
  slug: echo-dfr-dfr027-example
- key_count: 1
  name: Echo Dfr Dfr029 Example
  slug: echo-dfr-dfr029-example
- key_count: 54
  name: Echo Dfr Dfr030 Example
  slug: echo-dfr-dfr030-example
- key_count: 2
  name: Echo Dfr Dfr031 Example
  slug: echo-dfr-dfr031-example
- key_count: 1
  name: Echo Dfr Dfr032 Example
  slug: echo-dfr-dfr032-example
- key_count: 107
  name: Echo Dfr Dfr034 Example
  slug: echo-dfr-dfr034-example
- key_count: 2
  name: Echo Dfr Dfr035 Example
  slug: echo-dfr-dfr035-example
- key_count: 2
  name: Echo Dfr Dfr035 Exp Example
  slug: echo-dfr-dfr035-exp-example
- key_count: 58
  name: Echo Dfr Dfr035 Exp.Parameters Example
  slug: echo-dfr-dfr035-exp.parameters-example
- key_count: 1
  name: Echo Dfr Dfr035 Exp.Sources Example
  slug: echo-dfr-dfr035-exp.sources-example
- key_count: 57
  name: Echo Dfr Dfr036 Example
  slug: echo-dfr-dfr036-example
- key_count: 1
  name: Echo Dfr Dfr037 Example
  slug: echo-dfr-dfr037-example
- key_count: 2
  name: Echo Dfr Dfr038 Example
  slug: echo-dfr-dfr038-example
- key_count: 2
  name: Echo Dfr Dfr038 Exp Example
  slug: echo-dfr-dfr038-exp-example
- key_count: 110
  name: Echo Dfr Dfr038 Exp.Parameters Example
  slug: echo-dfr-dfr038-exp.parameters-example
- key_count: 1
  name: Echo Dfr Dfr038 Exp.Sources Example
  slug: echo-dfr-dfr038-exp.sources-example
- key_count: 109
  name: Echo Dfr Dfr040 Example
  slug: echo-dfr-dfr040-example
- key_count: 1
  name: Echo Dfr Dfr041 Example
  slug: echo-dfr-dfr041-example
- key_count: 2
  name: Echo Dfr Dfr042 Example
  slug: echo-dfr-dfr042-example
- key_count: 1
  name: Echo Dfr Dfr043 Example
  slug: echo-dfr-dfr043-example
- key_count: 107
  name: Echo Dfr Dfr045 Example
  slug: echo-dfr-dfr045-example
- key_count: 2
  name: Echo Dfr Dfr046 Example
  slug: echo-dfr-dfr046-example
- key_count: 1
  name: Echo Dfr Dfr047 .Status Example
  slug: echo-dfr-dfr047-.status-example
- key_count: 2
  name: Echo Dfr Dfr049 Example
  slug: echo-dfr-dfr049-example
- key_count: 1
  name: Echo Dfr Dfr050 Example
  slug: echo-dfr-dfr050-example
- key_count: 108
  name: Echo Dfr Dfr051 Example
  slug: echo-dfr-dfr051-example
- key_count: 2
  name: Echo Dfr Dfr052 Example
  slug: echo-dfr-dfr052-example
- key_count: 13
  name: Echo Dfr Dfr053 Example
  slug: echo-dfr-dfr053-example
- key_count: 6
  name: Echo Dfr Dfr054 Example
  slug: echo-dfr-dfr054-example
- key_count: 1
  name: Echo Dfr Dfr055 Example
  slug: echo-dfr-dfr055-example
- key_count: 2
  name: Echo Dfr Dfr057 Example
  slug: echo-dfr-dfr057-example
- key_count: 10
  name: Echo Dfr Dfr058 Example
  slug: echo-dfr-dfr058-example
- key_count: 2
  name: Echo Dfr Dfr059 Example
  slug: echo-dfr-dfr059-example
- key_count: 6
  name: Echo Dfr Dfr060 Example
  slug: echo-dfr-dfr060-example
- key_count: 32
  name: Echo Dfr Dfr061 Example
  slug: echo-dfr-dfr061-example
- key_count: 2
  name: Echo Dfr Dfr062 Example
  slug: echo-dfr-dfr062-example
- key_count: 4
  name: Echo Dfr Dfr063 S Example
  slug: echo-dfr-dfr063-s-example
- key_count: 2
  name: Echo Dfr Dfr064 Example
  slug: echo-dfr-dfr064-example
- key_count: 7
  name: Echo Dfr Dfr065 Example
  slug: echo-dfr-dfr065-example
- key_count: 2
  name: Echo Dfr Dfr066 Example
  slug: echo-dfr-dfr066-example
- key_count: 16
  name: Echo Dfr Dfr067 Example
  slug: echo-dfr-dfr067-example
- key_count: 2
  name: Echo Dfr Dfr068 Example
  slug: echo-dfr-dfr068-example
- key_count: 7
  name: Echo Dfr Dfr069 Example
  slug: echo-dfr-dfr069-example
- key_count: 18
  name: Echo Dfr Dfr070 Example
  slug: echo-dfr-dfr070-example
- key_count: 4
  name: Echo Dfr Dfr071 Example
  slug: echo-dfr-dfr071-example
- key_count: 4
  name: Echo Dfr Dfr072 Example
  slug: echo-dfr-dfr072-example
- key_count: 5
  name: Echo Dfr Dfr073 Example
  slug: echo-dfr-dfr073-example
- key_count: 1
  name: Echo Dfr Dfr074 Example
  slug: echo-dfr-dfr074-example
- key_count: 4
  name: Echo Dfr Dfr075 Example
  slug: echo-dfr-dfr075-example
- key_count: 2
  name: Echo Dfr Dfr076 Example
  slug: echo-dfr-dfr076-example
- key_count: 7
  name: Echo Dfr Dfr077 Example
  slug: echo-dfr-dfr077-example
- key_count: 97
  name: Echo Dfr Dfr078 Example
  slug: echo-dfr-dfr078-example
- key_count: 3
  name: Echo Dfr Dfr079 S Example
  slug: echo-dfr-dfr079-s-example
- key_count: 52
  name: Echo Dfr Dfr079 S.Evaluations Example
  slug: echo-dfr-dfr079-s.evaluations-example
- key_count: 49
  name: Echo Dfr Dfr079 S.Status Example
  slug: echo-dfr-dfr079-s.status-example
- key_count: 52
  name: Echo Dfr Dfr079 S.Violations Example
  slug: echo-dfr-dfr079-s.violations-example
- key_count: 105
  name: Echo Dfr Dfr081 Example
  slug: echo-dfr-dfr081-example
- key_count: 2
  name: Echo Dfr Dfr083 S Example
  slug: echo-dfr-dfr083-s-example
- key_count: 15
  name: Echo Dfr Dfr083 S.Rules Violated Example
  slug: echo-dfr-dfr083-s.rules-violated-example
- key_count: 4
  name: Echo Dfr Dfr084 Codes Example
  slug: echo-dfr-dfr084-codes-example
- key_count: 1
  name: Echo Dfr Dfr084 Example
  slug: echo-dfr-dfr084-example
- key_count: 1
  name: Echo Dfr Dfr085 Example
  slug: echo-dfr-dfr085-example
- key_count: 1
  name: Echo Dfr Dfr086 Example
  slug: echo-dfr-dfr086-example
- key_count: 1
  name: Echo Dfr Dfr088 Example
  slug: echo-dfr-dfr088-example
- key_count: 15
  name: Echo Dfr Dfr089 Example
  slug: echo-dfr-dfr089-example
- key_count: 1
  name: Echo Dfr Dfr090 Example
  slug: echo-dfr-dfr090-example
- key_count: 1
  name: Echo Dfr Dfr092 Example
  slug: echo-dfr-dfr092-example
- key_count: 15
  name: Echo Dfr Dfr093 Example
  slug: echo-dfr-dfr093-example
- key_count: 8
  name: Echo Dfr Dfr094 Example
  slug: echo-dfr-dfr094-example
- key_count: 1
  name: Echo Dfr Dfr095 Example
  slug: echo-dfr-dfr095-example
- key_count: 2
  name: Echo Dfr Dfr096 Example
  slug: echo-dfr-dfr096-example
- key_count: 1
  name: Echo Dfr Dfr098 Example
  slug: echo-dfr-dfr098-example
- key_count: 1
  name: Echo Dfr Dfr100 Example
  slug: echo-dfr-dfr100-example
- key_count: 10
  name: Echo Dfr Dfr101 Example
  slug: echo-dfr-dfr101-example
- key_count: 2
  name: Echo Dfr Dfr102 Example
  slug: echo-dfr-dfr102-example
- key_count: 10
  name: Echo Dfr Dfr103 Example
  slug: echo-dfr-dfr103-example
- key_count: 9
  name: Echo Dfr Dfr104 Example
  slug: echo-dfr-dfr104-example
- key_count: 4
  name: Echo Dfr Dfr105 Example
  slug: echo-dfr-dfr105-example
- key_count: 1
  name: Echo Dfr Dfr106 Example
  slug: echo-dfr-dfr106-example
- key_count: 1
  name: Echo Dfr Dfr108 Example
  slug: echo-dfr-dfr108-example
- key_count: 5
  name: Echo Dfr Dfr109 Example
  slug: echo-dfr-dfr109-example
- key_count: 14
  name: Echo Dfr Dfr110 Example
  slug: echo-dfr-dfr110-example
- key_count: 1
  name: Echo Dfr Dfr111 Details Example
  slug: echo-dfr-dfr111-details-example
- key_count: 16
  name: Echo Dfr Dfr111 Details.Sources Example
  slug: echo-dfr-dfr111-details.sources-example
- key_count: 1
  name: Echo Dfr Dfr111 Example
  slug: echo-dfr-dfr111-example
- key_count: 21
  name: Echo Dfr Dfr112 Example
  slug: echo-dfr-dfr112-example
- key_count: 2
  name: Echo Dfr Dfr114 Results Example
  slug: echo-dfr-dfr114-results-example
- key_count: 2
  name: Echo Dfr Dfr115 Example
  slug: echo-dfr-dfr115-example
- key_count: 2
  name: Echo Dfr Dfr116 Results Example
  slug: echo-dfr-dfr116-results-example
- key_count: 2
  name: Echo Dfr Dfr117 Results Example
  slug: echo-dfr-dfr117-results-example
- key_count: 2
  name: Echo Dfr Dfr118 Results Example
  slug: echo-dfr-dfr118-results-example
- key_count: 2
  name: Echo Dfr Dfr119 Results Example
  slug: echo-dfr-dfr119-results-example
- key_count: 2
  name: Echo Dfr Dfr120 Results Example
  slug: echo-dfr-dfr120-results-example
- key_count: 2
  name: Echo Dfr Dfr122 Results Example
  slug: echo-dfr-dfr122-results-example
- key_count: 3
  name: Echo Dfr Dfr123 Results Example
  slug: echo-dfr-dfr123-results-example
- key_count: 2
  name: Echo Dfr Dfr124 Results Example
  slug: echo-dfr-dfr124-results-example
- key_count: 2
  name: Echo Dfr Dfr125 Results Example
  slug: echo-dfr-dfr125-results-example
- key_count: 2
  name: Echo Dfr Dfr126 Results Example
  slug: echo-dfr-dfr126-results-example
- key_count: 2
  name: Echo Dfr Dfr127 Results Example
  slug: echo-dfr-dfr127-results-example
- key_count: 2
  name: Echo Dfr Dfr128 Results Example
  slug: echo-dfr-dfr128-results-example
- key_count: 2
  name: Echo Dfr Dfr129 Results Example
  slug: echo-dfr-dfr129-results-example
- key_count: 2
  name: Echo Dfr Dfr130 Results Example
  slug: echo-dfr-dfr130-results-example
- key_count: 2
  name: Echo Dfr Dfr131 Results Example
  slug: echo-dfr-dfr131-results-example
- key_count: 2
  name: Echo Dfr Dfr132 Results Example
  slug: echo-dfr-dfr132-results-example
- key_count: 2
  name: Echo Dfr Dfr133 Results Example
  slug: echo-dfr-dfr133-results-example
- key_count: 2
  name: Echo Dfr Dfr134 Results Example
  slug: echo-dfr-dfr134-results-example
- key_count: 2
  name: Echo Dfr Dfr135 Results Example
  slug: echo-dfr-dfr135-results-example
- key_count: 2
  name: Echo Dfr Dfr136 Results Example
  slug: echo-dfr-dfr136-results-example
- key_count: 41
  name: Echo Effluent Eff01 Example
  slug: echo-effluent-eff01-example
- key_count: 11
  name: Echo Effluent Eff02 Example
  slug: echo-effluent-eff02-example
- key_count: 7
  name: Echo Effluent Eff03 Example
  slug: echo-effluent-eff03-example
- key_count: 4
  name: Echo Effluent Eff04 Example
  slug: echo-effluent-eff04-example
- key_count: 17
  name: Echo Effluent Eff05 Example
  slug: echo-effluent-eff05-example
- key_count: 10
  name: Echo Effluent Eff06 Example
  slug: echo-effluent-eff06-example
- key_count: 4
  name: Echo Effluent Eff07 Example
  slug: echo-effluent-eff07-example
- key_count: 4
  name: Echo Effluent Eff08 Example
  slug: echo-effluent-eff08-example
- key_count: 18
  name: Echo Effluent Eff09 Example
  slug: echo-effluent-eff09-example
- key_count: 2
  name: Echo Effluent Rlup01 Example
  slug: echo-effluent-rlup01-example
- key_count: 2
  name: Echo Effluent Rlup23 Example
  slug: echo-effluent-rlup23-example
- key_count: 2
  name: Echo Rcra Geo Example
  slug: echo-rcra-geo-example
- key_count: 2
  name: Echo Rcra Meta1 Example
  slug: echo-rcra-meta1-example
- key_count: 6
  name: Echo Rcra Meta3 Example
  slug: echo-rcra-meta3-example
- key_count: 2
  name: Echo Rcra Qp0 Example
  slug: echo-rcra-qp0-example
- key_count: 119
  name: Echo Rcra Rcra01 Example
  slug: echo-rcra-rcra01-example
- key_count: 10
  name: Echo Rcra Rcra02 Example
  slug: echo-rcra-rcra02-example
- key_count: 4
  name: Echo Rcra Rcra03 Example
  slug: echo-rcra-rcra03-example
- key_count: 15
  name: Echo Rcra Rcra04 Example
  slug: echo-rcra-rcra04-example
- key_count: 17
  name: Echo Rcra Rcra05 Example
  slug: echo-rcra-rcra05-example
- key_count: 1
  name: Echo Rcra Rcra06 Example
  slug: echo-rcra-rcra06-example
- key_count: 120
  name: Echo Rcra Rcra07 Example
  slug: echo-rcra-rcra07-example
- key_count: 19
  name: Echo Rcra Rcra08 Example
  slug: echo-rcra-rcra08-example
- key_count: 3
  name: Echo Rcra Rcra09 Example
  slug: echo-rcra-rcra09-example
- key_count: 117
  name: Echo Rcra Rcra10 Example
  slug: echo-rcra-rcra10-example
- key_count: 10
  name: Echo Rcra Rcra11 Example
  slug: echo-rcra-rcra11-example
- key_count: 4
  name: Echo Rcra Rcra12 Example
  slug: echo-rcra-rcra12-example
- key_count: 5
  name: Echo Rcra Rcra13 Example
  slug: echo-rcra-rcra13-example
- key_count: 2
  name: Echo Sdw Meta1 Example
  slug: echo-sdw-meta1-example
- key_count: 6
  name: Echo Sdw Meta3 Example
  slug: echo-sdw-meta3-example
- key_count: 5
  name: Echo Sdw Sdw02 Example
  slug: echo-sdw-sdw02-example
- key_count: 14
  name: Echo Sdw Sdw03 Example
  slug: echo-sdw-sdw03-example
- key_count: 77
  name: Echo Sdw Sdw04 Example
  slug: echo-sdw-sdw04-example
- key_count: 1
  name: Elg Search Custom Search.Keyword Search Example
  slug: elg-search-custom-search.keyword-search-example
- key_count: 1
  name: Elg Search Custom Search.Multi Criteria Search Criteria Example
  slug: elg-search-custom-search.multi-criteria-search-criteria-example
- key_count: 1
  name: Elg Search Custom Search.Multi Criteria Search Example
  slug: elg-search-custom-search.multi-criteria-search-example
- key_count: 1
  name: Elg Search Glossary.Contact Example
  slug: elg-search-glossary.contact-example
- key_count: 1
  name: Elg Search Glossary.Help Example
  slug: elg-search-glossary.help-example
- key_count: 1
  name: Elg Search Glossary.List Example
  slug: elg-search-glossary.list-example
- key_count: 1
  name: Elg Search Limitation.Read Example
  slug: elg-search-limitation.read-example
- key_count: 1
  name: Elg Search Point Source Category.Cfr Example
  slug: elg-search-point-source-category.cfr-example
- key_count: 1
  name: Elg Search Point Source Category.Citation History Example
  slug: elg-search-point-source-category.citation-history-example
- key_count: 1
  name: Elg Search Point Source Category.Definitions Example
  slug: elg-search-point-source-category.definitions-example
- key_count: 1
  name: Elg Search Point Source Category.List Example
  slug: elg-search-point-source-category.list-example
- key_count: 1
  name: Elg Search Point Source Category.Read Example
  slug: elg-search-point-source-category.read-example
- key_count: 1
  name: Elg Search Point Source Subcategory.Read Example
  slug: elg-search-point-source-subcategory.read-example
- key_count: 1
  name: Elg Search Pollutant.Limitations Example
  slug: elg-search-pollutant.limitations-example
- key_count: 1
  name: Elg Search Pollutant.List Categories Example
  slug: elg-search-pollutant.list-categories-example
- key_count: 1
  name: Elg Search Pollutant.List Example
  slug: elg-search-pollutant.list-example
- key_count: 1
  name: Elg Search Pollutant.Read Category Example
  slug: elg-search-pollutant.read-category-example
- key_count: 1
  name: Elg Search Pollutant.Read Example
  slug: elg-search-pollutant.read-example
- key_count: 1
  name: Elg Search Treatment Technology.Category Limitations Example
  slug: elg-search-treatment-technology.category-limitations-example
- key_count: 1
  name: Elg Search Treatment Technology.Limitations Example
  slug: elg-search-treatment-technology.limitations-example
- key_count: 1
  name: Elg Search Treatment Technology.List Categories Example
  slug: elg-search-treatment-technology.list-categories-example
- key_count: 1
  name: Elg Search Treatment Technology.List Example
  slug: elg-search-treatment-technology.list-example
- key_count: 1
  name: Elg Search Treatment Technology.Read Category Example
  slug: elg-search-treatment-technology.read-category-example
- key_count: 1
  name: Elg Search Treatment Technology.Read Example
  slug: elg-search-treatment-technology.read-example
- key_count: 1
  name: Elg Search Wastestream Process.Limitations Example
  slug: elg-search-wastestream-process.limitations-example
- key_count: 0
  name: Envirofacts Row Example
  slug: envirofacts-row-example
- key_count: 5
  name: Envirofacts Uv Daily Example
  slug: envirofacts-uv-daily-example
- key_count: 5
  name: Envirofacts Uv Hourly Example
  slug: envirofacts-uv-hourly-example
- key_count: 1
  name: Mywaterway Generic Example
  slug: mywaterway-generic-example
features:
- description: Most public datasets and APIs are freely accessible without authentication.
  name: Open Government Data
- description: FRS and ECHO crosswalk facilities across CAA, CWA, RCRA, SDWA, and TRI.
  name: Cross-program Indexing
- description: Annual / quarterly bulk downloads in CSV, Excel, and Parquet supplement live APIs.
  name: Bulk Downloads
- description: WATERS, How's My Waterway, and StreamCat expose hydrography overlays.
  name: Geospatial Layers
- description: Many program datasets flow from state primacy agencies into national systems.
  name: State Primacy
- description: Some surfaces (AQS, CAM, Grants) require email-or-portal-registered keys with documented rate limits.
  name: API Key Tiers
graphqls:
- description: The U.S. Environmental Protection Agency (EPA) does not currently publish a native public GraphQL endpoint. The EPA exposes its environmental data through REST and SOAP services across programs includ
  name: EPA — U.S. Environmental Protection Agency GraphQL API
  slug: epa-graphql
image: https://www.epa.gov/themes/epa_theme/images/epa-logo.png
integrations:
- description: Government-wide API management front-door for several EPA APIs with X-API-Key sign-up flow.
  name: api.data.gov
- description: Federal open data catalog cross-listing every EPA-published dataset.
  name: data.gov
- description: EPA's Network Authentication & Authorization Services for credentialed submissions (FRS Submit, e-Manifest, NEI).
  name: NAAS / CDX
- description: State primacy programs forward data into AQS, ECHO, SDWIS, RCRAInfo, and TRI.
  name: State Environmental Agencies
- description: Cross-agency data sharing for water, weather, and agricultural environmental data.
  name: USGS, NOAA, USDA
json_schemas:
- name: Envelope
  property_count: 2
  slug: aqs-envelope
- name: Header
  property_count: 5
  slug: aqs-header
- name: AccountAttributesDTO
  property_count: 10
  slug: cam-account-account-attributes-dto
- name: AccountDTO
  property_count: 2
  slug: cam-account-account-dto
- name: AllowanceComplianceDTO
  property_count: 22
  slug: cam-account-allowance-compliance-dto
- name: AllowanceHoldingsDTO
  property_count: 12
  slug: cam-account-allowance-holdings-dto
- name: AllowanceTransactionsDTO
  property_count: 27
  slug: cam-account-allowance-transactions-dto
- name: ApplicableAccountAttributesDTO
  property_count: 6
  slug: cam-account-applicable-account-attributes-dto
- name: ApplicableAllowanceComplianceAttributesDTO
  property_count: 5
  slug: cam-account-applicable-allowance-compliance-attributes-dto
- name: ApplicableAllowanceHoldingsAttributesDTO
  property_count: 7
  slug: cam-account-applicable-allowance-holdings-attributes-dto
- name: ApplicableAllowanceTransactionsAttributesDTO
  property_count: 13
  slug: cam-account-applicable-allowance-transactions-attributes-dto
- name: ApplicableComplianceAttributesDTO
  property_count: 4
  slug: cam-account-applicable-compliance-attributes-dto
- name: EmissionsComplianceDTO
  property_count: 12
  slug: cam-account-emissions-compliance-dto
- name: OwnerOperatorsDTO
  property_count: 2
  slug: cam-account-owner-operators-dto
- name: BulkFileDTO
  property_count: 8
  slug: cam-camd-services-bulk-file-dto
- name: EmailRecipientListRequestDto
  property_count: 2
  slug: cam-camd-services-email-recipient-list-request-dto
- name: EmailRecipientListResponseDto
  property_count: 3
  slug: cam-camd-services-email-recipient-list-response-dto
- name: ReportColumnDTO
  property_count: 2
  slug: cam-camd-services-report-column-dto
- name: ReportDetailDTO
  property_count: 4
  slug: cam-camd-services-report-detail-dto
- name: ReportDTO
  property_count: 3
  slug: cam-camd-services-report-dto
- name: AnnualApportionedEmissionsAggregationDTO
  property_count: 7
  slug: cam-emissions-annual-apportioned-emissions-aggregation-dto
- name: AnnualApportionedEmissionsFacilityAggregationDTO
  property_count: 10
  slug: cam-emissions-annual-apportioned-emissions-facility-aggregation-dto
- name: AnnualApportionedEmissionsStateAggregationDTO
  property_count: 8
  slug: cam-emissions-annual-apportioned-emissions-state-aggregation-dto
- name: AnnualUnitDataView
  property_count: 26
  slug: cam-emissions-annual-unit-data-view
- name: ApplicableApportionedEmissionsAttributesDTO
  property_count: 7
  slug: cam-emissions-applicable-apportioned-emissions-attributes-dto
- name: DailyApportionedEmissionsFacilityAggregationDTO
  property_count: 10
  slug: cam-emissions-daily-apportioned-emissions-facility-aggregation-dto
- name: DailyApportionedEmissionsNationalAggregationDTO
  property_count: 7
  slug: cam-emissions-daily-apportioned-emissions-national-aggregation-dto
- name: DailyApportionedEmissionsStateAggregationDTO
  property_count: 8
  slug: cam-emissions-daily-apportioned-emissions-state-aggregation-dto
- name: DayUnitDataView
  property_count: 25
  slug: cam-emissions-day-unit-data-view
- name: EmissionsReviewDTO
  property_count: 15
  slug: cam-emissions-emissions-review-dto
- name: EmissionsSubmissionsProgressDTO
  property_count: 4
  slug: cam-emissions-emissions-submissions-progress-dto
- name: EmissionsViewDTO
  property_count: 2
  slug: cam-emissions-emissions-view-dto
- name: HourUnitDataView
  property_count: 34
  slug: cam-emissions-hour-unit-data-view
- name: HourUnitMatsDataView
  property_count: 30
  slug: cam-emissions-hour-unit-mats-data-view
- name: HourlyApportionedEmissionsDTO
  property_count: 34
  slug: cam-emissions-hourly-apportioned-emissions-dto
- name: HourlyApportionedEmissionsFacilityAggregationDTO
  property_count: 11
  slug: cam-emissions-hourly-apportioned-emissions-facility-aggregation-dto
- name: HourlyApportionedEmissionsNationalAggregationDTO
  property_count: 8
  slug: cam-emissions-hourly-apportioned-emissions-national-aggregation-dto
- name: HourlyApportionedEmissionsStateAggregationDTO
  property_count: 9
  slug: cam-emissions-hourly-apportioned-emissions-state-aggregation-dto
- name: HourlyMatsApportionedEmissionsDTO
  property_count: 30
  slug: cam-emissions-hourly-mats-apportioned-emissions-dto
- name: MonthUnitDataView
  property_count: 26
  slug: cam-emissions-month-unit-data-view
- name: MonthlyApportionedEmissionsFacilityAggregationDTO
  property_count: 11
  slug: cam-emissions-monthly-apportioned-emissions-facility-aggregation-dto
- name: MonthlyApportionedEmissionsNationalAggregationDTO
  property_count: 8
  slug: cam-emissions-monthly-apportioned-emissions-national-aggregation-dto
- name: MonthlyApportionedEmissionsStateAggregationDTO
  property_count: 9
  slug: cam-emissions-monthly-apportioned-emissions-state-aggregation-dto
- name: OzoneApportionedEmissionsFacilityAggregationDTO
  property_count: 10
  slug: cam-emissions-ozone-apportioned-emissions-facility-aggregation-dto
- name: OzoneApportionedEmissionsNationalAggregationDTO
  property_count: 7
  slug: cam-emissions-ozone-apportioned-emissions-national-aggregation-dto
- name: OzoneApportionedEmissionsStateAggregationDTO
  property_count: 8
  slug: cam-emissions-ozone-apportioned-emissions-state-aggregation-dto
- name: OzoneUnitDataView
  property_count: 26
  slug: cam-emissions-ozone-unit-data-view
- name: QuarterUnitDataView
  property_count: 27
  slug: cam-emissions-quarter-unit-data-view
- name: QuarterlyApportionedEmissionsFacilityAggregationDTO
  property_count: 11
  slug: cam-emissions-quarterly-apportioned-emissions-facility-aggregation-dto
- name: QuarterlyApportionedEmissionsNationalAggregationDTO
  property_count: 8
  slug: cam-emissions-quarterly-apportioned-emissions-national-aggregation-dto
- name: QuarterlyApportionedEmissionsStateAggregationDTO
  property_count: 9
  slug: cam-emissions-quarterly-apportioned-emissions-state-aggregation-dto
- name: ApplicableFacilityAttributesDTO
  property_count: 8
  slug: cam-facilities-applicable-facility-attributes-dto
- name: FacilityAttributesDTO
  property_count: 30
  slug: cam-facilities-facility-attributes-dto
- name: FacilityDTO
  property_count: 5
  slug: cam-facilities-facility-dto
- name: AccountTypeDTO
  property_count: 4
  slug: cam-master-data-account-type-dto
- name: CodeTableDto
  property_count: 2
  slug: cam-master-data-code-table-dto
- name: ControlTechnologyDTO
  property_count: 4
  slug: cam-master-data-control-technology-dto
- name: DataColumnDTO
  property_count: 4
  slug: cam-master-data-data-column-dto
- name: DataSetDTO
  property_count: 5
  slug: cam-master-data-data-set-dto
- name: DataTableDTO
  property_count: 4
  slug: cam-master-data-data-table-dto
- name: FuelTypeDTO
  property_count: 4
  slug: cam-master-data-fuel-type-dto
- name: ProgramDTO
  property_count: 12
  slug: cam-master-data-program-dto
- name: ReportingPeriodDTO
  property_count: 8
  slug: cam-master-data-reporting-period-dto
- name: UnitTypeDTO
  property_count: 5
  slug: cam-master-data-unit-type-dto
- name: AnalyzerRangeDTO
  property_count: 12
  slug: cam-monitor-plan-analyzer-range-dto
- name: AnalyzerRange
  property_count: 12
  slug: cam-monitor-plan-analyzer-range
- name: ComponentDTO
  property_count: 14
  slug: cam-monitor-plan-component-dto
- name: Component
  property_count: 16
  slug: cam-monitor-plan-component
- name: DuctWafDTO
  property_count: 19
  slug: cam-monitor-plan-duct-waf-dto
- name: DuctWaf
  property_count: 19
  slug: cam-monitor-plan-duct-waf
- name: EmissionEvaluation
  property_count: 10
  slug: cam-monitor-plan-emission-evaluation
- name: LastUpdatedConfigDTO
  property_count: 2
  slug: cam-monitor-plan-last-updated-config-dto
- name: LEEQualificationDTO
  property_count: 12
  slug: cam-monitor-plan-leequalification-dto
- name: LEEQualification
  property_count: 13
  slug: cam-monitor-plan-leequalification
- name: LMEQualificationDTO
  property_count: 9
  slug: cam-monitor-plan-lmequalification-dto
- name: LMEQualification
  property_count: 10
  slug: cam-monitor-plan-lmequalification
- name: MatsMethodDTO
  property_count: 12
  slug: cam-monitor-plan-mats-method-dto
- name: MatsMethod
  property_count: 12
  slug: cam-monitor-plan-mats-method
- name: MonitorAttributeDTO
  property_count: 16
  slug: cam-monitor-plan-monitor-attribute-dto
- name: MonitorAttribute
  property_count: 16
  slug: cam-monitor-plan-monitor-attribute
- name: MonitorDefaultDTO
  property_count: 18
  slug: cam-monitor-plan-monitor-default-dto
- name: MonitorDefault
  property_count: 18
  slug: cam-monitor-plan-monitor-default
- name: MonitorFormulaDTO
  property_count: 14
  slug: cam-monitor-plan-monitor-formula-dto
- name: MonitorFormula
  property_count: 14
  slug: cam-monitor-plan-monitor-formula
- name: MonitorLoadDTO
  property_count: 18
  slug: cam-monitor-plan-monitor-load-dto
- name: MonitorLoad
  property_count: 18
  slug: cam-monitor-plan-monitor-load
- name: MonitorLocationDTO
  property_count: 25
  slug: cam-monitor-plan-monitor-location-dto
- name: MonitorLocation
  property_count: 17
  slug: cam-monitor-plan-monitor-location
- name: MonitorMethodDTO
  property_count: 14
  slug: cam-monitor-plan-monitor-method-dto
- name: MonitorMethod
  property_count: 14
  slug: cam-monitor-plan-monitor-method
- name: MonitorPlanCommentDTO
  property_count: 9
  slug: cam-monitor-plan-monitor-plan-comment-dto
- name: MonitorPlanComment
  property_count: 9
  slug: cam-monitor-plan-monitor-plan-comment
- name: MonitorPlanDTO
  property_count: 33
  slug: cam-monitor-plan-monitor-plan-dto
- name: MonitorPlanReportingFreqDTO
  property_count: 9
  slug: cam-monitor-plan-monitor-plan-reporting-freq-dto
- name: MonitorPlanReportingFrequency
  property_count: 11
  slug: cam-monitor-plan-monitor-plan-reporting-frequency
- name: MonitorPlan
  property_count: 26
  slug: cam-monitor-plan-monitor-plan
- name: MonitorQualificationDTO
  property_count: 12
  slug: cam-monitor-plan-monitor-qualification-dto
- name: MonitorQualification
  property_count: 12
  slug: cam-monitor-plan-monitor-qualification
- name: MonitorSpanDTO
  property_count: 23
  slug: cam-monitor-plan-monitor-span-dto
- name: MonitorSpan
  property_count: 23
  slug: cam-monitor-plan-monitor-span
- name: MonitorSystemDTO
  property_count: 16
  slug: cam-monitor-plan-monitor-system-dto
- name: MonitorSystem
  property_count: 16
  slug: cam-monitor-plan-monitor-system
- name: PCTQualificationDTO
  property_count: 16
  slug: cam-monitor-plan-pctqualification-dto
- name: PCTQualification
  property_count: 17
  slug: cam-monitor-plan-pctqualification
- name: Plant
  property_count: 10
  slug: cam-monitor-plan-plant
- name: ProgramCode
  property_count: 26
  slug: cam-monitor-plan-program-code
- name: Program
  property_count: 15
  slug: cam-monitor-plan-program
- name: ReportingFreqDTO
  property_count: 6
  slug: cam-monitor-plan-reporting-freq-dto
- name: ReportingPeriod
  property_count: 8
  slug: cam-monitor-plan-reporting-period
- name: StackPipe
  property_count: 8
  slug: cam-monitor-plan-stack-pipe
- name: SystemComponentDTO
  property_count: 12
  slug: cam-monitor-plan-system-component-dto
- name: SystemComponent
  property_count: 12
  slug: cam-monitor-plan-system-component
- name: SystemFuelFlowDTO
  property_count: 15
  slug: cam-monitor-plan-system-fuel-flow-dto
- name: SystemFuelFlow
  property_count: 13
  slug: cam-monitor-plan-system-fuel-flow
- name: UnitBoilerType
  property_count: 8
  slug: cam-monitor-plan-unit-boiler-type
- name: UnitCapacityDTO
  property_count: 14
  slug: cam-monitor-plan-unit-capacity-dto
- name: UnitCapacity
  property_count: 9
  slug: cam-monitor-plan-unit-capacity
- name: UnitControlDTO
  property_count: 13
  slug: cam-monitor-plan-unit-control-dto
- name: UnitControl
  property_count: 14
  slug: cam-monitor-plan-unit-control
- name: UnitDTO
  property_count: 18
  slug: cam-monitor-plan-unit-dto
- name: UnitFuelDTO
  property_count: 15
  slug: cam-monitor-plan-unit-fuel-dto
- name: UnitFuel
  property_count: 15
  slug: cam-monitor-plan-unit-fuel
- name: UnitOpStatus
  property_count: 6
  slug: cam-monitor-plan-unit-op-status
- name: UnitProgramDTO
  property_count: 13
  slug: cam-monitor-plan-unit-program-dto
- name: UnitProgram
  property_count: 23
  slug: cam-monitor-plan-unit-program
- name: Unit
  property_count: 19
  slug: cam-monitor-plan-unit
- name: UnitStackConfigurationDTO
  property_count: 11
  slug: cam-monitor-plan-unit-stack-configuration-dto
- name: UnitStackConfiguration
  property_count: 10
  slug: cam-monitor-plan-unit-stack-configuration
- name: AirEmissionTestingDTO
  property_count: 14
  slug: cam-qa-cert-air-emission-testing-dto
- name: AppECorrelationTestRunBaseDTO
  property_count: 11
  slug: cam-qa-cert-app-ecorrelation-test-run-base-dto
- name: AppECorrelationTestRunDTO
  property_count: 20
  slug: cam-qa-cert-app-ecorrelation-test-run-dto
- name: AppECorrelationTestRunRecordDTO
  property_count: 18
  slug: cam-qa-cert-app-ecorrelation-test-run-record-dto
- name: AppECorrelationTestSummaryDTO
  property_count: 12
  slug: cam-qa-cert-app-ecorrelation-test-summary-dto
- name: AppECorrelationTestSummaryRecordDTO
  property_count: 11
  slug: cam-qa-cert-app-ecorrelation-test-summary-record-dto
- name: AppEHeatInputFromGasDTO
  property_count: 10
  slug: cam-qa-cert-app-eheat-input-from-gas-dto
- name: AppEHeatInputFromGasRecordDTO
  property_count: 10
  slug: cam-qa-cert-app-eheat-input-from-gas-record-dto
- name: AppEHeatInputFromOilDTO
  property_count: 16
  slug: cam-qa-cert-app-eheat-input-from-oil-dto
- name: AppEHeatInputFromOilRecordDTO
  property_count: 16
  slug: cam-qa-cert-app-eheat-input-from-oil-record-dto
- name: CalibrationInjectionDTO
  property_count: 25
  slug: cam-qa-cert-calibration-injection-dto
- name: CertEventReviewAndSubmitDTO
  property_count: 22
  slug: cam-qa-cert-cert-event-review-and-submit-dto
- name: CycleTimeInjectionDTO
  property_count: 17
  slug: cam-qa-cert-cycle-time-injection-dto
- name: CycleTimeInjectionRecordDTO
  property_count: 17
  slug: cam-qa-cert-cycle-time-injection-record-dto
- name: CycleTimeSummaryDTO
  property_count: 8
  slug: cam-qa-cert-cycle-time-summary-dto
- name: FlowRataRunDTO
  property_count: 23
  slug: cam-qa-cert-flow-rata-run-dto
- name: FlowToLoadCheckDTO
  property_count: 16
  slug: cam-qa-cert-flow-to-load-check-dto
- name: FlowToLoadCheckRecordDTO
  property_count: 16
  slug: cam-qa-cert-flow-to-load-check-record-dto
- name: FlowToLoadReferenceDTO
  property_count: 17
  slug: cam-qa-cert-flow-to-load-reference-dto
- name: FlowToLoadReferenceRecordDTO
  property_count: 17
  slug: cam-qa-cert-flow-to-load-reference-record-dto
- name: FuelFlowToLoadBaselineDTO
  property_count: 17
  slug: cam-qa-cert-fuel-flow-to-load-baseline-dto
- name: FuelFlowToLoadTestDTO
  property_count: 11
  slug: cam-qa-cert-fuel-flow-to-load-test-dto
- name: FuelFlowmeterAccuracyDTO
  property_count: 11
  slug: cam-qa-cert-fuel-flowmeter-accuracy-dto
- name: FuelFlowmeterAccuracyRecordDTO
  property_count: 11
  slug: cam-qa-cert-fuel-flowmeter-accuracy-record-dto
- name: HgInjectionDTO
  property_count: 10
  slug: cam-qa-cert-hg-injection-dto
- name: HgInjectionRecordDTO
  property_count: 10
  slug: cam-qa-cert-hg-injection-record-dto
- name: HgSummaryDTO
  property_count: 15
  slug: cam-qa-cert-hg-summary-dto
- name: LinearityInjectionDTO
  property_count: 10
  slug: cam-qa-cert-linearity-injection-dto
- name: LinearityInjectionRecordDTO
  property_count: 10
  slug: cam-qa-cert-linearity-injection-record-dto
- name: LinearitySummaryDTO
  property_count: 15
  slug: cam-qa-cert-linearity-summary-dto
- name: LinearitySummaryRecordDTO
  property_count: 14
  slug: cam-qa-cert-linearity-summary-record-dto
- name: OnlineOfflineCalibrationDTO
  property_count: 30
  slug: cam-qa-cert-online-offline-calibration-dto
- name: OnlineOfflineCalibrationRecordDTO
  property_count: 30
  slug: cam-qa-cert-online-offline-calibration-record-dto
- name: ProtocolGasDTO
  property_count: 10
  slug: cam-qa-cert-protocol-gas-dto
- name: ProtocolGasRecordDTO
  property_count: 10
  slug: cam-qa-cert-protocol-gas-record-dto
- name: QACertificationDTO
  property_count: 4
  slug: cam-qa-cert-qacertification-dto
- name: QACertificationEventDTO
  property_count: 28
  slug: cam-qa-cert-qacertification-event-dto
- name: RataDTO
  property_count: 14
  slug: cam-qa-cert-rata-dto
- name: RataRecordDTO
  property_count: 13
  slug: cam-qa-cert-rata-record-dto
- name: RataRunDTO
  property_count: 18
  slug: cam-qa-cert-rata-run-dto
- name: RataSummaryDTO
  property_count: 37
  slug: cam-qa-cert-rata-summary-dto
- name: RataSummaryRecordDTO
  property_count: 36
  slug: cam-qa-cert-rata-summary-record-dto
- name: RataTraverseDTO
  property_count: 21
  slug: cam-qa-cert-rata-traverse-dto
- name: RataTraverseRecordDTO
  property_count: 21
  slug: cam-qa-cert-rata-traverse-record-dto
- name: ReviewAndSubmitTestSummaryDTO
  property_count: 19
  slug: cam-qa-cert-review-and-submit-test-summary-dto
- name: TeeReviewAndSubmitDTO
  property_count: 21
  slug: cam-qa-cert-tee-review-and-submit-dto
- name: TestExtensionExemptionDTO
  property_count: 23
  slug: cam-qa-cert-test-extension-exemption-dto
- name: TestExtensionExemptionRecordDTO
  property_count: 23
  slug: cam-qa-cert-test-extension-exemption-record-dto
- name: TestQualificationDTO
  property_count: 11
  slug: cam-qa-cert-test-qualification-dto
- name: TestQualificationRecordDTO
  property_count: 11
  slug: cam-qa-cert-test-qualification-record-dto
- name: TestSummaryDTO
  property_count: 51
  slug: cam-qa-cert-test-summary-dto
- name: TestSummaryRecordDTO
  property_count: 34
  slug: cam-qa-cert-test-summary-record-dto
- name: TransmitterTransducerAccuracyDTO
  property_count: 11
  slug: cam-qa-cert-transmitter-transducer-accuracy-dto
- name: UnitDefaultTestDTO
  property_count: 13
  slug: cam-qa-cert-unit-default-test-dto
- name: UnitDefaultTestRecordDTO
  property_count: 12
  slug: cam-qa-cert-unit-default-test-record-dto
- name: UnitDefaultTestRunDTO
  property_count: 16
  slug: cam-qa-cert-unit-default-test-run-dto
- name: UnitDefaultTestRunRecordDTO
  property_count: 16
  slug: cam-qa-cert-unit-default-test-run-record-dto
- name: AccountAttributesDTO
  property_count: 10
  slug: cam-streaming-account-attributes-dto
- name: AllowanceComplianceDTO
  property_count: 22
  slug: cam-streaming-allowance-compliance-dto
- name: AllowanceHoldingsDTO
  property_count: 12
  slug: cam-streaming-allowance-holdings-dto
- name: AllowanceTransactionsDTO
  property_count: 27
  slug: cam-streaming-allowance-transactions-dto
- name: AnnualApportionedEmissionsAggregationDTO
  property_count: 7
  slug: cam-streaming-annual-apportioned-emissions-aggregation-dto
- name: AnnualApportionedEmissionsDTO
  property_count: 29
  slug: cam-streaming-annual-apportioned-emissions-dto
- name: AnnualApportionedEmissionsFacilityAggregationDTO
  property_count: 10
  slug: cam-streaming-annual-apportioned-emissions-facility-aggregation-dto
- name: AnnualApportionedEmissionsStateAggregationDTO
  property_count: 8
  slug: cam-streaming-annual-apportioned-emissions-state-aggregation-dto
- name: DailyApportionedEmissionsDTO
  property_count: 27
  slug: cam-streaming-daily-apportioned-emissions-dto
- name: DailyApportionedEmissionsFacilityAggregationDTO
  property_count: 10
  slug: cam-streaming-daily-apportioned-emissions-facility-aggregation-dto
- name: DailyApportionedEmissionsNationalAggregationDTO
  property_count: 7
  slug: cam-streaming-daily-apportioned-emissions-national-aggregation-dto
- name: DailyApportionedEmissionsStateAggregationDTO
  property_count: 8
  slug: cam-streaming-daily-apportioned-emissions-state-aggregation-dto
- name: DerivedHourlyValueBaseDTO
  property_count: 10
  slug: cam-streaming-derived-hourly-value-base-dto
- name: EmissionsComplianceDTO
  property_count: 12
  slug: cam-streaming-emissions-compliance-dto
- name: FacilityAttributesDTO
  property_count: 30
  slug: cam-streaming-facility-attributes-dto
- name: HourlyApportionedEmissionsDTO
  property_count: 34
  slug: cam-streaming-hourly-apportioned-emissions-dto
- name: HourlyApportionedEmissionsFacilityAggregationDTO
  property_count: 11
  slug: cam-streaming-hourly-apportioned-emissions-facility-aggregation-dto
- name: HourlyApportionedEmissionsNationalAggregationDTO
  property_count: 8
  slug: cam-streaming-hourly-apportioned-emissions-national-aggregation-dto
- name: HourlyApportionedEmissionsStateAggregationDTO
  property_count: 9
  slug: cam-streaming-hourly-apportioned-emissions-state-aggregation-dto
- name: HourlyMatsApportionedEmissionsDTO
  property_count: 31
  slug: cam-streaming-hourly-mats-apportioned-emissions-dto
- name: HourlyOperatingDTO
  property_count: 11
  slug: cam-streaming-hourly-operating-dto
- name: MonthlyApportionedEmissionsDTO
  property_count: 28
  slug: cam-streaming-monthly-apportioned-emissions-dto
- name: MonthlyApportionedEmissionsFacilityAggregationDTO
  property_count: 11
  slug: cam-streaming-monthly-apportioned-emissions-facility-aggregation-dto
- name: MonthlyApportionedEmissionsNationalAggregationDTO
  property_count: 8
  slug: cam-streaming-monthly-apportioned-emissions-national-aggregation-dto
- name: MonthlyApportionedEmissionsStateAggregationDTO
  property_count: 9
  slug: cam-streaming-monthly-apportioned-emissions-state-aggregation-dto
- name: OzoneApportionedEmissionsDTO
  property_count: 29
  slug: cam-streaming-ozone-apportioned-emissions-dto
- name: OzoneApportionedEmissionsFacilityAggregationDTO
  property_count: 10
  slug: cam-streaming-ozone-apportioned-emissions-facility-aggregation-dto
- name: OzoneApportionedEmissionsNationalAggregationDTO
  property_count: 7
  slug: cam-streaming-ozone-apportioned-emissions-national-aggregation-dto
- name: OzoneApportionedEmissionsStateAggregationDTO
  property_count: 8
  slug: cam-streaming-ozone-apportioned-emissions-state-aggregation-dto
- name: QuarterlyApportionedEmissionsDTO
  property_count: 28
  slug: cam-streaming-quarterly-apportioned-emissions-dto
- name: QuarterlyApportionedEmissionsFacilityAggregationDTO
  property_count: 11
  slug: cam-streaming-quarterly-apportioned-emissions-facility-aggregation-dto
- name: QuarterlyApportionedEmissionsNationalAggregationDTO
  property_count: 8
  slug: cam-streaming-quarterly-apportioned-emissions-national-aggregation-dto
- name: QuarterlyApportionedEmissionsStateAggregationDTO
  property_count: 9
  slug: cam-streaming-quarterly-apportioned-emissions-state-aggregation-dto
- name: SummaryValueBaseDTO
  property_count: 10
  slug: cam-streaming-summary-value-base-dto
- name: SupplementalOperatingDTO
  property_count: 9
  slug: cam-streaming-supplemental-operating-dto
- name: aggregation_engine
  property_count: 0
  slug: cip-service-aggregation-engine
- name: cipsrv_domains
  property_count: 2
  slug: cip-service-cipsrv-domains
- name: cipsrv_domains_state
  property_count: 3
  slug: cip-service-cipsrv-domains-state
- name: cipsrv_domains_states
  property_count: 0
  slug: cip-service-cipsrv-domains-states
- name: cipsrv_domains_tribe
  property_count: 4
  slug: cip-service-cipsrv-domains-tribe
- name: cipsrv_domains_tribes
  property_count: 0
  slug: cip-service-cipsrv-domains-tribes
- name: cipsrv_index_rb
  property_count: 29
  slug: cip-service-cipsrv-index-rb
- name: cipsrv_index_resp
  property_count: 13
  slug: cip-service-cipsrv-index-resp
- name: cipsrv_registry_components
  property_count: 6
  slug: cip-service-cipsrv-registry-components
- name: cipsrv_registry
  property_count: 4
  slug: cip-service-cipsrv-registry
- name: coordinates1
  property_count: 0
  slug: cip-service-coordinates1
- name: coordinates2
  property_count: 0
  slug: cip-service-coordinates2
- name: coordinates3
  property_count: 0
  slug: cip-service-coordinates3
- name: delineate_rb
  property_count: 20
  slug: cip-service-delineate-rb
- name: delineate_resp
  property_count: 7
  slug: cip-service-delineate-resp
- name: delineated_area_properties
  property_count: 4
  slug: cip-service-delineated-area-properties
- name: end_point_properties
  property_count: 3
  slug: cip-service-end-point-properties
- name: event_feature_properties
  property_count: 8
  slug: cip-service-event-feature-properties
- name: fcode_allow
  property_count: 0
  slug: cip-service-fcode-allow
- name: fcode_deny
  property_count: 0
  slug: cip-service-fcode-deny
- name: fill_basin_holes
  property_count: 0
  slug: cip-service-fill-basin-holes
- name: flow_accumulation_rb
  property_count: 6
  slug: cip-service-flow-accumulation-rb
- name: flow_accumulation_resp
  property_count: 11
  slug: cip-service-flow-accumulation-resp
- name: flowline_count
  property_count: 0
  slug: cip-service-flowline-count
- name: geojson_bbox
  property_count: 0
  slug: cip-service-geojson-bbox
- name: geojson_feature
  property_count: 5
  slug: cip-service-geojson-feature
- name: geojson_featurecollection
  property_count: 2
  slug: cip-service-geojson-featurecollection
- name: geojson_geometry
  property_count: 2
  slug: cip-service-geojson-geometry
- name: globalid
  property_count: 0
  slug: cip-service-globalid
- name: hydroseq
  property_count: 0
  slug: cip-service-hydroseq
- name: image_format
  property_count: 0
  slug: cip-service-image-format
- name: indexed_catchment_properties
  property_count: 4
  slug: cip-service-indexed-catchment-properties
- name: indexed_flowline_properties
  property_count: 6
  slug: cip-service-indexed-flowline-properties
- name: indexing_engine
  property_count: 0
  slug: cip-service-indexing-engine
- name: indexing_line_properties
  property_count: 1
  slug: cip-service-indexing-line-properties
- name: indexing_summary
  property_count: 1
  slug: cip-service-indexing-summary
- name: known_region
  property_count: 0
  slug: cip-service-known-region
- name: linked_data_program
  property_count: 0
  slug: cip-service-linked-data-program
- name: linked_data_wqp
  property_count: 41
  slug: cip-service-linked-data-wqp
- name: max_distancekm
  property_count: 0
  slug: cip-service-max-distancekm
- name: max_flowtimeday
  property_count: 0
  slug: cip-service-max-flowtimeday
- name: measure
  property_count: 0
  slug: cip-service-measure
- name: navigate_rb
  property_count: 17
  slug: cip-service-navigate-rb
- name: navigate_resp
  property_count: 5
  slug: cip-service-navigate-resp
- name: navigated_flowline_properties
  property_count: 20
  slug: cip-service-navigated-flowline-properties
- name: nhdplus_version
  property_count: 0
  slug: cip-service-nhdplus-version
- name: nhdplusid
  property_count: 0
  slug: cip-service-nhdplusid
- name: ordinate
  property_count: 0
  slug: cip-service-ordinate
- name: permanent_identifier
  property_count: 0
  slug: cip-service-permanent-identifier
- name: pointindexing_rb
  property_count: 13
  slug: cip-service-pointindexing-rb
- name: pointindexing_resp
  property_count: 11
  slug: cip-service-pointindexing-resp
- name: randomcatchment_rb
  property_count: 1
  slug: cip-service-randomcatchment-rb
- name: randomcatchment_resp
  property_count: 1
  slug: cip-service-randomcatchment-resp
- name: randomhuc12_rb
  property_count: 1
  slug: cip-service-randomhuc12-rb
- name: randomhuc12_resp
  property_count: 1
  slug: cip-service-randomhuc12-resp
- name: randomnav_rb
  property_count: 1
  slug: cip-service-randomnav-rb
- name: randomnav_resp
  property_count: 1
  slug: cip-service-randomnav-resp
- name: randompoint_rb
  property_count: 1
  slug: cip-service-randompoint-rb
- name: randompoint_resp
  property_count: 1
  slug: cip-service-randompoint-resp
- name: randomppnav_rb
  property_count: 1
  slug: cip-service-randomppnav-rb
- name: randomppnav_resp
  property_count: 2
  slug: cip-service-randomppnav-resp
- name: reachcode
  property_count: 0
  slug: cip-service-reachcode
- name: return_code
  property_count: 0
  slug: cip-service-return-code
- name: return_delineation_geometry
  property_count: 0
  slug: cip-service-return-delineation-geometry
- name: return_flowline_details
  property_count: 0
  slug: cip-service-return-flowline-details
- name: return_flowline_geometry
  property_count: 0
  slug: cip-service-return-flowline-geometry
- name: search_type
  property_count: 0
  slug: cip-service-search-type
- name: split_initial_catchment
  property_count: 0
  slug: cip-service-split-initial-catchment
- name: start_hydroseq
  property_count: 0
  slug: cip-service-start-hydroseq
- name: start_measure
  property_count: 0
  slug: cip-service-start-measure
- name: start_nhdplusid
  property_count: 0
  slug: cip-service-start-nhdplusid
- name: start_permanent_identifier
  property_count: 0
  slug: cip-service-start-permanent-identifier
- name: start_reachcode
  property_count: 0
  slug: cip-service-start-reachcode
- name: status_message
  property_count: 0
  slug: cip-service-status-message
- name: stop_hydroseq
  property_count: 0
  slug: cip-service-stop-hydroseq
- name: stop_measure
  property_count: 0
  slug: cip-service-stop-measure
- name: stop_nhdplusid
  property_count: 0
  slug: cip-service-stop-nhdplusid
- name: stop_permanent_identifier
  property_count: 0
  slug: cip-service-stop-permanent-identifier
- name: stop_reachcode
  property_count: 0
  slug: cip-service-stop-reachcode
- name: upstreamdownstream_rb
  property_count: 49
  slug: cip-service-upstreamdownstream-rb
- name: upstreamdownstream_resp
  property_count: 27
  slug: cip-service-upstreamdownstream-resp
- name: wbd_version
  property_count: 0
  slug: cip-service-wbd-version
- name: FormioSchemaAndSubmission
  property_count: 3
  slug: csb-rebate-formio-schema-and-submission
- name: air00
  property_count: 17
  slug: echo-air-air00
- name: air01
  property_count: 1
  slug: echo-air-air01
- name: air02
  property_count: 10
  slug: echo-air-air02
- name: air03
  property_count: 143
  slug: echo-air-air03
- name: air04
  property_count: 4
  slug: echo-air-air04
- name: air05
  property_count: 15
  slug: echo-air-air05
- name: air06
  property_count: 144
  slug: echo-air-air06
- name: air08
  property_count: 19
  slug: echo-air-air08
- name: air09
  property_count: 3
  slug: echo-air-air09
- name: air10
  property_count: 141
  slug: echo-air-air10
- name: air11
  property_count: 4
  slug: echo-air-air11
- name: air12
  property_count: 5
  slug: echo-air-air12
- name: geo
  property_count: 2
  slug: echo-air-geo
- name: meta1
  property_count: 2
  slug: echo-air-meta1
- name: meta3
  property_count: 6
  slug: echo-air-meta3
- name: qp0
  property_count: 2
  slug: echo-air-qp0
- name: echo01
  property_count: 13
  slug: echo-all-echo01
- name: echo02
  property_count: 4
  slug: echo-all-echo02
- name: echo03
  property_count: 193
  slug: echo-all-echo03
- name: echo04
  property_count: 20
  slug: echo-all-echo04
- name: echo05
  property_count: 17
  slug: echo-all-echo05
- name: echo06
  property_count: 1
  slug: echo-all-echo06
- name: echo07
  property_count: 194
  slug: echo-all-echo07
- name: echo08
  property_count: 23
  slug: echo-all-echo08
- name: echo09
  property_count: 3
  slug: echo-all-echo09
- name: echo10
  property_count: 191
  slug: echo-all-echo10
- name: echo11
  property_count: 5
  slug: echo-all-echo11
- name: geo
  property_count: 2
  slug: echo-all-geo
- name: meta1
  property_count: 2
  slug: echo-all-meta1
- name: meta3
  property_count: 6
  slug: echo-all-meta3
- name: qp0
  property_count: 2
  slug: echo-all-qp0
- name: crs0_Cases
  property_count: 40
  slug: echo-case-crs0-cases
- name: crs0_ClusterData
  property_count: 22
  slug: echo-case-crs0-cluster-data
- name: crs0_ClusterOutput
  property_count: 1
  slug: echo-case-crs0-cluster-output
- name: crs0_get_case_info.Results
  property_count: 20
  slug: echo-case-crs0-get-case-info.results
- name: crs0_get_cases_from_facility.CaseNumber
  property_count: 1
  slug: echo-case-crs0-get-cases-from-facility.case-number
- name: crs0_get_cases_from_facility.CaseNumbers
  property_count: 1
  slug: echo-case-crs0-get-cases-from-facility.case-numbers
- name: crs0_get_cases_from_facility.Results
  property_count: 1
  slug: echo-case-crs0-get-cases-from-facility.results
- name: crs0_get_facilities_from_case.RegistryID
  property_count: 1
  slug: echo-case-crs0-get-facilities-from-case.registry-id
- name: crs0_get_facilities_from_case.RegistryIDs
  property_count: 1
  slug: echo-case-crs0-get-facilities-from-case.registry-ids
- name: crs0_get_facilities_from_case.Results
  property_count: 1
  slug: echo-case-crs0-get-facilities-from-case.results
- name: crs0_MapData
  property_count: 7
  slug: echo-case-crs0-map-data
- name: crs0_MapOutput
  property_count: 4
  slug: echo-case-crs0-map-output
- name: crs1_CAEDDocuments
  property_count: 5
  slug: echo-case-crs1-caeddocuments
- name: crs1_CaseInformation
  property_count: 22
  slug: echo-case-crs1-case-information
- name: crs1_CaseMilestones
  property_count: 2
  slug: echo-case-crs1-case-milestones
- name: crs1_Citations
  property_count: 3
  slug: echo-case-crs1-citations
- name: crs1_ComplianceSchedules
  property_count: 7
  slug: echo-case-crs1-compliance-schedules
- name: crs1_ComplyingActions
  property_count: 4
  slug: echo-case-crs1-complying-actions
- name: crs1_Defendants
  property_count: 3
  slug: echo-case-crs1-defendants
- name: crs1_EnforcementConclusions
  property_count: 18
  slug: echo-case-crs1-enforcement-conclusions
- name: crs1_Facilities
  property_count: 8
  slug: echo-case-crs1-facilities
- name: crs1_FinalOrderStatuses
  property_count: 5
  slug: echo-case-crs1-final-order-statuses
- name: crs1_LawsAndSections
  property_count: 3
  slug: echo-case-crs1-laws-and-sections
- name: crs1_PollutantReductions
  property_count: 8
  slug: echo-case-crs1-pollutant-reductions
- name: crs1_Pollutants
  property_count: 2
  slug: echo-case-crs1-pollutants
- name: crs1_ProgramLinks
  property_count: 3
  slug: echo-case-crs1-program-links
- name: crs1_RelatedActivities
  property_count: 2
  slug: echo-case-crs1-related-activities
- name: crs1_Results
  property_count: 12
  slug: echo-case-crs1-results
- name: crs1_SupplementalEnvironmentalProjects
  property_count: 5
  slug: echo-case-crs1-supplemental-environmental-projects
- name: crs2_Results
  property_count: 20
  slug: echo-case-crs2-results
- name: crs3_CaseInformation
  property_count: 5
  slug: echo-case-crs3-case-information
- name: crs3_CRDefendants
  property_count: 5
  slug: echo-case-crs3-crdefendants
- name: crs3_CRDetails
  property_count: 3
  slug: echo-case-crs3-crdetails
- name: crs3_Locations
  property_count: 7
  slug: echo-case-crs3-locations
- name: crs3_Results
  property_count: 5
  slug: echo-case-crs3-results
- name: crs5_Results
  property_count: 5
  slug: echo-case-crs5-results
- name: met1
  property_count: 2
  slug: echo-case-met1
- name: met2
  property_count: 6
  slug: echo-case-met2
- name: qp0
  property_count: 2
  slug: echo-case-qp0
- name: rlk00_LuValues
  property_count: 2
  slug: echo-case-rlk00-lu-values
- name: rlk51_Results
  property_count: 2
  slug: echo-case-rlk51-results
- name: cwa01
  property_count: 305
  slug: echo-cwa-cwa01
- name: cwa02
  property_count: 10
  slug: echo-cwa-cwa02
- name: cwa03
  property_count: 4
  slug: echo-cwa-cwa03
- name: cwa04
  property_count: 19
  slug: echo-cwa-cwa04
- name: cwa05
  property_count: 20
  slug: echo-cwa-cwa05
- name: cwa06
  property_count: 1
  slug: echo-cwa-cwa06
- name: cwa07
  property_count: 306
  slug: echo-cwa-cwa07
- name: cwa08
  property_count: 22
  slug: echo-cwa-cwa08
- name: cwa09
  property_count: 3
  slug: echo-cwa-cwa09
- name: cwa10
  property_count: 303
  slug: echo-cwa-cwa10
- name: cwa11
  property_count: 10
  slug: echo-cwa-cwa11
- name: cwa12
  property_count: 4
  slug: echo-cwa-cwa12
- name: cwa13
  property_count: 5
  slug: echo-cwa-cwa13
- name: geo
  property_count: 2
  slug: echo-cwa-geo
- name: meta1
  property_count: 2
  slug: echo-cwa-meta1
- name: meta3
  property_count: 6
  slug: echo-cwa-meta3
- name: qp0
  property_count: 2
  slug: echo-cwa-qp0
- name: rlup01
  property_count: 2
  slug: echo-cwa-rlup01
- name: rlup20
  property_count: 2
  slug: echo-cwa-rlup20
- name: rlup23
  property_count: 2
  slug: echo-cwa-rlup23
- name: rlup24
  property_count: 2
  slug: echo-cwa-rlup24
- name: rlup54
  property_count: 2
  slug: echo-cwa-rlup54
- name: rlup58
  property_count: 2
  slug: echo-cwa-rlup58
- name: rlup59
  property_count: 2
  slug: echo-cwa-rlup59
- name: rlup61
  property_count: 2
  slug: echo-cwa-rlup61
- name: rlup65
  property_count: 2
  slug: echo-cwa-rlup65
- name: rlup75
  property_count: 2
  slug: echo-cwa-rlup75
- name: rlup77
  property_count: 2
  slug: echo-cwa-rlup77
- name: dfr0_get_aws_docs.Results
  property_count: 1
  slug: echo-dfr-dfr0-get-aws-docs.results
- name: dfr0_get_cwa_eff_alr_exp.Results
  property_count: 2
  slug: echo-dfr-dfr0-get-cwa-eff-alr-exp.results
- name: dfr0_get_cwa_eff_compliance_exp.Results
  property_count: 2
  slug: echo-dfr-dfr0-get-cwa-eff-compliance-exp.results
- name: dfr0_get_d80d90s_details.D80D90sDetails
  property_count: 1
  slug: echo-dfr-dfr0-get-d80d90s-details.d80-d90s-details
- name: dfr0_get_d80d90s_details.D80D90sDetails.Sources
  property_count: 29
  slug: echo-dfr-dfr0-get-d80d90s-details.d80-d90s-details.sources
- name: dfr0_get_d80d90s_details.Results
  property_count: 2
  slug: echo-dfr-dfr0-get-d80d90s-details.results
- name: dfr0_get_ejscreen_indexes.Results
  property_count: 2
  slug: echo-dfr-dfr0-get-ejscreen-indexes.results
- name: dfr0_Qtr12Header
  property_count: 96
  slug: echo-dfr-dfr0-qtr12-header
- name: dfr0_Qtr12Header39
  property_count: 102
  slug: echo-dfr-dfr0-qtr12-header39
- name: dfr0_Qtr12Status
  property_count: 13
  slug: echo-dfr-dfr0-qtr12-status
- name: dfr0_Qtr13Header
  property_count: 104
  slug: echo-dfr-dfr0-qtr13-header
- name: dfr0_Qtr13Status
  property_count: 14
  slug: echo-dfr-dfr0-qtr13-status
- name: dfr001_Results
  property_count: 2
  slug: echo-dfr-dfr001-results
- name: dfr002_Results
  property_count: 2
  slug: echo-dfr-dfr002-results
- name: dfr004
  property_count: 2
  slug: echo-dfr-dfr004
- name: dfr005_Results
  property_count: 2
  slug: echo-dfr-dfr005-results
- name: dfr006_Results
  property_count: 2
  slug: echo-dfr-dfr006-results
- name: dfr007_Results
  property_count: 2
  slug: echo-dfr-dfr007-results
- name: dfr009_Results
  property_count: 2
  slug: echo-dfr-dfr009-results
- name: dfr010_Results
  property_count: 2
  slug: echo-dfr-dfr010-results
- name: dfr011_Results
  property_count: 2
  slug: echo-dfr-dfr011-results
- name: dfr012_Results
  property_count: 2
  slug: echo-dfr-dfr012-results
- name: dfr013_Results
  property_count: 2
  slug: echo-dfr-dfr013-results
- name: dfr014_Results
  property_count: 2
  slug: echo-dfr-dfr014-results
- name: dfr015_Results
  property_count: 2
  slug: echo-dfr-dfr015-results
- name: dfr017_Results
  property_count: 2
  slug: echo-dfr-dfr017-results
- name: dfr018_CAEDDocuments
  property_count: 5
  slug: echo-dfr-dfr018-caeddocuments
- name: dfr018_EJScreenIndexes
  property_count: 13
  slug: echo-dfr-dfr018-ejscreen-indexes
- name: dfr018_MapData
  property_count: 6
  slug: echo-dfr-dfr018-map-data
- name: dfr018_MultipleFRSFacilities
  property_count: 1
  slug: echo-dfr-dfr018-multiple-frsfacilities
- name: dfr018_NAICS
  property_count: 1
  slug: echo-dfr-dfr018-naics
- name: dfr018_Permits
  property_count: 27
  slug: echo-dfr-dfr018-permits
- name: dfr018_ProgramDates
  property_count: 3
  slug: echo-dfr-dfr018-program-dates
- name: dfr018_RegistryIDs
  property_count: 8
  slug: echo-dfr-dfr018-registry-ids
- name: dfr018_Reports
  property_count: 1
  slug: echo-dfr-dfr018-reports
- name: dfr018_Results
  property_count: 44
  slug: echo-dfr-dfr018-results
- name: dfr018_Summaries
  property_count: 11
  slug: echo-dfr-dfr018-summaries
- name: dfr018_WebFireDocuments
  property_count: 7
  slug: echo-dfr-dfr018-web-fire-documents
- name: dfr019
  property_count: 2
  slug: echo-dfr-dfr019
- name: dfr020_.HPVHistory
  property_count: 49
  slug: echo-dfr-dfr020-.hpvhistory
- name: dfr020_.PermitHistory
  property_count: 49
  slug: echo-dfr-dfr020-.permit-history
- name: dfr020
  property_count: 5
  slug: echo-dfr-dfr020
- name: dfr021
  property_count: 14
  slug: echo-dfr-dfr021
- name: dfr022
  property_count: 53
  slug: echo-dfr-dfr022
- name: dfr023
  property_count: 53
  slug: echo-dfr-dfr023
- name: dfr024
  property_count: 13
  slug: echo-dfr-dfr024
- name: dfr025
  property_count: 2
  slug: echo-dfr-dfr025
- name: dfr026
  property_count: 1
  slug: echo-dfr-dfr026
- name: dfr027
  property_count: 2
  slug: echo-dfr-dfr027
- name: dfr029
  property_count: 1
  slug: echo-dfr-dfr029
- name: dfr030
  property_count: 54
  slug: echo-dfr-dfr030
- name: dfr031
  property_count: 2
  slug: echo-dfr-dfr031
- name: dfr032
  property_count: 1
  slug: echo-dfr-dfr032
- name: dfr034
  property_count: 107
  slug: echo-dfr-dfr034
- name: dfr035_EXP
  property_count: 2
  slug: echo-dfr-dfr035-exp
- name: dfr035_EXP.Parameters
  property_count: 58
  slug: echo-dfr-dfr035-exp.parameters
- name: dfr035_EXP.Sources
  property_count: 1
  slug: echo-dfr-dfr035-exp.sources
- name: dfr035
  property_count: 2
  slug: echo-dfr-dfr035
- name: dfr036
  property_count: 57
  slug: echo-dfr-dfr036
- name: dfr037
  property_count: 1
  slug: echo-dfr-dfr037
- name: dfr038_EXP
  property_count: 2
  slug: echo-dfr-dfr038-exp
- name: dfr038_EXP.Parameters
  property_count: 110
  slug: echo-dfr-dfr038-exp.parameters
- name: dfr038_EXP.Sources
  property_count: 1
  slug: echo-dfr-dfr038-exp.sources
- name: dfr038
  property_count: 2
  slug: echo-dfr-dfr038
- name: dfr040
  property_count: 109
  slug: echo-dfr-dfr040
- name: dfr041
  property_count: 1
  slug: echo-dfr-dfr041
- name: dfr042
  property_count: 2
  slug: echo-dfr-dfr042
- name: dfr043
  property_count: 1
  slug: echo-dfr-dfr043
- name: dfr045
  property_count: 107
  slug: echo-dfr-dfr045
- name: dfr046
  property_count: 2
  slug: echo-dfr-dfr046
- name: dfr047_.Status
  property_count: 1
  slug: echo-dfr-dfr047-.status
- name: dfr049
  property_count: 2
  slug: echo-dfr-dfr049
- name: dfr050
  property_count: 1
  slug: echo-dfr-dfr050
- name: dfr051
  property_count: 108
  slug: echo-dfr-dfr051
- name: dfr052
  property_count: 2
  slug: echo-dfr-dfr052
- name: dfr053
  property_count: 13
  slug: echo-dfr-dfr053
- name: dfr054
  property_count: 6
  slug: echo-dfr-dfr054
- name: dfr055
  property_count: 1
  slug: echo-dfr-dfr055
- name: dfr057
  property_count: 2
  slug: echo-dfr-dfr057
- name: dfr058
  property_count: 10
  slug: echo-dfr-dfr058
- name: dfr059
  property_count: 2
  slug: echo-dfr-dfr059
- name: dfr060
  property_count: 6
  slug: echo-dfr-dfr060
- name: dfr061
  property_count: 32
  slug: echo-dfr-dfr061
- name: dfr062
  property_count: 2
  slug: echo-dfr-dfr062
- name: dfr063_s
  property_count: 4
  slug: echo-dfr-dfr063-s
- name: dfr064
  property_count: 2
  slug: echo-dfr-dfr064
- name: dfr065
  property_count: 7
  slug: echo-dfr-dfr065
- name: dfr066
  property_count: 2
  slug: echo-dfr-dfr066
- name: dfr067
  property_count: 16
  slug: echo-dfr-dfr067
- name: dfr068
  property_count: 2
  slug: echo-dfr-dfr068
- name: dfr069
  property_count: 7
  slug: echo-dfr-dfr069
- name: dfr070
  property_count: 18
  slug: echo-dfr-dfr070
- name: dfr071
  property_count: 4
  slug: echo-dfr-dfr071
- name: dfr072
  property_count: 4
  slug: echo-dfr-dfr072
- name: dfr073
  property_count: 5
  slug: echo-dfr-dfr073
- name: dfr074
  property_count: 1
  slug: echo-dfr-dfr074
- name: dfr075
  property_count: 4
  slug: echo-dfr-dfr075
- name: dfr076
  property_count: 2
  slug: echo-dfr-dfr076
- name: dfr077
  property_count: 7
  slug: echo-dfr-dfr077
- name: dfr078
  property_count: 97
  slug: echo-dfr-dfr078
- name: dfr079_s
  property_count: 3
  slug: echo-dfr-dfr079-s
- name: dfr079_s.Evaluations
  property_count: 52
  slug: echo-dfr-dfr079-s.evaluations
- name: dfr079_s.Status
  property_count: 49
  slug: echo-dfr-dfr079-s.status
- name: dfr079_s.Violations
  property_count: 52
  slug: echo-dfr-dfr079-s.violations
- name: dfr081
  property_count: 105
  slug: echo-dfr-dfr081
- name: dfr083_s
  property_count: 2
  slug: echo-dfr-dfr083-s
- name: dfr083_s.RulesViolated
  property_count: 15
  slug: echo-dfr-dfr083-s.rules-violated
- name: dfr084_Codes
  property_count: 4
  slug: echo-dfr-dfr084-codes
- name: dfr084
  property_count: 1
  slug: echo-dfr-dfr084
- name: dfr085
  property_count: 1
  slug: echo-dfr-dfr085
- name: dfr086
  property_count: 1
  slug: echo-dfr-dfr086
- name: dfr088
  property_count: 1
  slug: echo-dfr-dfr088
- name: dfr089
  property_count: 15
  slug: echo-dfr-dfr089
- name: dfr090
  property_count: 1
  slug: echo-dfr-dfr090
- name: dfr092
  property_count: 1
  slug: echo-dfr-dfr092
- name: dfr093
  property_count: 15
  slug: echo-dfr-dfr093
- name: dfr094
  property_count: 8
  slug: echo-dfr-dfr094
- name: dfr095
  property_count: 1
  slug: echo-dfr-dfr095
- name: dfr096
  property_count: 2
  slug: echo-dfr-dfr096
- name: dfr098
  property_count: 1
  slug: echo-dfr-dfr098
- name: dfr100
  property_count: 1
  slug: echo-dfr-dfr100
- name: dfr101
  property_count: 10
  slug: echo-dfr-dfr101
- name: dfr102
  property_count: 2
  slug: echo-dfr-dfr102
- name: dfr103
  property_count: 10
  slug: echo-dfr-dfr103
- name: dfr104
  property_count: 9
  slug: echo-dfr-dfr104
- name: dfr105
  property_count: 4
  slug: echo-dfr-dfr105
- name: dfr106
  property_count: 1
  slug: echo-dfr-dfr106
- name: dfr108
  property_count: 1
  slug: echo-dfr-dfr108
- name: dfr109
  property_count: 5
  slug: echo-dfr-dfr109
- name: dfr110
  property_count: 14
  slug: echo-dfr-dfr110
- name: dfr111_Details
  property_count: 1
  slug: echo-dfr-dfr111-details
- name: dfr111_Details.Sources
  property_count: 16
  slug: echo-dfr-dfr111-details.sources
- name: dfr111
  property_count: 1
  slug: echo-dfr-dfr111
- name: dfr112
  property_count: 21
  slug: echo-dfr-dfr112
- name: dfr114_Results
  property_count: 2
  slug: echo-dfr-dfr114-results
- name: dfr115
  property_count: 2
  slug: echo-dfr-dfr115
- name: dfr116_Results
  property_count: 2
  slug: echo-dfr-dfr116-results
- name: dfr117_Results
  property_count: 2
  slug: echo-dfr-dfr117-results
- name: dfr118_Results
  property_count: 2
  slug: echo-dfr-dfr118-results
- name: dfr119_Results
  property_count: 2
  slug: echo-dfr-dfr119-results
- name: dfr120_Results
  property_count: 2
  slug: echo-dfr-dfr120-results
- name: dfr122_Results
  property_count: 2
  slug: echo-dfr-dfr122-results
- name: dfr123_Results
  property_count: 3
  slug: echo-dfr-dfr123-results
- name: dfr124_Results
  property_count: 2
  slug: echo-dfr-dfr124-results
- name: dfr125_Results
  property_count: 2
  slug: echo-dfr-dfr125-results
- name: dfr126_Results
  property_count: 2
  slug: echo-dfr-dfr126-results
- name: dfr127_Results
  property_count: 2
  slug: echo-dfr-dfr127-results
- name: dfr128_Results
  property_count: 2
  slug: echo-dfr-dfr128-results
- name: dfr129_Results
  property_count: 2
  slug: echo-dfr-dfr129-results
- name: dfr130_Results
  property_count: 2
  slug: echo-dfr-dfr130-results
- name: dfr131_Results
  property_count: 2
  slug: echo-dfr-dfr131-results
- name: dfr132_Results
  property_count: 2
  slug: echo-dfr-dfr132-results
- name: dfr133_Results
  property_count: 2
  slug: echo-dfr-dfr133-results
- name: dfr134_Results
  property_count: 2
  slug: echo-dfr-dfr134-results
- name: dfr135_Results
  property_count: 2
  slug: echo-dfr-dfr135-results
- name: dfr136_Results
  property_count: 2
  slug: echo-dfr-dfr136-results
- name: eff01
  property_count: 41
  slug: echo-effluent-eff01
- name: eff02
  property_count: 11
  slug: echo-effluent-eff02
- name: eff03
  property_count: 7
  slug: echo-effluent-eff03
- name: eff04
  property_count: 4
  slug: echo-effluent-eff04
- name: eff05
  property_count: 17
  slug: echo-effluent-eff05
- name: eff06
  property_count: 10
  slug: echo-effluent-eff06
- name: eff07
  property_count: 4
  slug: echo-effluent-eff07
- name: eff08
  property_count: 4
  slug: echo-effluent-eff08
- name: eff09
  property_count: 18
  slug: echo-effluent-eff09
- name: rlup01
  property_count: 2
  slug: echo-effluent-rlup01
- name: rlup23
  property_count: 2
  slug: echo-effluent-rlup23
- name: geo
  property_count: 2
  slug: echo-rcra-geo
- name: meta1
  property_count: 2
  slug: echo-rcra-meta1
- name: meta3
  property_count: 6
  slug: echo-rcra-meta3
- name: qp0
  property_count: 2
  slug: echo-rcra-qp0
- name: rcra01
  property_count: 119
  slug: echo-rcra-rcra01
- name: rcra02
  property_count: 10
  slug: echo-rcra-rcra02
- name: rcra03
  property_count: 4
  slug: echo-rcra-rcra03
- name: rcra04
  property_count: 15
  slug: echo-rcra-rcra04
- name: rcra05
  property_count: 17
  slug: echo-rcra-rcra05
- name: rcra06
  property_count: 1
  slug: echo-rcra-rcra06
- name: rcra07
  property_count: 120
  slug: echo-rcra-rcra07
- name: rcra08
  property_count: 19
  slug: echo-rcra-rcra08
- name: rcra09
  property_count: 3
  slug: echo-rcra-rcra09
- name: rcra10
  property_count: 117
  slug: echo-rcra-rcra10
- name: rcra11
  property_count: 10
  slug: echo-rcra-rcra11
- name: rcra12
  property_count: 4
  slug: echo-rcra-rcra12
- name: rcra13
  property_count: 5
  slug: echo-rcra-rcra13
- name: meta1
  property_count: 2
  slug: echo-sdw-meta1
- name: meta3
  property_count: 6
  slug: echo-sdw-meta3
- name: sdw02
  property_count: 5
  slug: echo-sdw-sdw02
- name: sdw03
  property_count: 14
  slug: echo-sdw-sdw03
- name: sdw04
  property_count: 77
  slug: echo-sdw-sdw04
- name: customSearch.keywordSearch
  property_count: 1
  slug: elg-search-custom-search.keyword-search
- name: customSearch.multiCriteriaSearchCriteria
  property_count: 1
  slug: elg-search-custom-search.multi-criteria-search-criteria
- name: customSearch.multiCriteriaSearch
  property_count: 1
  slug: elg-search-custom-search.multi-criteria-search
- name: glossary.contact
  property_count: 1
  slug: elg-search-glossary.contact
- name: glossary.help
  property_count: 1
  slug: elg-search-glossary.help
- name: glossary.list
  property_count: 1
  slug: elg-search-glossary.list
- name: limitation.read
  property_count: 1
  slug: elg-search-limitation.read
- name: pointSourceCategory.cfr
  property_count: 1
  slug: elg-search-point-source-category.cfr
- name: pointSourceCategory.citationHistory
  property_count: 1
  slug: elg-search-point-source-category.citation-history
- name: pointSourceCategory.definitions
  property_count: 1
  slug: elg-search-point-source-category.definitions
- name: pointSourceCategory.list
  property_count: 1
  slug: elg-search-point-source-category.list
- name: pointSourceCategory.read
  property_count: 1
  slug: elg-search-point-source-category.read
- name: pointSourceSubcategory.read
  property_count: 1
  slug: elg-search-point-source-subcategory.read
- name: pollutant.limitations
  property_count: 1
  slug: elg-search-pollutant.limitations
- name: pollutant.listCategories
  property_count: 1
  slug: elg-search-pollutant.list-categories
- name: pollutant.list
  property_count: 1
  slug: elg-search-pollutant.list
- name: pollutant.readCategory
  property_count: 1
  slug: elg-search-pollutant.read-category
- name: pollutant.read
  property_count: 1
  slug: elg-search-pollutant.read
- name: treatmentTechnology.categoryLimitations
  property_count: 1
  slug: elg-search-treatment-technology.category-limitations
- name: treatmentTechnology.limitations
  property_count: 1
  slug: elg-search-treatment-technology.limitations
- name: treatmentTechnology.listCategories
  property_count: 1
  slug: elg-search-treatment-technology.list-categories
- name: treatmentTechnology.list
  property_count: 1
  slug: elg-search-treatment-technology.list
- name: treatmentTechnology.readCategory
  property_count: 1
  slug: elg-search-treatment-technology.read-category
- name: treatmentTechnology.read
  property_count: 1
  slug: elg-search-treatment-technology.read
- name: wastestreamProcess.limitations
  property_count: 1
  slug: elg-search-wastestream-process.limitations
- name: Row
  property_count: 0
  slug: envirofacts-row
- name: UvDaily
  property_count: 5
  slug: envirofacts-uv-daily
- name: UvHourly
  property_count: 5
  slug: envirofacts-uv-hourly
- name: generic
  property_count: 1
  slug: mywaterway-generic
json_structures:
- name: Aqs Envelope Structure
  property_count: 2
  slug: aqs-envelope-structure
- name: Aqs Header Structure
  property_count: 5
  slug: aqs-header-structure
- name: Cam Account Account Attributes Dto Structure
  property_count: 10
  slug: cam-account-account-attributes-dto-structure
- name: Cam Account Account Dto Structure
  property_count: 2
  slug: cam-account-account-dto-structure
- name: Cam Account Allowance Compliance Dto Structure
  property_count: 22
  slug: cam-account-allowance-compliance-dto-structure
- name: Cam Account Allowance Holdings Dto Structure
  property_count: 12
  slug: cam-account-allowance-holdings-dto-structure
- name: Cam Account Allowance Transactions Dto Structure
  property_count: 27
  slug: cam-account-allowance-transactions-dto-structure
- name: Cam Account Applicable Account Attributes Dto Structure
  property_count: 6
  slug: cam-account-applicable-account-attributes-dto-structure
- name: Cam Account Applicable Allowance Compliance Attributes Dto Structure
  property_count: 5
  slug: cam-account-applicable-allowance-compliance-attributes-dto-structure
- name: Cam Account Applicable Allowance Holdings Attributes Dto Structure
  property_count: 7
  slug: cam-account-applicable-allowance-holdings-attributes-dto-structure
- name: Cam Account Applicable Allowance Transactions Attributes Dto Structure
  property_count: 13
  slug: cam-account-applicable-allowance-transactions-attributes-dto-structure
- name: Cam Account Applicable Compliance Attributes Dto Structure
  property_count: 4
  slug: cam-account-applicable-compliance-attributes-dto-structure
- name: Cam Account Emissions Compliance Dto Structure
  property_count: 12
  slug: cam-account-emissions-compliance-dto-structure
- name: Cam Account Owner Operators Dto Structure
  property_count: 2
  slug: cam-account-owner-operators-dto-structure
- name: Cam Camd Services Bulk File Dto Structure
  property_count: 8
  slug: cam-camd-services-bulk-file-dto-structure
- name: Cam Camd Services Email Recipient List Request Dto Structure
  property_count: 2
  slug: cam-camd-services-email-recipient-list-request-dto-structure
- name: Cam Camd Services Email Recipient List Response Dto Structure
  property_count: 3
  slug: cam-camd-services-email-recipient-list-response-dto-structure
- name: Cam Camd Services Report Column Dto Structure
  property_count: 2
  slug: cam-camd-services-report-column-dto-structure
- name: Cam Camd Services Report Detail Dto Structure
  property_count: 4
  slug: cam-camd-services-report-detail-dto-structure
- name: Cam Camd Services Report Dto Structure
  property_count: 3
  slug: cam-camd-services-report-dto-structure
- name: Cam Emissions Annual Apportioned Emissions Aggregation Dto Structure
  property_count: 7
  slug: cam-emissions-annual-apportioned-emissions-aggregation-dto-structure
- name: Cam Emissions Annual Apportioned Emissions Facility Aggregation Dto Structure
  property_count: 10
  slug: cam-emissions-annual-apportioned-emissions-facility-aggregation-dto-structure
- name: Cam Emissions Annual Apportioned Emissions State Aggregation Dto Structure
  property_count: 8
  slug: cam-emissions-annual-apportioned-emissions-state-aggregation-dto-structure
- name: Cam Emissions Annual Unit Data View Structure
  property_count: 26
  slug: cam-emissions-annual-unit-data-view-structure
- name: Cam Emissions Applicable Apportioned Emissions Attributes Dto Structure
  property_count: 7
  slug: cam-emissions-applicable-apportioned-emissions-attributes-dto-structure
- name: Cam Emissions Daily Apportioned Emissions Facility Aggregation Dto Structure
  property_count: 10
  slug: cam-emissions-daily-apportioned-emissions-facility-aggregation-dto-structure
- name: Cam Emissions Daily Apportioned Emissions National Aggregation Dto Structure
  property_count: 7
  slug: cam-emissions-daily-apportioned-emissions-national-aggregation-dto-structure
- name: Cam Emissions Daily Apportioned Emissions State Aggregation Dto Structure
  property_count: 8
  slug: cam-emissions-daily-apportioned-emissions-state-aggregation-dto-structure
- name: Cam Emissions Day Unit Data View Structure
  property_count: 25
  slug: cam-emissions-day-unit-data-view-structure
- name: Cam Emissions Emissions Review Dto Structure
  property_count: 15
  slug: cam-emissions-emissions-review-dto-structure
- name: Cam Emissions Emissions Submissions Progress Dto Structure
  property_count: 4
  slug: cam-emissions-emissions-submissions-progress-dto-structure
- name: Cam Emissions Emissions View Dto Structure
  property_count: 2
  slug: cam-emissions-emissions-view-dto-structure
- name: Cam Emissions Hour Unit Data View Structure
  property_count: 34
  slug: cam-emissions-hour-unit-data-view-structure
- name: Cam Emissions Hour Unit Mats Data View Structure
  property_count: 30
  slug: cam-emissions-hour-unit-mats-data-view-structure
- name: Cam Emissions Hourly Apportioned Emissions Dto Structure
  property_count: 34
  slug: cam-emissions-hourly-apportioned-emissions-dto-structure
- name: Cam Emissions Hourly Apportioned Emissions Facility Aggregation Dto Structure
  property_count: 11
  slug: cam-emissions-hourly-apportioned-emissions-facility-aggregation-dto-structure
- name: Cam Emissions Hourly Apportioned Emissions National Aggregation Dto Structure
  property_count: 8
  slug: cam-emissions-hourly-apportioned-emissions-national-aggregation-dto-structure
- name: Cam Emissions Hourly Apportioned Emissions State Aggregation Dto Structure
  property_count: 9
  slug: cam-emissions-hourly-apportioned-emissions-state-aggregation-dto-structure
- name: Cam Emissions Hourly Mats Apportioned Emissions Dto Structure
  property_count: 30
  slug: cam-emissions-hourly-mats-apportioned-emissions-dto-structure
- name: Cam Emissions Month Unit Data View Structure
  property_count: 26
  slug: cam-emissions-month-unit-data-view-structure
- name: Cam Emissions Monthly Apportioned Emissions Facility Aggregation Dto Structure
  property_count: 11
  slug: cam-emissions-monthly-apportioned-emissions-facility-aggregation-dto-structure
- name: Cam Emissions Monthly Apportioned Emissions National Aggregation Dto Structure
  property_count: 8
  slug: cam-emissions-monthly-apportioned-emissions-national-aggregation-dto-structure
- name: Cam Emissions Monthly Apportioned Emissions State Aggregation Dto Structure
  property_count: 9
  slug: cam-emissions-monthly-apportioned-emissions-state-aggregation-dto-structure
- name: Cam Emissions Ozone Apportioned Emissions Facility Aggregation Dto Structure
  property_count: 10
  slug: cam-emissions-ozone-apportioned-emissions-facility-aggregation-dto-structure
- name: Cam Emissions Ozone Apportioned Emissions National Aggregation Dto Structure
  property_count: 7
  slug: cam-emissions-ozone-apportioned-emissions-national-aggregation-dto-structure
- name: Cam Emissions Ozone Apportioned Emissions State Aggregation Dto Structure
  property_count: 8
  slug: cam-emissions-ozone-apportioned-emissions-state-aggregation-dto-structure
- name: Cam Emissions Ozone Unit Data View Structure
  property_count: 26
  slug: cam-emissions-ozone-unit-data-view-structure
- name: Cam Emissions Quarter Unit Data View Structure
  property_count: 27
  slug: cam-emissions-quarter-unit-data-view-structure
- name: Cam Emissions Quarterly Apportioned Emissions Facility Aggregation Dto Structure
  property_count: 11
  slug: cam-emissions-quarterly-apportioned-emissions-facility-aggregation-dto-structure
- name: Cam Emissions Quarterly Apportioned Emissions National Aggregation Dto Structure
  property_count: 8
  slug: cam-emissions-quarterly-apportioned-emissions-national-aggregation-dto-structure
- name: Cam Emissions Quarterly Apportioned Emissions State Aggregation Dto Structure
  property_count: 9
  slug: cam-emissions-quarterly-apportioned-emissions-state-aggregation-dto-structure
- name: Cam Facilities Applicable Facility Attributes Dto Structure
  property_count: 8
  slug: cam-facilities-applicable-facility-attributes-dto-structure
- name: Cam Facilities Facility Attributes Dto Structure
  property_count: 30
  slug: cam-facilities-facility-attributes-dto-structure
- name: Cam Facilities Facility Dto Structure
  property_count: 5
  slug: cam-facilities-facility-dto-structure
- name: Cam Master Data Account Type Dto Structure
  property_count: 4
  slug: cam-master-data-account-type-dto-structure
- name: Cam Master Data Code Table Dto Structure
  property_count: 2
  slug: cam-master-data-code-table-dto-structure
- name: Cam Master Data Control Technology Dto Structure
  property_count: 4
  slug: cam-master-data-control-technology-dto-structure
- name: Cam Master Data Data Column Dto Structure
  property_count: 4
  slug: cam-master-data-data-column-dto-structure
- name: Cam Master Data Data Set Dto Structure
  property_count: 5
  slug: cam-master-data-data-set-dto-structure
- name: Cam Master Data Data Table Dto Structure
  property_count: 4
  slug: cam-master-data-data-table-dto-structure
- name: Cam Master Data Fuel Type Dto Structure
  property_count: 4
  slug: cam-master-data-fuel-type-dto-structure
- name: Cam Master Data Program Dto Structure
  property_count: 12
  slug: cam-master-data-program-dto-structure
- name: Cam Master Data Reporting Period Dto Structure
  property_count: 8
  slug: cam-master-data-reporting-period-dto-structure
- name: Cam Master Data Unit Type Dto Structure
  property_count: 5
  slug: cam-master-data-unit-type-dto-structure
- name: Cam Monitor Plan Analyzer Range Dto Structure
  property_count: 12
  slug: cam-monitor-plan-analyzer-range-dto-structure
- name: Cam Monitor Plan Analyzer Range Structure
  property_count: 12
  slug: cam-monitor-plan-analyzer-range-structure
- name: Cam Monitor Plan Component Dto Structure
  property_count: 14
  slug: cam-monitor-plan-component-dto-structure
- name: Cam Monitor Plan Component Structure
  property_count: 16
  slug: cam-monitor-plan-component-structure
- name: Cam Monitor Plan Duct Waf Dto Structure
  property_count: 19
  slug: cam-monitor-plan-duct-waf-dto-structure
- name: Cam Monitor Plan Duct Waf Structure
  property_count: 19
  slug: cam-monitor-plan-duct-waf-structure
- name: Cam Monitor Plan Emission Evaluation Structure
  property_count: 10
  slug: cam-monitor-plan-emission-evaluation-structure
- name: Cam Monitor Plan Last Updated Config Dto Structure
  property_count: 2
  slug: cam-monitor-plan-last-updated-config-dto-structure
- name: Cam Monitor Plan Leequalification Dto Structure
  property_count: 12
  slug: cam-monitor-plan-leequalification-dto-structure
- name: Cam Monitor Plan Leequalification Structure
  property_count: 13
  slug: cam-monitor-plan-leequalification-structure
- name: Cam Monitor Plan Lmequalification Dto Structure
  property_count: 9
  slug: cam-monitor-plan-lmequalification-dto-structure
- name: Cam Monitor Plan Lmequalification Structure
  property_count: 10
  slug: cam-monitor-plan-lmequalification-structure
- name: Cam Monitor Plan Mats Method Dto Structure
  property_count: 12
  slug: cam-monitor-plan-mats-method-dto-structure
- name: Cam Monitor Plan Mats Method Structure
  property_count: 12
  slug: cam-monitor-plan-mats-method-structure
- name: Cam Monitor Plan Monitor Attribute Dto Structure
  property_count: 16
  slug: cam-monitor-plan-monitor-attribute-dto-structure
- name: Cam Monitor Plan Monitor Attribute Structure
  property_count: 16
  slug: cam-monitor-plan-monitor-attribute-structure
- name: Cam Monitor Plan Monitor Default Dto Structure
  property_count: 18
  slug: cam-monitor-plan-monitor-default-dto-structure
- name: Cam Monitor Plan Monitor Default Structure
  property_count: 18
  slug: cam-monitor-plan-monitor-default-structure
- name: Cam Monitor Plan Monitor Formula Dto Structure
  property_count: 14
  slug: cam-monitor-plan-monitor-formula-dto-structure
- name: Cam Monitor Plan Monitor Formula Structure
  property_count: 14
  slug: cam-monitor-plan-monitor-formula-structure
- name: Cam Monitor Plan Monitor Load Dto Structure
  property_count: 18
  slug: cam-monitor-plan-monitor-load-dto-structure
- name: Cam Monitor Plan Monitor Load Structure
  property_count: 18
  slug: cam-monitor-plan-monitor-load-structure
- name: Cam Monitor Plan Monitor Location Dto Structure
  property_count: 25
  slug: cam-monitor-plan-monitor-location-dto-structure
- name: Cam Monitor Plan Monitor Location Structure
  property_count: 17
  slug: cam-monitor-plan-monitor-location-structure
- name: Cam Monitor Plan Monitor Method Dto Structure
  property_count: 14
  slug: cam-monitor-plan-monitor-method-dto-structure
- name: Cam Monitor Plan Monitor Method Structure
  property_count: 14
  slug: cam-monitor-plan-monitor-method-structure
- name: Cam Monitor Plan Monitor Plan Comment Dto Structure
  property_count: 9
  slug: cam-monitor-plan-monitor-plan-comment-dto-structure
- name: Cam Monitor Plan Monitor Plan Comment Structure
  property_count: 9
  slug: cam-monitor-plan-monitor-plan-comment-structure
- name: Cam Monitor Plan Monitor Plan Dto Structure
  property_count: 33
  slug: cam-monitor-plan-monitor-plan-dto-structure
- name: Cam Monitor Plan Monitor Plan Reporting Freq Dto Structure
  property_count: 9
  slug: cam-monitor-plan-monitor-plan-reporting-freq-dto-structure
- name: Cam Monitor Plan Monitor Plan Reporting Frequency Structure
  property_count: 11
  slug: cam-monitor-plan-monitor-plan-reporting-frequency-structure
- name: Cam Monitor Plan Monitor Plan Structure
  property_count: 26
  slug: cam-monitor-plan-monitor-plan-structure
- name: Cam Monitor Plan Monitor Qualification Dto Structure
  property_count: 12
  slug: cam-monitor-plan-monitor-qualification-dto-structure
- name: Cam Monitor Plan Monitor Qualification Structure
  property_count: 12
  slug: cam-monitor-plan-monitor-qualification-structure
- name: Cam Monitor Plan Monitor Span Dto Structure
  property_count: 23
  slug: cam-monitor-plan-monitor-span-dto-structure
- name: Cam Monitor Plan Monitor Span Structure
  property_count: 23
  slug: cam-monitor-plan-monitor-span-structure
- name: Cam Monitor Plan Monitor System Dto Structure
  property_count: 16
  slug: cam-monitor-plan-monitor-system-dto-structure
- name: Cam Monitor Plan Monitor System Structure
  property_count: 16
  slug: cam-monitor-plan-monitor-system-structure
- name: Cam Monitor Plan Pctqualification Dto Structure
  property_count: 16
  slug: cam-monitor-plan-pctqualification-dto-structure
- name: Cam Monitor Plan Pctqualification Structure
  property_count: 17
  slug: cam-monitor-plan-pctqualification-structure
- name: Cam Monitor Plan Plant Structure
  property_count: 10
  slug: cam-monitor-plan-plant-structure
- name: Cam Monitor Plan Program Code Structure
  property_count: 26
  slug: cam-monitor-plan-program-code-structure
- name: Cam Monitor Plan Program Structure
  property_count: 15
  slug: cam-monitor-plan-program-structure
- name: Cam Monitor Plan Reporting Freq Dto Structure
  property_count: 6
  slug: cam-monitor-plan-reporting-freq-dto-structure
- name: Cam Monitor Plan Reporting Period Structure
  property_count: 8
  slug: cam-monitor-plan-reporting-period-structure
- name: Cam Monitor Plan Stack Pipe Structure
  property_count: 8
  slug: cam-monitor-plan-stack-pipe-structure
- name: Cam Monitor Plan System Component Dto Structure
  property_count: 12
  slug: cam-monitor-plan-system-component-dto-structure
- name: Cam Monitor Plan System Component Structure
  property_count: 12
  slug: cam-monitor-plan-system-component-structure
- name: Cam Monitor Plan System Fuel Flow Dto Structure
  property_count: 15
  slug: cam-monitor-plan-system-fuel-flow-dto-structure
- name: Cam Monitor Plan System Fuel Flow Structure
  property_count: 13
  slug: cam-monitor-plan-system-fuel-flow-structure
- name: Cam Monitor Plan Unit Boiler Type Structure
  property_count: 8
  slug: cam-monitor-plan-unit-boiler-type-structure
- name: Cam Monitor Plan Unit Capacity Dto Structure
  property_count: 14
  slug: cam-monitor-plan-unit-capacity-dto-structure
- name: Cam Monitor Plan Unit Capacity Structure
  property_count: 9
  slug: cam-monitor-plan-unit-capacity-structure
- name: Cam Monitor Plan Unit Control Dto Structure
  property_count: 13
  slug: cam-monitor-plan-unit-control-dto-structure
- name: Cam Monitor Plan Unit Control Structure
  property_count: 14
  slug: cam-monitor-plan-unit-control-structure
- name: Cam Monitor Plan Unit Dto Structure
  property_count: 18
  slug: cam-monitor-plan-unit-dto-structure
- name: Cam Monitor Plan Unit Fuel Dto Structure
  property_count: 15
  slug: cam-monitor-plan-unit-fuel-dto-structure
- name: Cam Monitor Plan Unit Fuel Structure
  property_count: 15
  slug: cam-monitor-plan-unit-fuel-structure
- name: Cam Monitor Plan Unit Op Status Structure
  property_count: 6
  slug: cam-monitor-plan-unit-op-status-structure
- name: Cam Monitor Plan Unit Program Dto Structure
  property_count: 13
  slug: cam-monitor-plan-unit-program-dto-structure
- name: Cam Monitor Plan Unit Program Structure
  property_count: 23
  slug: cam-monitor-plan-unit-program-structure
- name: Cam Monitor Plan Unit Stack Configuration Dto Structure
  property_count: 11
  slug: cam-monitor-plan-unit-stack-configuration-dto-structure
- name: Cam Monitor Plan Unit Stack Configuration Structure
  property_count: 10
  slug: cam-monitor-plan-unit-stack-configuration-structure
- name: Cam Monitor Plan Unit Structure
  property_count: 19
  slug: cam-monitor-plan-unit-structure
- name: Cam Qa Cert Air Emission Testing Dto Structure
  property_count: 14
  slug: cam-qa-cert-air-emission-testing-dto-structure
- name: Cam Qa Cert App Ecorrelation Test Run Base Dto Structure
  property_count: 11
  slug: cam-qa-cert-app-ecorrelation-test-run-base-dto-structure
- name: Cam Qa Cert App Ecorrelation Test Run Dto Structure
  property_count: 20
  slug: cam-qa-cert-app-ecorrelation-test-run-dto-structure
- name: Cam Qa Cert App Ecorrelation Test Run Record Dto Structure
  property_count: 18
  slug: cam-qa-cert-app-ecorrelation-test-run-record-dto-structure
- name: Cam Qa Cert App Ecorrelation Test Summary Dto Structure
  property_count: 12
  slug: cam-qa-cert-app-ecorrelation-test-summary-dto-structure
- name: Cam Qa Cert App Ecorrelation Test Summary Record Dto Structure
  property_count: 11
  slug: cam-qa-cert-app-ecorrelation-test-summary-record-dto-structure
- name: Cam Qa Cert App Eheat Input From Gas Dto Structure
  property_count: 10
  slug: cam-qa-cert-app-eheat-input-from-gas-dto-structure
- name: Cam Qa Cert App Eheat Input From Gas Record Dto Structure
  property_count: 10
  slug: cam-qa-cert-app-eheat-input-from-gas-record-dto-structure
- name: Cam Qa Cert App Eheat Input From Oil Dto Structure
  property_count: 16
  slug: cam-qa-cert-app-eheat-input-from-oil-dto-structure
- name: Cam Qa Cert App Eheat Input From Oil Record Dto Structure
  property_count: 16
  slug: cam-qa-cert-app-eheat-input-from-oil-record-dto-structure
- name: Cam Qa Cert Calibration Injection Dto Structure
  property_count: 25
  slug: cam-qa-cert-calibration-injection-dto-structure
- name: Cam Qa Cert Cert Event Review And Submit Dto Structure
  property_count: 22
  slug: cam-qa-cert-cert-event-review-and-submit-dto-structure
- name: Cam Qa Cert Cycle Time Injection Dto Structure
  property_count: 17
  slug: cam-qa-cert-cycle-time-injection-dto-structure
- name: Cam Qa Cert Cycle Time Injection Record Dto Structure
  property_count: 17
  slug: cam-qa-cert-cycle-time-injection-record-dto-structure
- name: Cam Qa Cert Cycle Time Summary Dto Structure
  property_count: 8
  slug: cam-qa-cert-cycle-time-summary-dto-structure
- name: Cam Qa Cert Flow Rata Run Dto Structure
  property_count: 23
  slug: cam-qa-cert-flow-rata-run-dto-structure
- name: Cam Qa Cert Flow To Load Check Dto Structure
  property_count: 16
  slug: cam-qa-cert-flow-to-load-check-dto-structure
- name: Cam Qa Cert Flow To Load Check Record Dto Structure
  property_count: 16
  slug: cam-qa-cert-flow-to-load-check-record-dto-structure
- name: Cam Qa Cert Flow To Load Reference Dto Structure
  property_count: 17
  slug: cam-qa-cert-flow-to-load-reference-dto-structure
- name: Cam Qa Cert Flow To Load Reference Record Dto Structure
  property_count: 17
  slug: cam-qa-cert-flow-to-load-reference-record-dto-structure
- name: Cam Qa Cert Fuel Flow To Load Baseline Dto Structure
  property_count: 17
  slug: cam-qa-cert-fuel-flow-to-load-baseline-dto-structure
- name: Cam Qa Cert Fuel Flow To Load Test Dto Structure
  property_count: 11
  slug: cam-qa-cert-fuel-flow-to-load-test-dto-structure
- name: Cam Qa Cert Fuel Flowmeter Accuracy Dto Structure
  property_count: 11
  slug: cam-qa-cert-fuel-flowmeter-accuracy-dto-structure
- name: Cam Qa Cert Fuel Flowmeter Accuracy Record Dto Structure
  property_count: 11
  slug: cam-qa-cert-fuel-flowmeter-accuracy-record-dto-structure
- name: Cam Qa Cert Hg Injection Dto Structure
  property_count: 10
  slug: cam-qa-cert-hg-injection-dto-structure
- name: Cam Qa Cert Hg Injection Record Dto Structure
  property_count: 10
  slug: cam-qa-cert-hg-injection-record-dto-structure
- name: Cam Qa Cert Hg Summary Dto Structure
  property_count: 15
  slug: cam-qa-cert-hg-summary-dto-structure
- name: Cam Qa Cert Linearity Injection Dto Structure
  property_count: 10
  slug: cam-qa-cert-linearity-injection-dto-structure
- name: Cam Qa Cert Linearity Injection Record Dto Structure
  property_count: 10
  slug: cam-qa-cert-linearity-injection-record-dto-structure
- name: Cam Qa Cert Linearity Summary Dto Structure
  property_count: 15
  slug: cam-qa-cert-linearity-summary-dto-structure
- name: Cam Qa Cert Linearity Summary Record Dto Structure
  property_count: 14
  slug: cam-qa-cert-linearity-summary-record-dto-structure
- name: Cam Qa Cert Online Offline Calibration Dto Structure
  property_count: 30
  slug: cam-qa-cert-online-offline-calibration-dto-structure
- name: Cam Qa Cert Online Offline Calibration Record Dto Structure
  property_count: 30
  slug: cam-qa-cert-online-offline-calibration-record-dto-structure
- name: Cam Qa Cert Protocol Gas Dto Structure
  property_count: 10
  slug: cam-qa-cert-protocol-gas-dto-structure
- name: Cam Qa Cert Protocol Gas Record Dto Structure
  property_count: 10
  slug: cam-qa-cert-protocol-gas-record-dto-structure
- name: Cam Qa Cert Qacertification Dto Structure
  property_count: 4
  slug: cam-qa-cert-qacertification-dto-structure
- name: Cam Qa Cert Qacertification Event Dto Structure
  property_count: 28
  slug: cam-qa-cert-qacertification-event-dto-structure
- name: Cam Qa Cert Rata Dto Structure
  property_count: 14
  slug: cam-qa-cert-rata-dto-structure
- name: Cam Qa Cert Rata Record Dto Structure
  property_count: 13
  slug: cam-qa-cert-rata-record-dto-structure
- name: Cam Qa Cert Rata Run Dto Structure
  property_count: 18
  slug: cam-qa-cert-rata-run-dto-structure
- name: Cam Qa Cert Rata Summary Dto Structure
  property_count: 37
  slug: cam-qa-cert-rata-summary-dto-structure
- name: Cam Qa Cert Rata Summary Record Dto Structure
  property_count: 36
  slug: cam-qa-cert-rata-summary-record-dto-structure
- name: Cam Qa Cert Rata Traverse Dto Structure
  property_count: 21
  slug: cam-qa-cert-rata-traverse-dto-structure
- name: Cam Qa Cert Rata Traverse Record Dto Structure
  property_count: 21
  slug: cam-qa-cert-rata-traverse-record-dto-structure
- name: Cam Qa Cert Review And Submit Test Summary Dto Structure
  property_count: 19
  slug: cam-qa-cert-review-and-submit-test-summary-dto-structure
- name: Cam Qa Cert Tee Review And Submit Dto Structure
  property_count: 21
  slug: cam-qa-cert-tee-review-and-submit-dto-structure
- name: Cam Qa Cert Test Extension Exemption Dto Structure
  property_count: 23
  slug: cam-qa-cert-test-extension-exemption-dto-structure
- name: Cam Qa Cert Test Extension Exemption Record Dto Structure
  property_count: 23
  slug: cam-qa-cert-test-extension-exemption-record-dto-structure
- name: Cam Qa Cert Test Qualification Dto Structure
  property_count: 11
  slug: cam-qa-cert-test-qualification-dto-structure
- name: Cam Qa Cert Test Qualification Record Dto Structure
  property_count: 11
  slug: cam-qa-cert-test-qualification-record-dto-structure
- name: Cam Qa Cert Test Summary Dto Structure
  property_count: 51
  slug: cam-qa-cert-test-summary-dto-structure
- name: Cam Qa Cert Test Summary Record Dto Structure
  property_count: 34
  slug: cam-qa-cert-test-summary-record-dto-structure
- name: Cam Qa Cert Transmitter Transducer Accuracy Dto Structure
  property_count: 11
  slug: cam-qa-cert-transmitter-transducer-accuracy-dto-structure
- name: Cam Qa Cert Unit Default Test Dto Structure
  property_count: 13
  slug: cam-qa-cert-unit-default-test-dto-structure
- name: Cam Qa Cert Unit Default Test Record Dto Structure
  property_count: 12
  slug: cam-qa-cert-unit-default-test-record-dto-structure
- name: Cam Qa Cert Unit Default Test Run Dto Structure
  property_count: 16
  slug: cam-qa-cert-unit-default-test-run-dto-structure
- name: Cam Qa Cert Unit Default Test Run Record Dto Structure
  property_count: 16
  slug: cam-qa-cert-unit-default-test-run-record-dto-structure
- name: Cam Streaming Account Attributes Dto Structure
  property_count: 10
  slug: cam-streaming-account-attributes-dto-structure
- name: Cam Streaming Allowance Compliance Dto Structure
  property_count: 22
  slug: cam-streaming-allowance-compliance-dto-structure
- name: Cam Streaming Allowance Holdings Dto Structure
  property_count: 12
  slug: cam-streaming-allowance-holdings-dto-structure
- name: Cam Streaming Allowance Transactions Dto Structure
  property_count: 27
  slug: cam-streaming-allowance-transactions-dto-structure
- name: Cam Streaming Annual Apportioned Emissions Aggregation Dto Structure
  property_count: 7
  slug: cam-streaming-annual-apportioned-emissions-aggregation-dto-structure
- name: Cam Streaming Annual Apportioned Emissions Dto Structure
  property_count: 29
  slug: cam-streaming-annual-apportioned-emissions-dto-structure
- name: Cam Streaming Annual Apportioned Emissions Facility Aggregation Dto Structure
  property_count: 10
  slug: cam-streaming-annual-apportioned-emissions-facility-aggregation-dto-structure
- name: Cam Streaming Annual Apportioned Emissions State Aggregation Dto Structure
  property_count: 8
  slug: cam-streaming-annual-apportioned-emissions-state-aggregation-dto-structure
- name: Cam Streaming Daily Apportioned Emissions Dto Structure
  property_count: 27
  slug: cam-streaming-daily-apportioned-emissions-dto-structure
- name: Cam Streaming Daily Apportioned Emissions Facility Aggregation Dto Structure
  property_count: 10
  slug: cam-streaming-daily-apportioned-emissions-facility-aggregation-dto-structure
- name: Cam Streaming Daily Apportioned Emissions National Aggregation Dto Structure
  property_count: 7
  slug: cam-streaming-daily-apportioned-emissions-national-aggregation-dto-structure
- name: Cam Streaming Daily Apportioned Emissions State Aggregation Dto Structure
  property_count: 8
  slug: cam-streaming-daily-apportioned-emissions-state-aggregation-dto-structure
- name: Cam Streaming Derived Hourly Value Base Dto Structure
  property_count: 10
  slug: cam-streaming-derived-hourly-value-base-dto-structure
- name: Cam Streaming Emissions Compliance Dto Structure
  property_count: 12
  slug: cam-streaming-emissions-compliance-dto-structure
- name: Cam Streaming Facility Attributes Dto Structure
  property_count: 30
  slug: cam-streaming-facility-attributes-dto-structure
- name: Cam Streaming Hourly Apportioned Emissions Dto Structure
  property_count: 34
  slug: cam-streaming-hourly-apportioned-emissions-dto-structure
- name: Cam Streaming Hourly Apportioned Emissions Facility Aggregation Dto Structure
  property_count: 11
  slug: cam-streaming-hourly-apportioned-emissions-facility-aggregation-dto-structure
- name: Cam Streaming Hourly Apportioned Emissions National Aggregation Dto Structure
  property_count: 8
  slug: cam-streaming-hourly-apportioned-emissions-national-aggregation-dto-structure
- name: Cam Streaming Hourly Apportioned Emissions State Aggregation Dto Structure
  property_count: 9
  slug: cam-streaming-hourly-apportioned-emissions-state-aggregation-dto-structure
- name: Cam Streaming Hourly Mats Apportioned Emissions Dto Structure
  property_count: 31
  slug: cam-streaming-hourly-mats-apportioned-emissions-dto-structure
- name: Cam Streaming Hourly Operating Dto Structure
  property_count: 11
  slug: cam-streaming-hourly-operating-dto-structure
- name: Cam Streaming Monthly Apportioned Emissions Dto Structure
  property_count: 28
  slug: cam-streaming-monthly-apportioned-emissions-dto-structure
- name: Cam Streaming Monthly Apportioned Emissions Facility Aggregation Dto Structure
  property_count: 11
  slug: cam-streaming-monthly-apportioned-emissions-facility-aggregation-dto-structure
- name: Cam Streaming Monthly Apportioned Emissions National Aggregation Dto Structure
  property_count: 8
  slug: cam-streaming-monthly-apportioned-emissions-national-aggregation-dto-structure
- name: Cam Streaming Monthly Apportioned Emissions State Aggregation Dto Structure
  property_count: 9
  slug: cam-streaming-monthly-apportioned-emissions-state-aggregation-dto-structure
- name: Cam Streaming Ozone Apportioned Emissions Dto Structure
  property_count: 29
  slug: cam-streaming-ozone-apportioned-emissions-dto-structure
- name: Cam Streaming Ozone Apportioned Emissions Facility Aggregation Dto Structure
  property_count: 10
  slug: cam-streaming-ozone-apportioned-emissions-facility-aggregation-dto-structure
- name: Cam Streaming Ozone Apportioned Emissions National Aggregation Dto Structure
  property_count: 7
  slug: cam-streaming-ozone-apportioned-emissions-national-aggregation-dto-structure
- name: Cam Streaming Ozone Apportioned Emissions State Aggregation Dto Structure
  property_count: 8
  slug: cam-streaming-ozone-apportioned-emissions-state-aggregation-dto-structure
- name: Cam Streaming Quarterly Apportioned Emissions Dto Structure
  property_count: 28
  slug: cam-streaming-quarterly-apportioned-emissions-dto-structure
- name: Cam Streaming Quarterly Apportioned Emissions Facility Aggregation Dto Structure
  property_count: 11
  slug: cam-streaming-quarterly-apportioned-emissions-facility-aggregation-dto-structure
- name: Cam Streaming Quarterly Apportioned Emissions National Aggregation Dto Structure
  property_count: 8
  slug: cam-streaming-quarterly-apportioned-emissions-national-aggregation-dto-structure
- name: Cam Streaming Quarterly Apportioned Emissions State Aggregation Dto Structure
  property_count: 9
  slug: cam-streaming-quarterly-apportioned-emissions-state-aggregation-dto-structure
- name: Cam Streaming Summary Value Base Dto Structure
  property_count: 10
  slug: cam-streaming-summary-value-base-dto-structure
- name: Cam Streaming Supplemental Operating Dto Structure
  property_count: 9
  slug: cam-streaming-supplemental-operating-dto-structure
- name: Cip Service Aggregation Engine Structure
  property_count: 0
  slug: cip-service-aggregation-engine-structure
- name: Cip Service Cipsrv Domains State Structure
  property_count: 3
  slug: cip-service-cipsrv-domains-state-structure
- name: Cip Service Cipsrv Domains States Structure
  property_count: 0
  slug: cip-service-cipsrv-domains-states-structure
- name: Cip Service Cipsrv Domains Structure
  property_count: 2
  slug: cip-service-cipsrv-domains-structure
- name: Cip Service Cipsrv Domains Tribe Structure
  property_count: 4
  slug: cip-service-cipsrv-domains-tribe-structure
- name: Cip Service Cipsrv Domains Tribes Structure
  property_count: 0
  slug: cip-service-cipsrv-domains-tribes-structure
- name: Cip Service Cipsrv Index Rb Structure
  property_count: 29
  slug: cip-service-cipsrv-index-rb-structure
- name: Cip Service Cipsrv Index Resp Structure
  property_count: 13
  slug: cip-service-cipsrv-index-resp-structure
- name: Cip Service Cipsrv Registry Components Structure
  property_count: 6
  slug: cip-service-cipsrv-registry-components-structure
- name: Cip Service Cipsrv Registry Structure
  property_count: 4
  slug: cip-service-cipsrv-registry-structure
- name: Cip Service Coordinates1 Structure
  property_count: 0
  slug: cip-service-coordinates1-structure
- name: Cip Service Coordinates2 Structure
  property_count: 0
  slug: cip-service-coordinates2-structure
- name: Cip Service Coordinates3 Structure
  property_count: 0
  slug: cip-service-coordinates3-structure
- name: Cip Service Delineate Rb Structure
  property_count: 20
  slug: cip-service-delineate-rb-structure
- name: Cip Service Delineate Resp Structure
  property_count: 7
  slug: cip-service-delineate-resp-structure
- name: Cip Service Delineated Area Properties Structure
  property_count: 4
  slug: cip-service-delineated-area-properties-structure
- name: Cip Service End Point Properties Structure
  property_count: 3
  slug: cip-service-end-point-properties-structure
- name: Cip Service Event Feature Properties Structure
  property_count: 8
  slug: cip-service-event-feature-properties-structure
- name: Cip Service Fcode Allow Structure
  property_count: 0
  slug: cip-service-fcode-allow-structure
- name: Cip Service Fcode Deny Structure
  property_count: 0
  slug: cip-service-fcode-deny-structure
- name: Cip Service Fill Basin Holes Structure
  property_count: 0
  slug: cip-service-fill-basin-holes-structure
- name: Cip Service Flow Accumulation Rb Structure
  property_count: 6
  slug: cip-service-flow-accumulation-rb-structure
- name: Cip Service Flow Accumulation Resp Structure
  property_count: 11
  slug: cip-service-flow-accumulation-resp-structure
- name: Cip Service Flowline Count Structure
  property_count: 0
  slug: cip-service-flowline-count-structure
- name: Cip Service Geojson Bbox Structure
  property_count: 0
  slug: cip-service-geojson-bbox-structure
- name: Cip Service Geojson Feature Structure
  property_count: 5
  slug: cip-service-geojson-feature-structure
- name: Cip Service Geojson Featurecollection Structure
  property_count: 2
  slug: cip-service-geojson-featurecollection-structure
- name: Cip Service Geojson Geometry Structure
  property_count: 2
  slug: cip-service-geojson-geometry-structure
- name: Cip Service Globalid Structure
  property_count: 0
  slug: cip-service-globalid-structure
- name: Cip Service Hydroseq Structure
  property_count: 0
  slug: cip-service-hydroseq-structure
- name: Cip Service Image Format Structure
  property_count: 0
  slug: cip-service-image-format-structure
- name: Cip Service Indexed Catchment Properties Structure
  property_count: 4
  slug: cip-service-indexed-catchment-properties-structure
- name: Cip Service Indexed Flowline Properties Structure
  property_count: 6
  slug: cip-service-indexed-flowline-properties-structure
- name: Cip Service Indexing Engine Structure
  property_count: 0
  slug: cip-service-indexing-engine-structure
- name: Cip Service Indexing Line Properties Structure
  property_count: 1
  slug: cip-service-indexing-line-properties-structure
- name: Cip Service Indexing Summary Structure
  property_count: 1
  slug: cip-service-indexing-summary-structure
- name: Cip Service Known Region Structure
  property_count: 0
  slug: cip-service-known-region-structure
- name: Cip Service Linked Data Program Structure
  property_count: 0
  slug: cip-service-linked-data-program-structure
- name: Cip Service Linked Data Wqp Structure
  property_count: 41
  slug: cip-service-linked-data-wqp-structure
- name: Cip Service Max Distancekm Structure
  property_count: 0
  slug: cip-service-max-distancekm-structure
- name: Cip Service Max Flowtimeday Structure
  property_count: 0
  slug: cip-service-max-flowtimeday-structure
- name: Cip Service Measure Structure
  property_count: 0
  slug: cip-service-measure-structure
- name: Cip Service Navigate Rb Structure
  property_count: 17
  slug: cip-service-navigate-rb-structure
- name: Cip Service Navigate Resp Structure
  property_count: 5
  slug: cip-service-navigate-resp-structure
- name: Cip Service Navigated Flowline Properties Structure
  property_count: 20
  slug: cip-service-navigated-flowline-properties-structure
- name: Cip Service Nhdplus Version Structure
  property_count: 0
  slug: cip-service-nhdplus-version-structure
- name: Cip Service Nhdplusid Structure
  property_count: 0
  slug: cip-service-nhdplusid-structure
- name: Cip Service Ordinate Structure
  property_count: 0
  slug: cip-service-ordinate-structure
- name: Cip Service Permanent Identifier Structure
  property_count: 0
  slug: cip-service-permanent-identifier-structure
- name: Cip Service Pointindexing Rb Structure
  property_count: 13
  slug: cip-service-pointindexing-rb-structure
- name: Cip Service Pointindexing Resp Structure
  property_count: 11
  slug: cip-service-pointindexing-resp-structure
- name: Cip Service Randomcatchment Rb Structure
  property_count: 1
  slug: cip-service-randomcatchment-rb-structure
- name: Cip Service Randomcatchment Resp Structure
  property_count: 1
  slug: cip-service-randomcatchment-resp-structure
- name: Cip Service Randomhuc12 Rb Structure
  property_count: 1
  slug: cip-service-randomhuc12-rb-structure
- name: Cip Service Randomhuc12 Resp Structure
  property_count: 1
  slug: cip-service-randomhuc12-resp-structure
- name: Cip Service Randomnav Rb Structure
  property_count: 1
  slug: cip-service-randomnav-rb-structure
- name: Cip Service Randomnav Resp Structure
  property_count: 1
  slug: cip-service-randomnav-resp-structure
- name: Cip Service Randompoint Rb Structure
  property_count: 1
  slug: cip-service-randompoint-rb-structure
- name: Cip Service Randompoint Resp Structure
  property_count: 1
  slug: cip-service-randompoint-resp-structure
- name: Cip Service Randomppnav Rb Structure
  property_count: 1
  slug: cip-service-randomppnav-rb-structure
- name: Cip Service Randomppnav Resp Structure
  property_count: 2
  slug: cip-service-randomppnav-resp-structure
- name: Cip Service Reachcode Structure
  property_count: 0
  slug: cip-service-reachcode-structure
- name: Cip Service Return Code Structure
  property_count: 0
  slug: cip-service-return-code-structure
- name: Cip Service Return Delineation Geometry Structure
  property_count: 0
  slug: cip-service-return-delineation-geometry-structure
- name: Cip Service Return Flowline Details Structure
  property_count: 0
  slug: cip-service-return-flowline-details-structure
- name: Cip Service Return Flowline Geometry Structure
  property_count: 0
  slug: cip-service-return-flowline-geometry-structure
- name: Cip Service Search Type Structure
  property_count: 0
  slug: cip-service-search-type-structure
- name: Cip Service Split Initial Catchment Structure
  property_count: 0
  slug: cip-service-split-initial-catchment-structure
- name: Cip Service Start Hydroseq Structure
  property_count: 0
  slug: cip-service-start-hydroseq-structure
- name: Cip Service Start Measure Structure
  property_count: 0
  slug: cip-service-start-measure-structure
- name: Cip Service Start Nhdplusid Structure
  property_count: 0
  slug: cip-service-start-nhdplusid-structure
- name: Cip Service Start Permanent Identifier Structure
  property_count: 0
  slug: cip-service-start-permanent-identifier-structure
- name: Cip Service Start Reachcode Structure
  property_count: 0
  slug: cip-service-start-reachcode-structure
- name: Cip Service Status Message Structure
  property_count: 0
  slug: cip-service-status-message-structure
- name: Cip Service Stop Hydroseq Structure
  property_count: 0
  slug: cip-service-stop-hydroseq-structure
- name: Cip Service Stop Measure Structure
  property_count: 0
  slug: cip-service-stop-measure-structure
- name: Cip Service Stop Nhdplusid Structure
  property_count: 0
  slug: cip-service-stop-nhdplusid-structure
- name: Cip Service Stop Permanent Identifier Structure
  property_count: 0
  slug: cip-service-stop-permanent-identifier-structure
- name: Cip Service Stop Reachcode Structure
  property_count: 0
  slug: cip-service-stop-reachcode-structure
- name: Cip Service Upstreamdownstream Rb Structure
  property_count: 49
  slug: cip-service-upstreamdownstream-rb-structure
- name: Cip Service Upstreamdownstream Resp Structure
  property_count: 27
  slug: cip-service-upstreamdownstream-resp-structure
- name: Cip Service Wbd Version Structure
  property_count: 0
  slug: cip-service-wbd-version-structure
- name: Csb Rebate Formio Schema And Submission Structure
  property_count: 3
  slug: csb-rebate-formio-schema-and-submission-structure
- name: Echo Air Air00 Structure
  property_count: 17
  slug: echo-air-air00-structure
- name: Echo Air Air01 Structure
  property_count: 1
  slug: echo-air-air01-structure
- name: Echo Air Air02 Structure
  property_count: 10
  slug: echo-air-air02-structure
- name: Echo Air Air03 Structure
  property_count: 143
  slug: echo-air-air03-structure
- name: Echo Air Air04 Structure
  property_count: 4
  slug: echo-air-air04-structure
- name: Echo Air Air05 Structure
  property_count: 15
  slug: echo-air-air05-structure
- name: Echo Air Air06 Structure
  property_count: 144
  slug: echo-air-air06-structure
- name: Echo Air Air08 Structure
  property_count: 19
  slug: echo-air-air08-structure
- name: Echo Air Air09 Structure
  property_count: 3
  slug: echo-air-air09-structure
- name: Echo Air Air10 Structure
  property_count: 141
  slug: echo-air-air10-structure
- name: Echo Air Air11 Structure
  property_count: 4
  slug: echo-air-air11-structure
- name: Echo Air Air12 Structure
  property_count: 5
  slug: echo-air-air12-structure
- name: Echo Air Geo Structure
  property_count: 2
  slug: echo-air-geo-structure
- name: Echo Air Meta1 Structure
  property_count: 2
  slug: echo-air-meta1-structure
- name: Echo Air Meta3 Structure
  property_count: 6
  slug: echo-air-meta3-structure
- name: Echo Air Qp0 Structure
  property_count: 2
  slug: echo-air-qp0-structure
- name: Echo All Echo01 Structure
  property_count: 13
  slug: echo-all-echo01-structure
- name: Echo All Echo02 Structure
  property_count: 4
  slug: echo-all-echo02-structure
- name: Echo All Echo03 Structure
  property_count: 193
  slug: echo-all-echo03-structure
- name: Echo All Echo04 Structure
  property_count: 20
  slug: echo-all-echo04-structure
- name: Echo All Echo05 Structure
  property_count: 17
  slug: echo-all-echo05-structure
- name: Echo All Echo06 Structure
  property_count: 1
  slug: echo-all-echo06-structure
- name: Echo All Echo07 Structure
  property_count: 194
  slug: echo-all-echo07-structure
- name: Echo All Echo08 Structure
  property_count: 23
  slug: echo-all-echo08-structure
- name: Echo All Echo09 Structure
  property_count: 3
  slug: echo-all-echo09-structure
- name: Echo All Echo10 Structure
  property_count: 191
  slug: echo-all-echo10-structure
- name: Echo All Echo11 Structure
  property_count: 5
  slug: echo-all-echo11-structure
- name: Echo All Geo Structure
  property_count: 2
  slug: echo-all-geo-structure
- name: Echo All Meta1 Structure
  property_count: 2
  slug: echo-all-meta1-structure
- name: Echo All Meta3 Structure
  property_count: 6
  slug: echo-all-meta3-structure
- name: Echo All Qp0 Structure
  property_count: 2
  slug: echo-all-qp0-structure
- name: Echo Case Crs0 Cases Structure
  property_count: 40
  slug: echo-case-crs0-cases-structure
- name: Echo Case Crs0 Cluster Data Structure
  property_count: 22
  slug: echo-case-crs0-cluster-data-structure
- name: Echo Case Crs0 Cluster Output Structure
  property_count: 1
  slug: echo-case-crs0-cluster-output-structure
- name: Echo Case Crs0 Get Case Info.Results Structure
  property_count: 20
  slug: echo-case-crs0-get-case-info.results-structure
- name: Echo Case Crs0 Get Cases From Facility.Case Number Structure
  property_count: 1
  slug: echo-case-crs0-get-cases-from-facility.case-number-structure
- name: Echo Case Crs0 Get Cases From Facility.Case Numbers Structure
  property_count: 1
  slug: echo-case-crs0-get-cases-from-facility.case-numbers-structure
- name: Echo Case Crs0 Get Cases From Facility.Results Structure
  property_count: 1
  slug: echo-case-crs0-get-cases-from-facility.results-structure
- name: Echo Case Crs0 Get Facilities From Case.Registry Id Structure
  property_count: 1
  slug: echo-case-crs0-get-facilities-from-case.registry-id-structure
- name: Echo Case Crs0 Get Facilities From Case.Registry Ids Structure
  property_count: 1
  slug: echo-case-crs0-get-facilities-from-case.registry-ids-structure
- name: Echo Case Crs0 Get Facilities From Case.Results Structure
  property_count: 1
  slug: echo-case-crs0-get-facilities-from-case.results-structure
- name: Echo Case Crs0 Map Data Structure
  property_count: 7
  slug: echo-case-crs0-map-data-structure
- name: Echo Case Crs0 Map Output Structure
  property_count: 4
  slug: echo-case-crs0-map-output-structure
- name: Echo Case Crs1 Caeddocuments Structure
  property_count: 5
  slug: echo-case-crs1-caeddocuments-structure
- name: Echo Case Crs1 Case Information Structure
  property_count: 22
  slug: echo-case-crs1-case-information-structure
- name: Echo Case Crs1 Case Milestones Structure
  property_count: 2
  slug: echo-case-crs1-case-milestones-structure
- name: Echo Case Crs1 Citations Structure
  property_count: 3
  slug: echo-case-crs1-citations-structure
- name: Echo Case Crs1 Compliance Schedules Structure
  property_count: 7
  slug: echo-case-crs1-compliance-schedules-structure
- name: Echo Case Crs1 Complying Actions Structure
  property_count: 4
  slug: echo-case-crs1-complying-actions-structure
- name: Echo Case Crs1 Defendants Structure
  property_count: 3
  slug: echo-case-crs1-defendants-structure
- name: Echo Case Crs1 Enforcement Conclusions Structure
  property_count: 18
  slug: echo-case-crs1-enforcement-conclusions-structure
- name: Echo Case Crs1 Facilities Structure
  property_count: 8
  slug: echo-case-crs1-facilities-structure
- name: Echo Case Crs1 Final Order Statuses Structure
  property_count: 5
  slug: echo-case-crs1-final-order-statuses-structure
- name: Echo Case Crs1 Laws And Sections Structure
  property_count: 3
  slug: echo-case-crs1-laws-and-sections-structure
- name: Echo Case Crs1 Pollutant Reductions Structure
  property_count: 8
  slug: echo-case-crs1-pollutant-reductions-structure
- name: Echo Case Crs1 Pollutants Structure
  property_count: 2
  slug: echo-case-crs1-pollutants-structure
- name: Echo Case Crs1 Program Links Structure
  property_count: 3
  slug: echo-case-crs1-program-links-structure
- name: Echo Case Crs1 Related Activities Structure
  property_count: 2
  slug: echo-case-crs1-related-activities-structure
- name: Echo Case Crs1 Results Structure
  property_count: 12
  slug: echo-case-crs1-results-structure
- name: Echo Case Crs1 Supplemental Environmental Projects Structure
  property_count: 5
  slug: echo-case-crs1-supplemental-environmental-projects-structure
- name: Echo Case Crs2 Results Structure
  property_count: 20
  slug: echo-case-crs2-results-structure
- name: Echo Case Crs3 Case Information Structure
  property_count: 5
  slug: echo-case-crs3-case-information-structure
- name: Echo Case Crs3 Crdefendants Structure
  property_count: 5
  slug: echo-case-crs3-crdefendants-structure
- name: Echo Case Crs3 Crdetails Structure
  property_count: 3
  slug: echo-case-crs3-crdetails-structure
- name: Echo Case Crs3 Locations Structure
  property_count: 7
  slug: echo-case-crs3-locations-structure
- name: Echo Case Crs3 Results Structure
  property_count: 5
  slug: echo-case-crs3-results-structure
- name: Echo Case Crs5 Results Structure
  property_count: 5
  slug: echo-case-crs5-results-structure
- name: Echo Case Met1 Structure
  property_count: 2
  slug: echo-case-met1-structure
- name: Echo Case Met2 Structure
  property_count: 6
  slug: echo-case-met2-structure
- name: Echo Case Qp0 Structure
  property_count: 2
  slug: echo-case-qp0-structure
- name: Echo Case Rlk00 Lu Values Structure
  property_count: 2
  slug: echo-case-rlk00-lu-values-structure
- name: Echo Case Rlk51 Results Structure
  property_count: 2
  slug: echo-case-rlk51-results-structure
- name: Echo Cwa Cwa01 Structure
  property_count: 305
  slug: echo-cwa-cwa01-structure
- name: Echo Cwa Cwa02 Structure
  property_count: 10
  slug: echo-cwa-cwa02-structure
- name: Echo Cwa Cwa03 Structure
  property_count: 4
  slug: echo-cwa-cwa03-structure
- name: Echo Cwa Cwa04 Structure
  property_count: 19
  slug: echo-cwa-cwa04-structure
- name: Echo Cwa Cwa05 Structure
  property_count: 20
  slug: echo-cwa-cwa05-structure
- name: Echo Cwa Cwa06 Structure
  property_count: 1
  slug: echo-cwa-cwa06-structure
- name: Echo Cwa Cwa07 Structure
  property_count: 306
  slug: echo-cwa-cwa07-structure
- name: Echo Cwa Cwa08 Structure
  property_count: 22
  slug: echo-cwa-cwa08-structure
- name: Echo Cwa Cwa09 Structure
  property_count: 3
  slug: echo-cwa-cwa09-structure
- name: Echo Cwa Cwa10 Structure
  property_count: 303
  slug: echo-cwa-cwa10-structure
- name: Echo Cwa Cwa11 Structure
  property_count: 10
  slug: echo-cwa-cwa11-structure
- name: Echo Cwa Cwa12 Structure
  property_count: 4
  slug: echo-cwa-cwa12-structure
- name: Echo Cwa Cwa13 Structure
  property_count: 5
  slug: echo-cwa-cwa13-structure
- name: Echo Cwa Geo Structure
  property_count: 2
  slug: echo-cwa-geo-structure
- name: Echo Cwa Meta1 Structure
  property_count: 2
  slug: echo-cwa-meta1-structure
- name: Echo Cwa Meta3 Structure
  property_count: 6
  slug: echo-cwa-meta3-structure
- name: Echo Cwa Qp0 Structure
  property_count: 2
  slug: echo-cwa-qp0-structure
- name: Echo Cwa Rlup01 Structure
  property_count: 2
  slug: echo-cwa-rlup01-structure
- name: Echo Cwa Rlup20 Structure
  property_count: 2
  slug: echo-cwa-rlup20-structure
- name: Echo Cwa Rlup23 Structure
  property_count: 2
  slug: echo-cwa-rlup23-structure
- name: Echo Cwa Rlup24 Structure
  property_count: 2
  slug: echo-cwa-rlup24-structure
- name: Echo Cwa Rlup54 Structure
  property_count: 2
  slug: echo-cwa-rlup54-structure
- name: Echo Cwa Rlup58 Structure
  property_count: 2
  slug: echo-cwa-rlup58-structure
- name: Echo Cwa Rlup59 Structure
  property_count: 2
  slug: echo-cwa-rlup59-structure
- name: Echo Cwa Rlup61 Structure
  property_count: 2
  slug: echo-cwa-rlup61-structure
- name: Echo Cwa Rlup65 Structure
  property_count: 2
  slug: echo-cwa-rlup65-structure
- name: Echo Cwa Rlup75 Structure
  property_count: 2
  slug: echo-cwa-rlup75-structure
- name: Echo Cwa Rlup77 Structure
  property_count: 2
  slug: echo-cwa-rlup77-structure
- name: Echo Dfr Dfr0 Get Aws Docs.Results Structure
  property_count: 1
  slug: echo-dfr-dfr0-get-aws-docs.results-structure
- name: Echo Dfr Dfr0 Get Cwa Eff Alr Exp.Results Structure
  property_count: 2
  slug: echo-dfr-dfr0-get-cwa-eff-alr-exp.results-structure
- name: Echo Dfr Dfr0 Get Cwa Eff Compliance Exp.Results Structure
  property_count: 2
  slug: echo-dfr-dfr0-get-cwa-eff-compliance-exp.results-structure
- name: Echo Dfr Dfr0 Get D80D90S Details.D80 D90S Details Structure
  property_count: 1
  slug: echo-dfr-dfr0-get-d80d90s-details.d80-d90s-details-structure
- name: Echo Dfr Dfr0 Get D80D90S Details.D80 D90S Details.Sources Structure
  property_count: 29
  slug: echo-dfr-dfr0-get-d80d90s-details.d80-d90s-details.sources-structure
- name: Echo Dfr Dfr0 Get D80D90S Details.Results Structure
  property_count: 2
  slug: echo-dfr-dfr0-get-d80d90s-details.results-structure
- name: Echo Dfr Dfr0 Get Ejscreen Indexes.Results Structure
  property_count: 2
  slug: echo-dfr-dfr0-get-ejscreen-indexes.results-structure
- name: Echo Dfr Dfr0 Qtr12 Header Structure
  property_count: 96
  slug: echo-dfr-dfr0-qtr12-header-structure
- name: Echo Dfr Dfr0 Qtr12 Header39 Structure
  property_count: 102
  slug: echo-dfr-dfr0-qtr12-header39-structure
- name: Echo Dfr Dfr0 Qtr12 Status Structure
  property_count: 13
  slug: echo-dfr-dfr0-qtr12-status-structure
- name: Echo Dfr Dfr0 Qtr13 Header Structure
  property_count: 104
  slug: echo-dfr-dfr0-qtr13-header-structure
- name: Echo Dfr Dfr0 Qtr13 Status Structure
  property_count: 14
  slug: echo-dfr-dfr0-qtr13-status-structure
- name: Echo Dfr Dfr001 Results Structure
  property_count: 2
  slug: echo-dfr-dfr001-results-structure
- name: Echo Dfr Dfr002 Results Structure
  property_count: 2
  slug: echo-dfr-dfr002-results-structure
- name: Echo Dfr Dfr004 Structure
  property_count: 2
  slug: echo-dfr-dfr004-structure
- name: Echo Dfr Dfr005 Results Structure
  property_count: 2
  slug: echo-dfr-dfr005-results-structure
- name: Echo Dfr Dfr006 Results Structure
  property_count: 2
  slug: echo-dfr-dfr006-results-structure
- name: Echo Dfr Dfr007 Results Structure
  property_count: 2
  slug: echo-dfr-dfr007-results-structure
- name: Echo Dfr Dfr009 Results Structure
  property_count: 2
  slug: echo-dfr-dfr009-results-structure
- name: Echo Dfr Dfr010 Results Structure
  property_count: 2
  slug: echo-dfr-dfr010-results-structure
- name: Echo Dfr Dfr011 Results Structure
  property_count: 2
  slug: echo-dfr-dfr011-results-structure
- name: Echo Dfr Dfr012 Results Structure
  property_count: 2
  slug: echo-dfr-dfr012-results-structure
- name: Echo Dfr Dfr013 Results Structure
  property_count: 2
  slug: echo-dfr-dfr013-results-structure
- name: Echo Dfr Dfr014 Results Structure
  property_count: 2
  slug: echo-dfr-dfr014-results-structure
- name: Echo Dfr Dfr015 Results Structure
  property_count: 2
  slug: echo-dfr-dfr015-results-structure
- name: Echo Dfr Dfr017 Results Structure
  property_count: 2
  slug: echo-dfr-dfr017-results-structure
- name: Echo Dfr Dfr018 Caeddocuments Structure
  property_count: 5
  slug: echo-dfr-dfr018-caeddocuments-structure
- name: Echo Dfr Dfr018 Ejscreen Indexes Structure
  property_count: 13
  slug: echo-dfr-dfr018-ejscreen-indexes-structure
- name: Echo Dfr Dfr018 Map Data Structure
  property_count: 6
  slug: echo-dfr-dfr018-map-data-structure
- name: Echo Dfr Dfr018 Multiple Frsfacilities Structure
  property_count: 1
  slug: echo-dfr-dfr018-multiple-frsfacilities-structure
- name: Echo Dfr Dfr018 Naics Structure
  property_count: 1
  slug: echo-dfr-dfr018-naics-structure
- name: Echo Dfr Dfr018 Permits Structure
  property_count: 27
  slug: echo-dfr-dfr018-permits-structure
- name: Echo Dfr Dfr018 Program Dates Structure
  property_count: 3
  slug: echo-dfr-dfr018-program-dates-structure
- name: Echo Dfr Dfr018 Registry Ids Structure
  property_count: 8
  slug: echo-dfr-dfr018-registry-ids-structure
- name: Echo Dfr Dfr018 Reports Structure
  property_count: 1
  slug: echo-dfr-dfr018-reports-structure
- name: Echo Dfr Dfr018 Results Structure
  property_count: 44
  slug: echo-dfr-dfr018-results-structure
- name: Echo Dfr Dfr018 Summaries Structure
  property_count: 11
  slug: echo-dfr-dfr018-summaries-structure
- name: Echo Dfr Dfr018 Web Fire Documents Structure
  property_count: 7
  slug: echo-dfr-dfr018-web-fire-documents-structure
- name: Echo Dfr Dfr019 Structure
  property_count: 2
  slug: echo-dfr-dfr019-structure
- name: Echo Dfr Dfr020 .Hpvhistory Structure
  property_count: 49
  slug: echo-dfr-dfr020-.hpvhistory-structure
- name: Echo Dfr Dfr020 .Permit History Structure
  property_count: 49
  slug: echo-dfr-dfr020-.permit-history-structure
- name: Echo Dfr Dfr020 Structure
  property_count: 5
  slug: echo-dfr-dfr020-structure
- name: Echo Dfr Dfr021 Structure
  property_count: 14
  slug: echo-dfr-dfr021-structure
- name: Echo Dfr Dfr022 Structure
  property_count: 53
  slug: echo-dfr-dfr022-structure
- name: Echo Dfr Dfr023 Structure
  property_count: 53
  slug: echo-dfr-dfr023-structure
- name: Echo Dfr Dfr024 Structure
  property_count: 13
  slug: echo-dfr-dfr024-structure
- name: Echo Dfr Dfr025 Structure
  property_count: 2
  slug: echo-dfr-dfr025-structure
- name: Echo Dfr Dfr026 Structure
  property_count: 1
  slug: echo-dfr-dfr026-structure
- name: Echo Dfr Dfr027 Structure
  property_count: 2
  slug: echo-dfr-dfr027-structure
- name: Echo Dfr Dfr029 Structure
  property_count: 1
  slug: echo-dfr-dfr029-structure
- name: Echo Dfr Dfr030 Structure
  property_count: 54
  slug: echo-dfr-dfr030-structure
- name: Echo Dfr Dfr031 Structure
  property_count: 2
  slug: echo-dfr-dfr031-structure
- name: Echo Dfr Dfr032 Structure
  property_count: 1
  slug: echo-dfr-dfr032-structure
- name: Echo Dfr Dfr034 Structure
  property_count: 107
  slug: echo-dfr-dfr034-structure
- name: Echo Dfr Dfr035 Exp Structure
  property_count: 2
  slug: echo-dfr-dfr035-exp-structure
- name: Echo Dfr Dfr035 Exp.Parameters Structure
  property_count: 58
  slug: echo-dfr-dfr035-exp.parameters-structure
- name: Echo Dfr Dfr035 Exp.Sources Structure
  property_count: 1
  slug: echo-dfr-dfr035-exp.sources-structure
- name: Echo Dfr Dfr035 Structure
  property_count: 2
  slug: echo-dfr-dfr035-structure
- name: Echo Dfr Dfr036 Structure
  property_count: 57
  slug: echo-dfr-dfr036-structure
- name: Echo Dfr Dfr037 Structure
  property_count: 1
  slug: echo-dfr-dfr037-structure
- name: Echo Dfr Dfr038 Exp Structure
  property_count: 2
  slug: echo-dfr-dfr038-exp-structure
- name: Echo Dfr Dfr038 Exp.Parameters Structure
  property_count: 110
  slug: echo-dfr-dfr038-exp.parameters-structure
- name: Echo Dfr Dfr038 Exp.Sources Structure
  property_count: 1
  slug: echo-dfr-dfr038-exp.sources-structure
- name: Echo Dfr Dfr038 Structure
  property_count: 2
  slug: echo-dfr-dfr038-structure
- name: Echo Dfr Dfr040 Structure
  property_count: 109
  slug: echo-dfr-dfr040-structure
- name: Echo Dfr Dfr041 Structure
  property_count: 1
  slug: echo-dfr-dfr041-structure
- name: Echo Dfr Dfr042 Structure
  property_count: 2
  slug: echo-dfr-dfr042-structure
- name: Echo Dfr Dfr043 Structure
  property_count: 1
  slug: echo-dfr-dfr043-structure
- name: Echo Dfr Dfr045 Structure
  property_count: 107
  slug: echo-dfr-dfr045-structure
- name: Echo Dfr Dfr046 Structure
  property_count: 2
  slug: echo-dfr-dfr046-structure
- name: Echo Dfr Dfr047 .Status Structure
  property_count: 1
  slug: echo-dfr-dfr047-.status-structure
- name: Echo Dfr Dfr049 Structure
  property_count: 2
  slug: echo-dfr-dfr049-structure
- name: Echo Dfr Dfr050 Structure
  property_count: 1
  slug: echo-dfr-dfr050-structure
- name: Echo Dfr Dfr051 Structure
  property_count: 108
  slug: echo-dfr-dfr051-structure
- name: Echo Dfr Dfr052 Structure
  property_count: 2
  slug: echo-dfr-dfr052-structure
- name: Echo Dfr Dfr053 Structure
  property_count: 13
  slug: echo-dfr-dfr053-structure
- name: Echo Dfr Dfr054 Structure
  property_count: 6
  slug: echo-dfr-dfr054-structure
- name: Echo Dfr Dfr055 Structure
  property_count: 1
  slug: echo-dfr-dfr055-structure
- name: Echo Dfr Dfr057 Structure
  property_count: 2
  slug: echo-dfr-dfr057-structure
- name: Echo Dfr Dfr058 Structure
  property_count: 10
  slug: echo-dfr-dfr058-structure
- name: Echo Dfr Dfr059 Structure
  property_count: 2
  slug: echo-dfr-dfr059-structure
- name: Echo Dfr Dfr060 Structure
  property_count: 6
  slug: echo-dfr-dfr060-structure
- name: Echo Dfr Dfr061 Structure
  property_count: 32
  slug: echo-dfr-dfr061-structure
- name: Echo Dfr Dfr062 Structure
  property_count: 2
  slug: echo-dfr-dfr062-structure
- name: Echo Dfr Dfr063 S Structure
  property_count: 4
  slug: echo-dfr-dfr063-s-structure
- name: Echo Dfr Dfr064 Structure
  property_count: 2
  slug: echo-dfr-dfr064-structure
- name: Echo Dfr Dfr065 Structure
  property_count: 7
  slug: echo-dfr-dfr065-structure
- name: Echo Dfr Dfr066 Structure
  property_count: 2
  slug: echo-dfr-dfr066-structure
- name: Echo Dfr Dfr067 Structure
  property_count: 16
  slug: echo-dfr-dfr067-structure
- name: Echo Dfr Dfr068 Structure
  property_count: 2
  slug: echo-dfr-dfr068-structure
- name: Echo Dfr Dfr069 Structure
  property_count: 7
  slug: echo-dfr-dfr069-structure
- name: Echo Dfr Dfr070 Structure
  property_count: 18
  slug: echo-dfr-dfr070-structure
- name: Echo Dfr Dfr071 Structure
  property_count: 4
  slug: echo-dfr-dfr071-structure
- name: Echo Dfr Dfr072 Structure
  property_count: 4
  slug: echo-dfr-dfr072-structure
- name: Echo Dfr Dfr073 Structure
  property_count: 5
  slug: echo-dfr-dfr073-structure
- name: Echo Dfr Dfr074 Structure
  property_count: 1
  slug: echo-dfr-dfr074-structure
- name: Echo Dfr Dfr075 Structure
  property_count: 4
  slug: echo-dfr-dfr075-structure
- name: Echo Dfr Dfr076 Structure
  property_count: 2
  slug: echo-dfr-dfr076-structure
- name: Echo Dfr Dfr077 Structure
  property_count: 7
  slug: echo-dfr-dfr077-structure
- name: Echo Dfr Dfr078 Structure
  property_count: 97
  slug: echo-dfr-dfr078-structure
- name: Echo Dfr Dfr079 S Structure
  property_count: 3
  slug: echo-dfr-dfr079-s-structure
- name: Echo Dfr Dfr079 S.Evaluations Structure
  property_count: 52
  slug: echo-dfr-dfr079-s.evaluations-structure
- name: Echo Dfr Dfr079 S.Status Structure
  property_count: 49
  slug: echo-dfr-dfr079-s.status-structure
- name: Echo Dfr Dfr079 S.Violations Structure
  property_count: 52
  slug: echo-dfr-dfr079-s.violations-structure
- name: Echo Dfr Dfr081 Structure
  property_count: 105
  slug: echo-dfr-dfr081-structure
- name: Echo Dfr Dfr083 S Structure
  property_count: 2
  slug: echo-dfr-dfr083-s-structure
- name: Echo Dfr Dfr083 S.Rules Violated Structure
  property_count: 15
  slug: echo-dfr-dfr083-s.rules-violated-structure
- name: Echo Dfr Dfr084 Codes Structure
  property_count: 4
  slug: echo-dfr-dfr084-codes-structure
- name: Echo Dfr Dfr084 Structure
  property_count: 1
  slug: echo-dfr-dfr084-structure
- name: Echo Dfr Dfr085 Structure
  property_count: 1
  slug: echo-dfr-dfr085-structure
- name: Echo Dfr Dfr086 Structure
  property_count: 1
  slug: echo-dfr-dfr086-structure
- name: Echo Dfr Dfr088 Structure
  property_count: 1
  slug: echo-dfr-dfr088-structure
- name: Echo Dfr Dfr089 Structure
  property_count: 15
  slug: echo-dfr-dfr089-structure
- name: Echo Dfr Dfr090 Structure
  property_count: 1
  slug: echo-dfr-dfr090-structure
- name: Echo Dfr Dfr092 Structure
  property_count: 1
  slug: echo-dfr-dfr092-structure
- name: Echo Dfr Dfr093 Structure
  property_count: 15
  slug: echo-dfr-dfr093-structure
- name: Echo Dfr Dfr094 Structure
  property_count: 8
  slug: echo-dfr-dfr094-structure
- name: Echo Dfr Dfr095 Structure
  property_count: 1
  slug: echo-dfr-dfr095-structure
- name: Echo Dfr Dfr096 Structure
  property_count: 2
  slug: echo-dfr-dfr096-structure
- name: Echo Dfr Dfr098 Structure
  property_count: 1
  slug: echo-dfr-dfr098-structure
- name: Echo Dfr Dfr100 Structure
  property_count: 1
  slug: echo-dfr-dfr100-structure
- name: Echo Dfr Dfr101 Structure
  property_count: 10
  slug: echo-dfr-dfr101-structure
- name: Echo Dfr Dfr102 Structure
  property_count: 2
  slug: echo-dfr-dfr102-structure
- name: Echo Dfr Dfr103 Structure
  property_count: 10
  slug: echo-dfr-dfr103-structure
- name: Echo Dfr Dfr104 Structure
  property_count: 9
  slug: echo-dfr-dfr104-structure
- name: Echo Dfr Dfr105 Structure
  property_count: 4
  slug: echo-dfr-dfr105-structure
- name: Echo Dfr Dfr106 Structure
  property_count: 1
  slug: echo-dfr-dfr106-structure
- name: Echo Dfr Dfr108 Structure
  property_count: 1
  slug: echo-dfr-dfr108-structure
- name: Echo Dfr Dfr109 Structure
  property_count: 5
  slug: echo-dfr-dfr109-structure
- name: Echo Dfr Dfr110 Structure
  property_count: 14
  slug: echo-dfr-dfr110-structure
- name: Echo Dfr Dfr111 Details Structure
  property_count: 1
  slug: echo-dfr-dfr111-details-structure
- name: Echo Dfr Dfr111 Details.Sources Structure
  property_count: 16
  slug: echo-dfr-dfr111-details.sources-structure
- name: Echo Dfr Dfr111 Structure
  property_count: 1
  slug: echo-dfr-dfr111-structure
- name: Echo Dfr Dfr112 Structure
  property_count: 21
  slug: echo-dfr-dfr112-structure
- name: Echo Dfr Dfr114 Results Structure
  property_count: 2
  slug: echo-dfr-dfr114-results-structure
- name: Echo Dfr Dfr115 Structure
  property_count: 2
  slug: echo-dfr-dfr115-structure
- name: Echo Dfr Dfr116 Results Structure
  property_count: 2
  slug: echo-dfr-dfr116-results-structure
- name: Echo Dfr Dfr117 Results Structure
  property_count: 2
  slug: echo-dfr-dfr117-results-structure
- name: Echo Dfr Dfr118 Results Structure
  property_count: 2
  slug: echo-dfr-dfr118-results-structure
- name: Echo Dfr Dfr119 Results Structure
  property_count: 2
  slug: echo-dfr-dfr119-results-structure
- name: Echo Dfr Dfr120 Results Structure
  property_count: 2
  slug: echo-dfr-dfr120-results-structure
- name: Echo Dfr Dfr122 Results Structure
  property_count: 2
  slug: echo-dfr-dfr122-results-structure
- name: Echo Dfr Dfr123 Results Structure
  property_count: 3
  slug: echo-dfr-dfr123-results-structure
- name: Echo Dfr Dfr124 Results Structure
  property_count: 2
  slug: echo-dfr-dfr124-results-structure
- name: Echo Dfr Dfr125 Results Structure
  property_count: 2
  slug: echo-dfr-dfr125-results-structure
- name: Echo Dfr Dfr126 Results Structure
  property_count: 2
  slug: echo-dfr-dfr126-results-structure
- name: Echo Dfr Dfr127 Results Structure
  property_count: 2
  slug: echo-dfr-dfr127-results-structure
- name: Echo Dfr Dfr128 Results Structure
  property_count: 2
  slug: echo-dfr-dfr128-results-structure
- name: Echo Dfr Dfr129 Results Structure
  property_count: 2
  slug: echo-dfr-dfr129-results-structure
- name: Echo Dfr Dfr130 Results Structure
  property_count: 2
  slug: echo-dfr-dfr130-results-structure
- name: Echo Dfr Dfr131 Results Structure
  property_count: 2
  slug: echo-dfr-dfr131-results-structure
- name: Echo Dfr Dfr132 Results Structure
  property_count: 2
  slug: echo-dfr-dfr132-results-structure
- name: Echo Dfr Dfr133 Results Structure
  property_count: 2
  slug: echo-dfr-dfr133-results-structure
- name: Echo Dfr Dfr134 Results Structure
  property_count: 2
  slug: echo-dfr-dfr134-results-structure
- name: Echo Dfr Dfr135 Results Structure
  property_count: 2
  slug: echo-dfr-dfr135-results-structure
- name: Echo Dfr Dfr136 Results Structure
  property_count: 2
  slug: echo-dfr-dfr136-results-structure
- name: Echo Effluent Eff01 Structure
  property_count: 41
  slug: echo-effluent-eff01-structure
- name: Echo Effluent Eff02 Structure
  property_count: 11
  slug: echo-effluent-eff02-structure
- name: Echo Effluent Eff03 Structure
  property_count: 7
  slug: echo-effluent-eff03-structure
- name: Echo Effluent Eff04 Structure
  property_count: 4
  slug: echo-effluent-eff04-structure
- name: Echo Effluent Eff05 Structure
  property_count: 17
  slug: echo-effluent-eff05-structure
- name: Echo Effluent Eff06 Structure
  property_count: 10
  slug: echo-effluent-eff06-structure
- name: Echo Effluent Eff07 Structure
  property_count: 4
  slug: echo-effluent-eff07-structure
- name: Echo Effluent Eff08 Structure
  property_count: 4
  slug: echo-effluent-eff08-structure
- name: Echo Effluent Eff09 Structure
  property_count: 18
  slug: echo-effluent-eff09-structure
- name: Echo Effluent Rlup01 Structure
  property_count: 2
  slug: echo-effluent-rlup01-structure
- name: Echo Effluent Rlup23 Structure
  property_count: 2
  slug: echo-effluent-rlup23-structure
- name: Echo Rcra Geo Structure
  property_count: 2
  slug: echo-rcra-geo-structure
- name: Echo Rcra Meta1 Structure
  property_count: 2
  slug: echo-rcra-meta1-structure
- name: Echo Rcra Meta3 Structure
  property_count: 6
  slug: echo-rcra-meta3-structure
- name: Echo Rcra Qp0 Structure
  property_count: 2
  slug: echo-rcra-qp0-structure
- name: Echo Rcra Rcra01 Structure
  property_count: 119
  slug: echo-rcra-rcra01-structure
- name: Echo Rcra Rcra02 Structure
  property_count: 10
  slug: echo-rcra-rcra02-structure
- name: Echo Rcra Rcra03 Structure
  property_count: 4
  slug: echo-rcra-rcra03-structure
- name: Echo Rcra Rcra04 Structure
  property_count: 15
  slug: echo-rcra-rcra04-structure
- name: Echo Rcra Rcra05 Structure
  property_count: 17
  slug: echo-rcra-rcra05-structure
- name: Echo Rcra Rcra06 Structure
  property_count: 1
  slug: echo-rcra-rcra06-structure
- name: Echo Rcra Rcra07 Structure
  property_count: 120
  slug: echo-rcra-rcra07-structure
- name: Echo Rcra Rcra08 Structure
  property_count: 19
  slug: echo-rcra-rcra08-structure
- name: Echo Rcra Rcra09 Structure
  property_count: 3
  slug: echo-rcra-rcra09-structure
- name: Echo Rcra Rcra10 Structure
  property_count: 117
  slug: echo-rcra-rcra10-structure
- name: Echo Rcra Rcra11 Structure
  property_count: 10
  slug: echo-rcra-rcra11-structure
- name: Echo Rcra Rcra12 Structure
  property_count: 4
  slug: echo-rcra-rcra12-structure
- name: Echo Rcra Rcra13 Structure
  property_count: 5
  slug: echo-rcra-rcra13-structure
- name: Echo Sdw Meta1 Structure
  property_count: 2
  slug: echo-sdw-meta1-structure
- name: Echo Sdw Meta3 Structure
  property_count: 6
  slug: echo-sdw-meta3-structure
- name: Echo Sdw Sdw02 Structure
  property_count: 5
  slug: echo-sdw-sdw02-structure
- name: Echo Sdw Sdw03 Structure
  property_count: 14
  slug: echo-sdw-sdw03-structure
- name: Echo Sdw Sdw04 Structure
  property_count: 77
  slug: echo-sdw-sdw04-structure
- name: Elg Search Custom Search.Keyword Search Structure
  property_count: 1
  slug: elg-search-custom-search.keyword-search-structure
- name: Elg Search Custom Search.Multi Criteria Search Criteria Structure
  property_count: 1
  slug: elg-search-custom-search.multi-criteria-search-criteria-structure
- name: Elg Search Custom Search.Multi Criteria Search Structure
  property_count: 1
  slug: elg-search-custom-search.multi-criteria-search-structure
- name: Elg Search Glossary.Contact Structure
  property_count: 1
  slug: elg-search-glossary.contact-structure
- name: Elg Search Glossary.Help Structure
  property_count: 1
  slug: elg-search-glossary.help-structure
- name: Elg Search Glossary.List Structure
  property_count: 1
  slug: elg-search-glossary.list-structure
- name: Elg Search Limitation.Read Structure
  property_count: 1
  slug: elg-search-limitation.read-structure
- name: Elg Search Point Source Category.Cfr Structure
  property_count: 1
  slug: elg-search-point-source-category.cfr-structure
- name: Elg Search Point Source Category.Citation History Structure
  property_count: 1
  slug: elg-search-point-source-category.citation-history-structure
- name: Elg Search Point Source Category.Definitions Structure
  property_count: 1
  slug: elg-search-point-source-category.definitions-structure
- name: Elg Search Point Source Category.List Structure
  property_count: 1
  slug: elg-search-point-source-category.list-structure
- name: Elg Search Point Source Category.Read Structure
  property_count: 1
  slug: elg-search-point-source-category.read-structure
- name: Elg Search Point Source Subcategory.Read Structure
  property_count: 1
  slug: elg-search-point-source-subcategory.read-structure
- name: Elg Search Pollutant.Limitations Structure
  property_count: 1
  slug: elg-search-pollutant.limitations-structure
- name: Elg Search Pollutant.List Categories Structure
  property_count: 1
  slug: elg-search-pollutant.list-categories-structure
- name: Elg Search Pollutant.List Structure
  property_count: 1
  slug: elg-search-pollutant.list-structure
- name: Elg Search Pollutant.Read Category Structure
  property_count: 1
  slug: elg-search-pollutant.read-category-structure
- name: Elg Search Pollutant.Read Structure
  property_count: 1
  slug: elg-search-pollutant.read-structure
- name: Elg Search Treatment Technology.Category Limitations Structure
  property_count: 1
  slug: elg-search-treatment-technology.category-limitations-structure
- name: Elg Search Treatment Technology.Limitations Structure
  property_count: 1
  slug: elg-search-treatment-technology.limitations-structure
- name: Elg Search Treatment Technology.List Categories Structure
  property_count: 1
  slug: elg-search-treatment-technology.list-categories-structure
- name: Elg Search Treatment Technology.List Structure
  property_count: 1
  slug: elg-search-treatment-technology.list-structure
- name: Elg Search Treatment Technology.Read Category Structure
  property_count: 1
  slug: elg-search-treatment-technology.read-category-structure
- name: Elg Search Treatment Technology.Read Structure
  property_count: 1
  slug: elg-search-treatment-technology.read-structure
- name: Elg Search Wastestream Process.Limitations Structure
  property_count: 1
  slug: elg-search-wastestream-process.limitations-structure
- name: Envirofacts Row Structure
  property_count: 0
  slug: envirofacts-row-structure
- name: Envirofacts Uv Daily Structure
  property_count: 5
  slug: envirofacts-uv-daily-structure
- name: Envirofacts Uv Hourly Structure
  property_count: 5
  slug: envirofacts-uv-hourly-structure
- name: Mywaterway Generic Structure
  property_count: 1
  slug: mywaterway-generic-structure
jsonld:
- class_count: 3
  name: Epa Aqs Context
  property_count: 7
  slug: epa-aqs-context
- class_count: 14
  name: Epa Cam Account Context
  property_count: 64
  slug: epa-cam-account-context
- class_count: 8
  name: Epa Cam Camd Services Context
  property_count: 21
  slug: epa-cam-camd-services-context
- class_count: 33
  name: Epa Cam Emissions Context
  property_count: 74
  slug: epa-cam-emissions-context
- class_count: 5
  name: Epa Cam Facilities Context
  property_count: 36
  slug: epa-cam-facilities-context
- class_count: 12
  name: Epa Cam Master Data Context
  property_count: 48
  slug: epa-cam-master-data-context
- class_count: 66
  name: Epa Cam Monitor Plan Context
  property_count: 306
  slug: epa-cam-monitor-plan-context
- class_count: 59
  name: Epa Cam Qa Cert Context
  property_count: 344
  slug: epa-cam-qa-cert-context
- class_count: 37
  name: Epa Cam Streaming Context
  property_count: 138
  slug: epa-cam-streaming-context
- class_count: 48
  name: Epa Cip Service Context
  property_count: 238
  slug: epa-cip-service-context
- class_count: 5
  name: Epa Context
  property_count: 1
  slug: epa-context
- class_count: 3
  name: Epa Csb Rebate Context
  property_count: 3
  slug: epa-csb-rebate-context
- class_count: 18
  name: Epa Echo Air Context
  property_count: 198
  slug: epa-echo-air-context
- class_count: 17
  name: Epa Echo All Context
  property_count: 256
  slug: epa-echo-all-context
- class_count: 43
  name: Epa Echo Case Context
  property_count: 214
  slug: epa-echo-case-context
- class_count: 30
  name: Epa Echo Cwa Context
  property_count: 367
  slug: epa-echo-cwa-context
- class_count: 158
  name: Epa Echo Dfr Context
  property_count: 654
  slug: epa-echo-dfr-context
- class_count: 13
  name: Epa Echo Effluent Context
  property_count: 86
  slug: epa-echo-effluent-context
- class_count: 19
  name: Epa Echo Rcra Context
  property_count: 174
  slug: epa-echo-rcra-context
- class_count: 7
  name: Epa Echo Sdw Context
  property_count: 98
  slug: epa-echo-sdw-context
- class_count: 27
  name: Epa Elg Search Context
  property_count: 1
  slug: epa-elg-search-context
- class_count: 5
  name: Epa Envirofacts Context
  property_count: 7
  slug: epa-envirofacts-context
- class_count: 3
  name: Epa Mywaterway Context
  property_count: 1
  slug: epa-mywaterway-context
layout: provider
modified: '2026-05-29'
name: EPA — U.S. Environmental Protection Agency
nav: Providers
network: true
overview: 'EPA — U.S. Environmental Protection Agency publishes 128 APIs on the [APIs.io](https://apis.io/) network, including Account Type Codes API, Accounts API, Air Emission Testing API, and 125 more. Tagged areas include Government, Environmental, Open Data, Air Quality, and Water Quality.


  The EPA — U.S. Environmental Protection Agency catalog on APIs.io includes 23 JSON-LD contexts and 2 Spectral governance rulesets.


  EPA — U.S. Environmental Protection Agency''s developer surface includes authentication, API reference, getting-started guide, documentation, engineering blog, YouTube channel, support, and 22 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 11
  name: Epa Rate Limits
  slug: epa-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: EPA — U.S. Environmental Protection Agency API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: epa-jsonschema-spectral-rules
- effective_rule_count: 30
  extends:
  - '@stoplight/spectral-rulesets/dist/oas'
  name: EPA — U.S. Environmental Protection Agency API Rules
  rule_count: 30
  severity_counts:
    error: 10
    hint: 0
    info: 3
    warn: 17
  slug: epa-rules
score:
  band: strong
  composite: 60.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 35.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.1
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 28.8
    contract_quality: 70.4
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 42.1
  previous_composite: 60.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 92.2
      derived: 0
      marker_coverage: 0.0
      total: 128
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 55.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/epa/refs/heads/main/screenshots/epa-2026-06-20T180747.png
security:
- kind: authentication
  name: Epa Authentication
  slug: epa-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Epa Domain Security
  slug: epa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: epa
solutions:
- description: How's My Waterway, AirNow, and Insect Repellents are designed for consumer use.
  name: Public-Facing Awareness
- description: ECHO, RCRAInfo, NPDES eDMR, e-Manifest support regulated-entity reporting workflows.
  name: Regulatory Compliance
- description: CTX, ToxCast, ToxRefDB, EPA HTTK, FrEDI underpin chemical safety and climate research.
  name: Scientific Research
- description: FRS Submit, SoR, Grants, CSB Rebate APIs support EPA program operations and grantees.
  name: Internal Government
tags:
- Government
- Environmental
- Open Data
- Air Quality
- Water Quality
- Hazardous Waste
- Compliance
- Emissions
use_cases:
- description: Overlay TRI, ECHO, and AQS data with demographic layers to identify cumulative impacts.
  name: Environmental Justice Analysis
- description: Use ECHO and the Detailed Facility Report to vet sites in M&A diligence or permit reviews.
  name: Compliance Screening
- description: Combine AQS observations with NWS / EPA AirNow forecasts for public-facing apps.
  name: Air Quality Forecasting
- description: Integrate the e-Manifest API into waste generator and transporter logistics systems.
  name: Hazardous Waste Tracking
- description: Use SDWIS via ECHO to monitor public water system violations and inform consumer notifications.
  name: Drinking Water Reporting
- description: Pull CAM emissions and GHGRP data for power-sector carbon analytics and FrEDI-style impact modeling.
  name: Climate / Decarbonization
- description: Use CTX (Chemical, Hazard, Bioactivity, Exposure) data plus ToxCast/ToxRefDB to triage substances.
  name: Chemical Risk Assessment
- description: Combine ATTAINS impairments, How's My Waterway, and StreamCat metrics for restoration planning.
  name: Watershed Restoration
website: https://www.epa.gov
---
