---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 87
  human_in_the_loop: 0
  name: Hint Health Agentic Access
  operation_count: 153
  slug: hint-health-agentic-access
  summary_line: 153 operations · 87 acting
api_count: 2
apis:
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The AccountAccessToken API from Hint Health — 1 operation(s) for accountaccesstoken.
  name: Hint Health AccountAccessToken API
  phrasing_intents:
  - id: AccountAccessToken.CreateAcccessToken
    intent: Create a patient portal access link
    question: Can I send an already-authenticated patient straight into their patient portal?
  phrasing_ops: 1
  slug: hint-health-accountaccesstoken-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Affiliate API from Hint Health — 2 operation(s) for affiliate.
  name: Hint Health Affiliate API
  phrasing_intents:
  - id: Affiliate.ListAffiliates
    intent: List affiliates
    question: Which affiliates is the practice working with?
  - id: Affiliate.ShowPatientAffiliate
    intent: Find a patient's affiliate
    question: Which affiliate is a patient assigned to?
  phrasing_ops: 2
  slug: hint-health-affiliate-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The AffiliateBill API from Hint Health — 1 operation(s) for affiliatebill.
  name: Hint Health AffiliateBill API
  phrasing_intents:
  - id: AffiliateBill.ListAffiliateBills
    intent: List bills for an affiliate
    question: What bills have been sent to an affiliate?
  phrasing_ops: 1
  slug: hint-health-affiliatebill-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The AffiliatePatient API from Hint Health — 2 operation(s) for affiliatepatient.
  name: Hint Health AffiliatePatient API
  phrasing_intents:
  - id: AffiliatePatient.CreateAffiliatePatient
    intent: Assign a patient to an affiliate
    question: Can I link a patient to an affiliate?
  - id: AffiliatePatient.DestroyAffiliatePatient
    intent: Remove a patient from an affiliate
    question: Can I take a patient off an affiliation?
  phrasing_ops: 2
  slug: hint-health-affiliatepatient-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Charge API from Hint Health — 1 operation(s) for charge.
  name: Hint Health Charge API
  phrasing_intents:
  - id: Charge.CreateCharge
    intent: Charge a patient for an item
    question: Can I bill a patient for a product or service from the catalog?
  phrasing_ops: 1
  slug: hint-health-charge-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The ChargeItem API from Hint Health — 2 operation(s) for chargeitem.
  name: Hint Health ChargeItem API
  phrasing_intents:
  - id: ChargeItem.CreateChargeItem
    intent: Create a charge item
    question: How do I add a new billable product or service to my catalog?
  - id: ChargeItem.ListAllChargeItems
    intent: List charge items
    question: What billable items and services does my practice have set up?
  - id: ChargeItem.DeleteChargeItem
    intent: Delete a charge item
    question: Can I remove a service we no longer offer from the catalog?
  - id: ChargeItem.ShowChargeItem
    intent: Look up a charge item
    question: What is the current price of a specific charge item?
  - id: ChargeItem.UpdateChargeItem
    intent: Update a charge item
    question: Can I change the price of an existing charge item?
  phrasing_ops: 5
  slug: hint-health-chargeitem-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The ClinicalNoteInteraction API from Hint Health — 2 operation(s) for clinicalnoteinteraction.
  name: Hint Health ClinicalNoteInteraction API
  phrasing_intents:
  - id: ClinicalNoteInteraction.CreateClinicalNoteInteraction
    intent: Add a clinical note to a patient's chart
    question: How do I post a clinical note from my system into a patient's chart?
  - id: ClinicalNoteInteraction.ShowClinicalNoteInteraction
    intent: Get a clinical note on a patient
    question: Can I read back a clinical note I posted to a patient's chart?
  - id: ClinicalNoteInteraction.UpdateClinicalNoteInteraction
    intent: Edit an existing clinical note
    question: Is it possible to correct the text of a clinical note already in a patient's chart?
  phrasing_ops: 3
  slug: hint-health-clinicalnoteinteraction-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Company API from Hint Health — 3 operation(s) for company.
  name: Hint Health Company API
  phrasing_intents:
  - id: Company.CreateCompany
    intent: Add an employer company
    question: What is needed to add a new employer company to my practice?
  - id: Company.ListAllCompanies
    intent: List employer companies
    question: Which employer companies are set up in my practice?
  - id: Company.DeactivateCompany
    intent: Deactivate an employer company
    question: How do I deactivate a company that is no longer a client?
  - id: Company.ShowCompany
    intent: Get one employer company
    question: What details are on file for a specific company?
  - id: Company.UpdateCompany
    intent: Update a company's name, address or phones
    question: How do I change a company's address or phone numbers?
  phrasing_ops: 5
  slug: hint-health-company-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The CompanyPlan API from Hint Health — 2 operation(s) for companyplan.
  name: Hint Health CompanyPlan API
  phrasing_intents:
  - id: CompanyPlan.CreateCompanyPlan
    intent: Offer a plan to a company
    question: Can I make a membership plan available to an employer company?
  - id: CompanyPlan.ListCompanyPlans
    intent: List plans offered to a company
    question: Which membership plans are offered to an employer company?
  - id: CompanyPlan.DestroyCompanyPlan
    intent: Remove a plan from a company
    question: Is there a way to stop offering a plan to an employer company?
  - id: CompanyPlan.UpdateCompanyPlan
    intent: Open or close a company plan to enrollment
    question: How do I close enrollment on a plan a company already offers?
  phrasing_ops: 4
  slug: hint-health-companyplan-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Coupon API from Hint Health — 2 operation(s) for coupon.
  name: Hint Health Coupon API
  phrasing_intents:
  - id: Coupon.ListAllCoupons
    intent: List the practice's coupons
    question: Which coupons does my practice offer?
  - id: Coupon.ShowCoupon
    intent: Get one coupon
    question: How do I look up the details of a specific coupon?
  phrasing_ops: 2
  slug: hint-health-coupon-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Credit API from Hint Health — 2 operation(s) for credit.
  name: Hint Health Credit API
  phrasing_intents:
  - id: Credit.CreateCredit
    intent: Give a patient an account credit
    question: How do I add a credit to a patient's account?
  - id: Credit.ListAllCredits
    intent: List a patient's credits
    question: What account credits does a patient have?
  - id: Credit.UpdateCredit
    intent: Change an existing patient credit
    question: Can I adjust the amount of a credit I already gave a patient?
  phrasing_ops: 3
  slug: hint-health-credit-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The CreditCategory API from Hint Health — 2 operation(s) for creditcategory.
  name: Hint Health CreditCategory API
  phrasing_intents:
  - id: CreditCategory.CreateCreditCategory
    intent: Create a credit category
    question: Can I add a new category for grouping patient credits?
  - id: CreditCategory.ListCreditCategories
    intent: List credit categories
    question: What credit categories are set up for my practice?
  - id: CreditCategory.DeleteCreditCategory
    intent: Delete a credit category
    question: Can I remove a credit category we no longer use?
  - id: CreditCategory.ShowCreditCategory
    intent: Look up a credit category
    question: What are the details of one credit category?
  - id: CreditCategory.UpdateCreditCategory
    intent: Rename a credit category
    question: Can I rename an existing credit category?
  phrasing_ops: 5
  slug: hint-health-creditcategory-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The CustomerInvoice API from Hint Health — 6 operation(s) for customerinvoice.
  name: Hint Health CustomerInvoice API
  phrasing_intents:
  - id: CustomerInvoice.CreateCustomerInvoice
    intent: Create a customer invoice
    question: How do I create a new invoice for a patient through the API?
  - id: CustomerInvoice.ListAllCustomerInvoices
    intent: List customer invoices
    question: Which customer invoices has my practice created recently?
  - id: CustomerInvoice.CreatePDF
    intent: Generate a PDF link for a customer invoice
    question: Can I get a downloadable PDF of a customer invoice?
  - id: CustomerInvoice.DeleteCustomerInvoice
    intent: Delete a customer invoice
    question: Can I permanently delete a customer invoice I created by mistake?
  - id: CustomerInvoice.ShowCustomerInvoice
    intent: Look up one customer invoice
    question: What status is a specific customer invoice in, paid or disputed or still a draft?
  - id: CustomerInvoice.UpdateCustomerInvoice
    intent: Update a customer invoice
    question: Can I change which patient an existing customer invoice belongs to?
  - id: CustomerInvoice.IssueCustomerInvoice
    intent: Issue a draft customer invoice
    question: How do I finalize a draft invoice so it is issued to the patient?
  - id: CustomerInvoice.ReturnToDraft
    intent: Return a customer invoice to draft
    question: Can I put an issued invoice back into draft so I can fix it?
  phrasing_ops: 10
  slug: hint-health-customerinvoice-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The CustomerInvoiceCharge API from Hint Health — 2 operation(s) for customerinvoicecharge.
  name: Hint Health CustomerInvoiceCharge API
  phrasing_intents:
  - id: CustomerInvoiceCharge.CreateCustomerInvoiceCharge
    intent: Add a line charge to a customer invoice
    question: How do I add a charge line to a patient's customer invoice?
  - id: CustomerInvoiceCharge.DeleteCustomerInvoiceCharge
    intent: Remove a charge from a customer invoice
    question: Can I delete a wrong line item from a customer invoice?
  - id: CustomerInvoiceCharge.UpdateCustomerInvoiceCharge
    intent: Edit a charge on a customer invoice
    question: How do I change the price or quantity of a charge already on an invoice?
  phrasing_ops: 3
  slug: hint-health-customerinvoicecharge-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The CustomerInvoicePayment API from Hint Health — 2 operation(s) for customerinvoicepayment.
  name: Hint Health CustomerInvoicePayment API
  phrasing_intents:
  - id: CustomerInvoicePayment.CreatePayment
    intent: Record a payment on a customer invoice
    question: How do I record a payment the patient made outside the system?
  - id: CustomerInvoicePayment.ListAllPayments
    intent: List payments on a customer invoice
    question: What payments have been made against a customer invoice?
  - id: CustomerInvoicePayment.ShowPayment
    intent: Look up one invoice payment
    question: What are the details of a specific payment on an invoice?
  phrasing_ops: 3
  slug: hint-health-customerinvoicepayment-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The DocumentInteraction API from Hint Health — 2 operation(s) for documentinteraction.
  name: Hint Health DocumentInteraction API
  phrasing_intents:
  - id: DocumentInteraction.CreateDocumentInteraction
    intent: Add a document to a patient's record
    question: How do I attach a document from my system to a patient's record?
  - id: DocumentInteraction.ShowDocumentInteraction
    intent: Get a document on a patient's record
    question: Can I fetch a document interaction I added to a patient?
  - id: DocumentInteraction.UpdateDocumentInteraction
    intent: Update a document on a patient's record
    question: How do I change the status or body of a patient document I already posted?
  phrasing_ops: 3
  slug: hint-health-documentinteraction-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The EmployeeDivision API from Hint Health — 1 operation(s) for employeedivision.
  name: Hint Health EmployeeDivision API
  phrasing_intents:
  - id: EmployeeDivision.ListAllEmployeeDivisions
    intent: List a company's employee divisions
    question: What employee divisions does an employer client have?
  phrasing_ops: 1
  slug: hint-health-employeedivision-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The GlobalWebhookEndpoint API from Hint Health — 2 operation(s) for globalwebhookendpoint.
  name: Hint Health GlobalWebhookEndpoint API
  phrasing_intents:
  - id: GlobalWebhookEndpoint.CreateWebhookEndpointLegacy
    intent: Register a global webhook endpoint (legacy)
    question: How do I add a global webhook URL that is not tied to one integration?
  - id: GlobalWebhookEndpoint.WebhookEndpointsLegacy
    intent: List global webhook endpoints (legacy)
    question: Which global webhook endpoints are registered across all my integrations?
  - id: GlobalWebhookEndpoint.DeleteWebhookEndpointLegacy
    intent: Delete a global webhook endpoint (legacy)
    question: Does deleting a global webhook endpoint cancel deliveries still pending or retrying?
  - id: GlobalWebhookEndpoint.ShowWebhookEndpointLegacy
    intent: Get one global webhook endpoint (legacy)
    question: Can I look up a single global webhook endpoint by id?
  - id: GlobalWebhookEndpoint.UpdateWebhookEndpointLegacy
    intent: Change a global webhook endpoint URL (legacy)
    question: How do I change the URL of a global webhook endpoint?
  phrasing_ops: 5
  slug: hint-health-globalwebhookendpoint-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Integration API from Hint Health — 4 operation(s) for integration.
  name: Hint Health Integration API
  phrasing_intents:
  - id: Integration.ActivateIntegration
    intent: Activate an integration
    question: Can I activate an integration that is still pending?
  - id: Integration.DeactivateIntegration
    intent: Deactivate an integration
    question: Is there a way to deactivate an integration with a practice?
  - id: Integration.ListAllIntegrations
    intent: List my integrations
    question: Which practice integrations do I have?
  - id: Integration.ShowIntegration
    intent: Get one integration
    question: What are the details and status of one integration?
  - id: Integration.UpdateIntegration
    intent: Override an integration's webhook URL
    question: Can I send one integration's webhooks to a different URL than my default?
  phrasing_ops: 5
  slug: hint-health-integration-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The IntegrationRecord API from Hint Health — 1 operation(s) for integrationrecord.
  name: Hint Health IntegrationRecord API
  phrasing_intents:
  - id: IntegrationRecord.ListAllIntegrationRecords
    intent: List a patient's integration records
    question: Which integration records link a patient to outside systems?
  phrasing_ops: 1
  slug: hint-health-integrationrecord-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Interaction API from Hint Health — 1 operation(s) for interaction.
  name: Hint Health Interaction API
  phrasing_intents:
  - id: Interaction.ListAllInteractions
    intent: List patient interactions
    question: What interactions have been logged for a patient?
  - id: Interaction.ListInteractionFileDownloadUrls
    intent: Get download links for all interaction files
    question: Can I download every file attached to an interaction at once?
  - id: Interaction.GetInteractionFileDownloadUrl
    intent: Get a download link for one interaction file
    question: Can I get a download link for just one file on an interaction?
  phrasing_ops: 3
  slug: hint-health-interaction-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The InteractionNotifications API from Hint Health — 1 operation(s) for interactionnotifications.
  name: Hint Health InteractionNotifications API
  phrasing_intents:
  - id: InteractionNotifications.CreateInteractionNotification
    intent: Send a notification about an interaction
    question: Can I notify the care team about a specific interaction?
  phrasing_ops: 1
  slug: hint-health-interactionnotifications-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Invoice API from Hint Health — 2 operation(s) for invoice.
  name: Hint Health Invoice API
  phrasing_intents:
  - id: Invoice.ListAllInvoices
    intent: List an employer company's invoices
    question: Which invoices have been issued to an employer company?
  - id: Invoice.ShowInvoice
    intent: Get one company invoice
    question: How do I look up a single invoice for a company?
  phrasing_ops: 2
  slug: hint-health-invoice-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The InvoicePayment API from Hint Health — 2 operation(s) for invoicepayment.
  name: Hint Health InvoicePayment API
  phrasing_intents:
  - id: InvoicePayment.CreatePayment
    intent: Record a payment on a company invoice
    question: How do I record a check or external payment against a company invoice?
  - id: InvoicePayment.ListAllPayments
    intent: List payments on a company invoice
    question: Which payments have been applied to an employer company's invoice?
  - id: InvoicePayment.ShowPayment
    intent: Get one payment on a company invoice
    question: Can I look up a single payment applied to a company invoice?
  phrasing_ops: 3
  slug: hint-health-invoicepayment-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The LabInteraction API from Hint Health — 2 operation(s) for labinteraction.
  name: Hint Health LabInteraction API
  phrasing_intents:
  - id: LabInteraction.CreateLabInteraction
    intent: Record a lab order for a patient
    question: How do I push a lab order and its results into a patient's chart?
  - id: LabInteraction.ShowLabInteraction
    intent: Look up a patient's lab interaction
    question: What results came back on a specific lab order?
  - id: LabInteraction.UpdateLabInteraction
    intent: Update a patient's lab interaction
    question: Can I add results to a lab order after it was created?
  phrasing_ops: 3
  slug: hint-health-labinteraction-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Location API from Hint Health — 2 operation(s) for location.
  name: Hint Health Location API
  phrasing_intents:
  - id: Location.CreateLocation
    intent: Add a practice location
    question: How do I add a new clinic location?
  - id: Location.ListLocations
    intent: List practice locations
    question: What clinic locations does the practice have?
  - id: Location.DeleteLocation
    intent: Delete a location
    question: Can I delete a clinic location that has closed?
  - id: Location.ShowLocation
    intent: Look up a location
    question: What address and phone number does a specific location have?
  - id: Location.UpdateLocation
    intent: Update a location
    question: Can I change the phone number on an existing location?
  phrasing_ops: 5
  slug: hint-health-location-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Membership API from Hint Health — 6 operation(s) for membership.
  name: Hint Health Membership API
  phrasing_intents:
  - id: Membership.BillMembership
    intent: Bill a membership from a start date
    question: How do I generate a bill for a patient's membership starting on a specific date?
  - id: Membership.CancelMembership
    intent: Cancel a patient membership
    question: How do I cancel a patient's membership with an end date and a reason?
  - id: Membership.ConfirmMembership
    intent: Confirm an unconfirmed membership
    question: How do I confirm a membership that is still waiting for confirmation?
  - id: Membership.CreateMembership
    intent: Enroll patients in a membership plan
    question: How do I enroll a patient in a membership plan with Hint?
  - id: Membership.ListAllMemberships
    intent: List the practice's memberships
    question: Which memberships does my practice have right now?
  - id: Membership.DeleteMembership
    intent: Delete a membership record
    question: How do I delete a membership that was created by mistake?
  - id: Membership.ShowMembership
    intent: Look up one membership and its status
    question: What is the current status of a specific membership, active, unpaid or ended?
  - id: Membership.UpdateMembership
    intent: Change an existing membership's plan or terms
    question: How do I switch an existing membership to a different plan?
  phrasing_ops: 9
  slug: hint-health-membership-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The MembershipContract API from Hint Health — 3 operation(s) for membershipcontract.
  name: Hint Health MembershipContract API
  phrasing_intents:
  - id: MembershipContract.ListAllMembershipContracts
    intent: List a membership's contracts
    question: Which contract terms has a membership gone through?
  - id: MembershipContract.RenewMembershipContract
    intent: Renew a membership contract
    question: Can I renew a membership contract for another term?
  - id: MembershipContract.UpdateMembershipContract
    intent: Change a contract's end or billing end date
    question: How do I change the end date of a membership contract?
  phrasing_ops: 3
  slug: hint-health-membershipcontract-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The MembershipMember API from Hint Health — 3 operation(s) for membershipmember.
  name: Hint Health MembershipMember API
  phrasing_intents:
  - id: MembershipMember.CancelMembershipMember
    intent: Cancel a member on a membership
    question: How do I cancel one person on a membership and record why?
  - id: MembershipMember.CreateMembershipMember
    intent: Add a patient to a membership
    question: Can I add a dependent to an existing membership?
  - id: MembershipMember.ListMembershipMembers
    intent: List members on a membership
    question: Who is covered under a particular membership?
  - id: MembershipMember.DestroyMembershipMember
    intent: Delete a member from a membership
    question: Can I delete a member record that was added to the wrong membership?
  - id: MembershipMember.ShowMembershipMember
    intent: Look up one membership member
    question: What are the details of a specific member on a membership?
  - id: MembershipMember.UpdateMembershipMember
    intent: Update a membership member
    question: Can I change a member's start date after they join a membership?
  phrasing_ops: 6
  slug: hint-health-membershipmember-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Partner API from Hint Health — 1 operation(s) for partner.
  name: Hint Health Partner API
  phrasing_intents:
  - id: Partner.ShowPartnerLegacy
    intent: View my partner profile (legacy)
    question: Where do I see my partner profile with marketing and support URLs under the older route?
  - id: Partner.UpdatePartnerLegacy
    intent: Update partner listing details (legacy)
    question: How do I change my partner marketing URL, support URL or product description?
  - id: Partner.ShowPartner
    intent: View my partner account
    question: What name and contact email are on my partner account?
  - id: Partner.UpdatePartner
    intent: Rename my partner account or change its email
    question: How do I rename my partner account?
  phrasing_ops: 4
  slug: hint-health-partner-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The PartnerCharge API from Hint Health — 2 operation(s) for partnercharge.
  name: Hint Health PartnerCharge API
  phrasing_intents:
  - id: PartnerCharge.CreatePartnerCharge
    intent: Bill a partner charge
    question: Can a partner charge be billed to either the patient or the practice?
  - id: PartnerCharge.ListAllPartnerCharges
    intent: List partner charges
    question: What charges have partners billed through the practice?
  - id: PartnerCharge.ShowPartnerCharge
    intent: Look up a partner charge
    question: What are the details of a specific partner charge?
  phrasing_ops: 3
  slug: hint-health-partnercharge-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The PartnerInteraction API from Hint Health — 2 operation(s) for partnerinteraction.
  name: Hint Health PartnerInteraction API
  phrasing_intents:
  - id: PartnerInteraction.CreatePartnerInteraction
    intent: Log a partner interaction on a patient
    question: How do I log an event from my partner app on a patient's timeline?
  - id: PartnerInteraction.ShowPartnerInteraction
    intent: Get a partner interaction on a patient
    question: Can I fetch a partner interaction I logged on a patient?
  - id: PartnerInteraction.UpdatePartnerInteraction
    intent: Update a partner interaction's status
    question: Is it possible to change the status of a partner interaction already logged?
  phrasing_ops: 3
  slug: hint-health-partnerinteraction-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Patient API from Hint Health — 3 operation(s) for patient.
  name: Hint Health Patient API
  phrasing_intents:
  - id: Patient.CreatePatient
    intent: Register a new patient
    question: What do I need to add a new patient to the practice?
  - id: Patient.ListAllPatients
    intent: List patients
    question: How do I get a list of all patients in my practice?
  - id: Patient.DeletePatient
    intent: Delete a patient
    question: Can I permanently delete a patient record?
  - id: Patient.ShowPatient
    intent: Look up a patient
    question: What is a specific patient's membership status?
  - id: Patient.UpdatePatient
    intent: Update a patient's details
    question: Can I change an existing patient's address or phone number?
  - id: Patient.MatchPatients
    intent: Find patients matching a name and details
    question: Does a patient with this name and birth date already exist before I create one?
  phrasing_ops: 6
  slug: hint-health-patient-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Plan API from Hint Health — 1 operation(s) for plan.
  name: Hint Health Plan API
  phrasing_intents:
  - id: Plan.ListAllPlans
    intent: List membership plans
    question: What membership plans does the practice offer?
  phrasing_ops: 1
  slug: hint-health-plan-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Practice API from Hint Health — 1 operation(s) for practice.
  name: Hint Health Practice API
  phrasing_intents:
  - id: Practice.GetPractice
    intent: View the practice profile
    question: Where can I see my practice's name, address and contact details?
  - id: Practice.UpdatePractice
    intent: Update the practice profile
    question: How do I change my practice's address or phone numbers?
  phrasing_ops: 2
  slug: hint-health-practice-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Practitioner API from Hint Health — 2 operation(s) for practitioner.
  name: Hint Health Practitioner API
  phrasing_intents:
  - id: Practitioner.CreatePractitioner
    intent: Add a practitioner
    question: How do I add a new doctor or clinician to the practice?
  - id: Practitioner.ProviderPractitioners
    intent: List practitioners
    question: Which practitioners work at the practice?
  - id: Practitioner.DeletePractitioner
    intent: Delete a practitioner
    question: Can I remove a practitioner who has left the practice?
  - id: Practitioner.ShowPractitioner
    intent: Look up a practitioner
    question: What is a specific practitioner's bio and education?
  - id: Practitioner.UpdatePractitioner
    intent: Update a practitioner
    question: Can I update a practitioner's bio or photo?
  phrasing_ops: 5
  slug: hint-health-practitioner-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Quote API from Hint Health — 1 operation(s) for quote.
  name: Hint Health Quote API
  phrasing_intents:
  - id: Quote.CreateQuote
    intent: Quote a membership price
    question: How much would a membership plan cost for a given set of members?
  phrasing_ops: 1
  slug: hint-health-quote-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The SignupAttempt API from Hint Health — 2 operation(s) for signupattempt.
  name: Hint Health SignupAttempt API
  phrasing_intents:
  - id: SignupAttempt.ListSignupAttempts
    intent: List signup attempts
    question: Who started signing up online but did not finish?
  - id: SignupAttempt.ShowSignupAttempt
    intent: Look up a signup attempt
    question: What details were captured on a specific signup attempt?
  phrasing_ops: 2
  slug: hint-health-signupattempt-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The SocialSecurityNumber API from Hint Health — 1 operation(s) for socialsecuritynumber.
  name: Hint Health SocialSecurityNumber API
  phrasing_intents:
  - id: SocialSecurityNumber.ShowSocialSecurityNumber
    intent: Retrieve a patient's Social Security number
    question: Can I retrieve the SSN on file for a patient?
  phrasing_ops: 1
  slug: hint-health-socialsecuritynumber-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Sponsorship API from Hint Health — 2 operation(s) for sponsorship.
  name: Hint Health Sponsorship API
  phrasing_intents:
  - id: Sponsorship.CreateSponsorship
    intent: Sponsor a patient under a company
    question: How do I add an employee as a sponsored patient under their employer?
  - id: Sponsorship.ListSponsorships
    intent: List a company's sponsored patients
    question: Which patients does an employer company sponsor?
  - id: Sponsorship.DestroySponsorship
    intent: Remove a company sponsorship
    question: If I remove a subscriber's sponsorship, are their dependents removed too?
  - id: Sponsorship.ShowSponsorhip
    intent: Get one company sponsorship
    question: Can I look up a single sponsorship at a company?
  - id: Sponsorship.UpdateSponsorship
    intent: Change a sponsorship's type or external id
    question: How do I change the sponsorship type for an employee?
  phrasing_ops: 5
  slug: hint-health-sponsorship-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Supplements API from Hint Health — 2 operation(s) for supplements.
  name: Hint Health Supplements API
  phrasing_intents:
  - id: Supplements.CreateSupplement
    intent: Record a supplement for a patient
    question: How do I add a supplement to a patient's record?
  - id: Supplements.ListAllPatientSupplements
    intent: List a patient's supplements
    question: What supplements is a patient currently taking?
  - id: Supplements.DeleteSupplement
    intent: Delete a patient supplement
    question: Can I remove a supplement the patient stopped taking?
  - id: Supplements.ShowSupplement
    intent: Look up one patient supplement
    question: What dose is recorded for a specific supplement on a patient?
  - id: Supplements.UpdateSupplement
    intent: Update a patient supplement
    question: Can I change the dose of a supplement already on a patient's record?
  phrasing_ops: 5
  slug: hint-health-supplements-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The User API from Hint Health — 1 operation(s) for user.
  name: Hint Health User API
  phrasing_intents:
  - id: User.ListUsers
    intent: List practice users
    question: Which staff users have access to my practice?
  phrasing_ops: 1
  slug: hint-health-user-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The AffiliateAncillaryCharge API from Hint Health — 1 operation(s) for affiliateancillarycharge.
  name: Hint Health Affiliate Ancillary Charge API
  phrasing_intents:
  - id: AffiliateAncillaryCharge.ListAffiliateAncillaryCharges
    intent: List ancillary charges across affiliates
    question: Which ancillary charges have my network's affiliates added?
  phrasing_ops: 1
  slug: hint-health-affiliateancillarycharge-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The App API from Hint Health — 1 operation(s) for app.
  name: Hint Health App API
  phrasing_intents:
  - id: App.GetProductApp
    intent: Get a product's embedded app settings
    question: What app configuration sits behind one of my products?
  - id: App.UpdateProductApp
    intent: Change a product app's handshake or roles
    question: How do I change the handshake URL on my product's existing app?
  - id: App.CreateProductApp
    intent: Create an embedded app for a product
    question: How do I set up an app with a handshake URL for my product?
  phrasing_ops: 3
  slug: hint-health-app-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Appointment API from Hint Health — 2 operation(s) for appointment.
  name: Hint Health Appointment API
  phrasing_intents:
  - id: Appointment.ListAllAppointmentTypes
    intent: List appointment types
    question: What kinds of appointments does the practice offer?
  - id: Appointment.ListAllAppointments
    intent: List appointments
    question: Which appointments are booked between two dates?
  phrasing_ops: 2
  slug: hint-health-appointment-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The AppSurface API from Hint Health — 2 operation(s) for appsurface.
  name: Hint Health App Surface API
  phrasing_intents:
  - id: AppSurface.CreateProductAppSurface
    intent: Add a surface to a product app
    question: How do I embed my app in a page or the clinical chart with a source URL?
  - id: AppSurface.UpdateProductAppSurface
    intent: Edit an existing app surface
    question: How do I change the source URL of an app surface already created?
  - id: AppSurface.DeleteProductAppSurface
    intent: Remove a surface from a product app
    question: Is there a way to remove an embedded surface from my product's app?
  phrasing_ops: 3
  slug: hint-health-appsurface-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Backend API from Hint Health — 2 operation(s) for backend.
  name: Hint Health Backend API
  phrasing_intents:
  - id: Backend.ListBackends
    intent: List partner backends
    question: Which backends does my partner account have?
  - id: Backend.ShowBackend
    intent: Look up a partner backend
    question: What webhook and OAuth settings does a specific backend have?
  - id: Backend.UpdateBackend
    intent: Update a partner backend's settings
    question: Can I pause webhook delivery for one of my backends?
  phrasing_ops: 3
  slug: hint-health-backend-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Installation API from Hint Health — 5 operation(s) for installation.
  name: Hint Health Installation API
  phrasing_intents:
  - id: Installation.ListInstallations
    intent: List partner app installations
    question: Which practices have installed my partner product?
  - id: Installation.ConnectInstallation
    intent: Exchange an install code for credentials
    question: How do I turn the authorization code from a practice install into API credentials?
  - id: Installation.ShowInstallation
    intent: Look up one installation
    question: What practice and product does a specific installation belong to?
  - id: Installation.ActivateInstallation
    intent: Activate a pending installation
    question: How do I activate an installation that is still pending?
  - id: Installation.DeactivateInstallation
    intent: Deactivate an installation
    question: Can I deactivate one installation without affecting the practice's other installs?
  phrasing_ops: 5
  slug: hint-health-installation-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The InstallationApiKeys API from Hint Health — 2 operation(s) for installationapikeys.
  name: Hint Health Installation API Keys API
  phrasing_intents:
  - id: InstallationApiKeys.ListApiKeys
    intent: List an installation's API keys
    question: Which API keys exist for an installation's practice connection?
  - id: InstallationApiKeys.CreateApiKey
    intent: Create an API key for an installation
    question: How do I generate a new API key for an installation?
  - id: InstallationApiKeys.UpdateApiKey
    intent: Relabel an installation API key
    question: Can I rename the label on an existing installation API key?
  - id: InstallationApiKeys.DeleteApiKey
    intent: Delete an installation API key
    question: Can I revoke a leaked API key on an installation?
  phrasing_ops: 4
  slug: hint-health-installationapikeys-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The InstallationWebhookEndpoints API from Hint Health — 2 operation(s) for installationwebhookendpoints.
  name: Hint Health Installation Webhook Endpoints API
  phrasing_intents:
  - id: InstallationWebhookEndpoints.ListWebhookEndpoints
    intent: List an installation's webhook endpoints
    question: Which webhook endpoints are registered for a product installation at a practice?
  - id: InstallationWebhookEndpoints.CreateWebhookEndpoint
    intent: Add a webhook endpoint to an installation
    question: How do I register a webhook URL for one product installation?
  - id: InstallationWebhookEndpoints.UpdateWebhookEndpoint
    intent: Change an installation webhook URL
    question: How do I change the URL of a webhook on a product installation?
  - id: InstallationWebhookEndpoints.DeleteWebhookEndpoint
    intent: Delete an installation webhook endpoint
    question: How do I remove a webhook endpoint from a product installation?
  phrasing_ops: 4
  slug: hint-health-installationwebhookendpoints-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The PartnerProductHighlight API from Hint Health — 2 operation(s) for partnerproducthighlight.
  name: Hint Health Partner Product Highlight API
  phrasing_intents:
  - id: PartnerProductHighlight.ListProductHighlights
    intent: List a product's highlights
    question: What highlights are shown on my partner product listing?
  - id: PartnerProductHighlight.CreateProductHighlight
    intent: Add a highlight to a product listing
    question: Can I add an image highlight to my product listing?
  - id: PartnerProductHighlight.UpdateProductHighlight
    intent: Update a product highlight
    question: Can I reorder the highlights on my product listing?
  - id: PartnerProductHighlight.DestroyProductHighlight
    intent: Delete a product highlight
    question: Can I remove an outdated highlight from my product listing?
  phrasing_ops: 4
  slug: hint-health-partnerproducthighlight-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The PartnerProductLink API from Hint Health — 2 operation(s) for partnerproductlink.
  name: Hint Health Partner Product Link API
  phrasing_intents:
  - id: PartnerProductLink.ListProductLinks
    intent: List a product's links
    question: Which links are attached to my product listing?
  - id: PartnerProductLink.CreateProductLink
    intent: Add a link to a product listing
    question: How do I add a link with UTM tracking to my product listing?
  - id: PartnerProductLink.UpdateProductLink
    intent: Edit a product link
    question: How do I change the URL or title of an existing product link?
  - id: PartnerProductLink.DestroyProductLink
    intent: Remove a link from a product
    question: Can I delete a link from my product listing?
  phrasing_ops: 4
  slug: hint-health-partnerproductlink-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The PartnerProductOverview API from Hint Health — 1 operation(s) for partnerproductoverview.
  name: Hint Health Partner Product Overview API
  phrasing_intents:
  - id: PartnerProductOverview.GetProductOverview
    intent: View a product's overview
    question: What description and images appear on my product's overview?
  - id: PartnerProductOverview.UpdateProductOverview
    intent: Edit a product's overview
    question: Can I rewrite the description on my product's overview?
  phrasing_ops: 2
  slug: hint-health-partnerproductoverview-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The PartnerProductPrecondition API from Hint Health — 2 operation(s) for partnerproductprecondition.
  name: Hint Health Partner Product Precondition API
  phrasing_intents:
  - id: PartnerProductPrecondition.ListProductPreconditions
    intent: List a product's install preconditions
    question: What preconditions must a practice meet before installing my product?
  - id: PartnerProductPrecondition.CreateProductPrecondition
    intent: Add a precondition to a product
    question: Can I require practices to complete a step before installing my product?
  - id: PartnerProductPrecondition.UpdateProductPrecondition
    intent: Update a product precondition
    question: Can I change the URL of an existing product precondition?
  - id: PartnerProductPrecondition.DestroyProductPrecondition
    intent: Delete a product precondition
    question: Can I drop a precondition that practices no longer need to meet?
  phrasing_ops: 4
  slug: hint-health-partnerproductprecondition-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Product API from Hint Health — 3 operation(s) for product.
  name: Hint Health Product API
  phrasing_intents:
  - id: Product.ListProducts
    intent: List my partner products
    question: Which marketplace products have I created as a partner?
  - id: Product.CreateProduct
    intent: Create a marketplace product
    question: What does it take to create a new product listing for the Hint marketplace?
  - id: Product.GetProduct
    intent: Get one partner product
    question: What details are stored on one of my products?
  - id: Product.UpdateProduct
    intent: Edit a partner product listing
    question: How do I change the name, summary or icon of an existing product?
  - id: Product.DestroyProduct
    intent: Delete a partner product
    question: Can I delete a product I no longer want listed?
  - id: Product.RequestProductReview
    intent: Submit a product for marketplace review
    question: What step sends my product for review before it goes live in the marketplace?
  phrasing_ops: 6
  slug: hint-health-product-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Testimonial API from Hint Health — 2 operation(s) for testimonial.
  name: Hint Health Testimonial API
  phrasing_intents:
  - id: Testimonial.ListProductTestimonials
    intent: List a product's testimonials
    question: What customer testimonials are on my partner product listing?
  - id: Testimonial.CreateProductTestimonial
    intent: Add a testimonial to a product
    question: Can I add a customer quote to my product listing?
  - id: Testimonial.UpdateProductTestimonial
    intent: Update a product testimonial
    question: Can I edit the wording of an existing testimonial?
  - id: Testimonial.DestroyProductTestimonial
    intent: Delete a product testimonial
    question: Can I remove a testimonial from my product listing?
  phrasing_ops: 4
  slug: hint-health-testimonial-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The WebhookRequest API from Hint Health — 1 operation(s) for webhookrequest.
  name: Hint Health Webhook Request API
  phrasing_intents:
  - id: WebhookRequest.ListWebhookRequests
    intent: List webhook delivery attempts
    question: Which webhook deliveries failed or are still retrying?
  phrasing_ops: 1
  slug: hint-health-webhookrequest-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The OAuth API from Hint Health — 1 operation(s) for oauth.
  name: Hint Health O Auth API
  phrasing_intents:
  - id: OAuth.OauthTokens
    intent: Exchange an authorization code for an access token
    question: What call exchanges an OAuth authorization code for an access token?
  phrasing_ops: 1
  slug: hint-health-oauth-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The API Key API from Hint Health — 1 operation(s) for api key.
  name: Hint Health API Key API
  phrasing_intents:
  - id: ApiKey.ListApiKeys
    intent: List my partner API keys
    question: Which API keys exist on my partner account?
  - id: ApiKey.CreateApiKey
    intent: Create a partner API key
    question: How do I generate a new API key for my partner account?
  phrasing_ops: 2
  slug: hint-health-api-key-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Cancellation Reason API from Hint Health — 1 operation(s) for cancellation reason.
  name: Hint Health Cancellation Reason API
  phrasing_intents:
  - id: CancellationReason.ListCancellationReasons
    intent: List membership cancellation reasons
    question: Which cancellation reasons can I choose from when ending a membership?
  phrasing_ops: 1
  slug: hint-health-cancellation-reason-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Credit Line API from Hint Health — 1 operation(s) for credit line.
  name: Hint Health Credit Line API
  phrasing_intents:
  - id: CreditLine.ListCreditLines
    intent: List credit lines
    question: Which credit lines exist for patient credits?
  phrasing_ops: 1
  slug: hint-health-credit-line-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Form Response API from Hint Health — 2 operation(s) for form response.
  name: Hint Health Form Response API
  phrasing_intents:
  - id: FormResponse.ListAllFormResponses
    intent: List a patient's form responses
    question: What forms has a patient filled out?
  - id: FormResponse.ShowFormResponse
    intent: Look up one form response
    question: What answers did a patient give on a specific form?
  phrasing_ops: 2
  slug: hint-health-form-response-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Lead Source API from Hint Health — 2 operation(s) for lead source.
  name: Hint Health Lead Source API
  phrasing_intents:
  - id: LeadSource.DeleteLeadSource
    intent: Delete a lead source
    question: Can I remove a referral source we no longer track?
  - id: LeadSource.UpdateLeadSource
    intent: Rename a lead source
    question: Can I rename an existing lead source?
  - id: LeadSource.LeadSource
    intent: Create a lead source
    question: Can I add a new lead source for a marketing campaign?
  - id: LeadSource.LeadSources
    intent: List lead sources
    question: Which lead sources are configured for tracking where patients come from?
  phrasing_ops: 4
  slug: hint-health-lead-source-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Payment Method API from Hint Health — 3 operation(s) for payment method.
  name: Hint Health Payment Method API
  phrasing_intents:
  - id: PaymentMethod.CreatePaymentMethod
    intent: Save a tokenized payment method for a patient
    question: How do I attach a tokenized card or bank account to a patient?
  - id: PaymentMethod.ListAllPaymentMethods
    intent: List a patient's payment methods
    question: Which cards or bank accounts does a patient have on file?
  - id: PaymentMethod.CreateSetupIntent
    intent: Start payment method setup for a patient
    question: How do I get a session key or client secret to collect a patient's card securely?
  - id: PaymentMethod.DeletePaymentMethod
    intent: Remove a patient's payment method
    question: Is there a way to remove an old card from a patient's account?
  - id: PaymentMethod.ShowPaymentMethod
    intent: Get one patient payment method
    question: Can I look up a single saved payment method for a patient?
  phrasing_ops: 5
  slug: hint-health-payment-method-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Product Category API from Hint Health — 3 operation(s) for product category.
  name: Hint Health Product Category API
  phrasing_intents:
  - id: ProductCategory.ListAvailableProductCategories
    intent: List all marketplace categories
    question: Which marketplace categories are available to tag my product with?
  - id: ProductCategory.ListProductCategories
    intent: List categories on one product
    question: Which categories is my product currently listed under?
  - id: ProductCategory.AttachProductCategory
    intent: Attach a category to a product
    question: How do I add my product to an existing marketplace category?
  - id: ProductCategory.DetachProductCategory
    intent: Detach a category from a product
    question: How do I take my product out of a category?
  phrasing_ops: 4
  slug: hint-health-product-category-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Webhook Endpoint API from Hint Health — 4 operation(s) for webhook endpoint.
  name: Hint Health Webhook Endpoint API
  phrasing_intents:
  - id: WebhookEndpoint.CreateWebhookEndpointLegacy
    intent: Add a webhook endpoint to an integration (legacy)
    question: Can I register a webhook URL on one specific integration through the legacy endpoint?
  - id: WebhookEndpoint.WebhookEndpointsLegacy
    intent: List an integration's webhook endpoints (legacy)
    question: Which webhook URLs are registered on one of my integrations under the older integration endpoints?
  - id: WebhookEndpoint.DeleteWebhookEndpointLegacy
    intent: Remove an integration webhook endpoint (legacy)
    question: What happens to pending and retrying webhooks when I delete an integration's endpoint?
  - id: WebhookEndpoint.ShowWebhookEndpointLegacy
    intent: Get one integration webhook endpoint (legacy)
    question: What are the details of one webhook endpoint that belongs to an integration?
  - id: WebhookEndpoint.UpdateWebhookEndpointLegacy
    intent: Change an integration webhook URL (legacy)
    question: Is it possible to point an existing integration webhook endpoint at a new URL?
  - id: WebhookEndpoint.ListWebhookEndpoints
    intent: List partner webhook endpoints
    question: Which webhook endpoints are set up on my partner account?
  - id: WebhookEndpoint.UpdateWebhookEndpoint
    intent: Change a partner webhook endpoint URL
    question: How do I change where a partner webhook endpoint delivers?
  - id: WebhookEndpoint.DeleteWebhookEndpoint
    intent: Delete a partner webhook endpoint
    question: Can I remove a webhook endpoint from my partner account?
  phrasing_ops: 8
  slug: hint-health-webhook-endpoint-api
- baseURL: https://api.hint.com
  baseurl_source: declared
  description: The Webhook Event API from Hint Health — 1 operation(s) for webhook event.
  name: Hint Health Webhook Event API
  phrasing_intents:
  - id: WebhookEvent.ListWebhookEvents
    intent: List webhook event types
    question: Which webhook event types can my partner endpoint receive?
  phrasing_ops: 1
  slug: hint-health-webhook-event-api
artifact_total: 642
asyncapis:
- description: ''
  name: Hint Health Webhooks
  slug: hint-health-webhooks
collections:
- collection_type: open
  name: Hint Health AccountAccessToken API
  slug: open-hint-health-accountaccesstoken-api
- collection_type: open
  name: Hint Health AccountAccessToken Affiliate API
  slug: open-hint-health-affiliate-api
- collection_type: open
  name: Hint Health AccountAccessToken AffiliateBill API
  slug: open-hint-health-affiliatebill-api
- collection_type: open
  name: Hint Health AccountAccessToken AffiliatePatient API
  slug: open-hint-health-affiliatepatient-api
- collection_type: open
  name: Hint Health AccountAccessToken CancellationReason API
  slug: open-hint-health-cancellationreason-api
- collection_type: open
  name: Hint Health AccountAccessToken Charge API
  slug: open-hint-health-charge-api
- collection_type: open
  name: Hint Health AccountAccessToken ChargeItem API
  slug: open-hint-health-chargeitem-api
- collection_type: open
  name: Hint Health AccountAccessToken ClinicalNoteInteraction API
  slug: open-hint-health-clinicalnoteinteraction-api
- collection_type: open
  name: Hint Health AccountAccessToken Company API
  slug: open-hint-health-company-api
- collection_type: open
  name: Hint Health AccountAccessToken CompanyPlan API
  slug: open-hint-health-companyplan-api
- collection_type: open
  name: Hint Health AccountAccessToken Coupon API
  slug: open-hint-health-coupon-api
- collection_type: open
  name: Hint Health AccountAccessToken Credit API
  slug: open-hint-health-credit-api
- collection_type: open
  name: Hint Health AccountAccessToken CreditCategory API
  slug: open-hint-health-creditcategory-api
- collection_type: open
  name: Hint Health AccountAccessToken CreditLine API
  slug: open-hint-health-creditline-api
- collection_type: open
  name: Hint Health AccountAccessToken CustomerInvoice API
  slug: open-hint-health-customerinvoice-api
- collection_type: open
  name: Hint Health AccountAccessToken CustomerInvoiceCharge API
  slug: open-hint-health-customerinvoicecharge-api
- collection_type: open
  name: Hint Health AccountAccessToken CustomerInvoicePayment API
  slug: open-hint-health-customerinvoicepayment-api
- collection_type: open
  name: Hint Health AccountAccessToken DocumentInteraction API
  slug: open-hint-health-documentinteraction-api
- collection_type: open
  name: Hint Health AccountAccessToken EmployeeDivision API
  slug: open-hint-health-employeedivision-api
- collection_type: open
  name: Hint Health AccountAccessToken FormResponse API
  slug: open-hint-health-formresponse-api
- collection_type: open
  name: Hint Health AccountAccessToken GlobalWebhookEndpoint API
  slug: open-hint-health-globalwebhookendpoint-api
- collection_type: open
  name: Hint Health AccountAccessToken Integration API
  slug: open-hint-health-integration-api
- collection_type: open
  name: Hint Health AccountAccessToken IntegrationRecord API
  slug: open-hint-health-integrationrecord-api
- collection_type: open
  name: Hint Health AccountAccessToken Interaction API
  slug: open-hint-health-interaction-api
- collection_type: open
  name: Hint Health AccountAccessToken InteractionNotifications API
  slug: open-hint-health-interactionnotifications-api
- collection_type: open
  name: Hint Health AccountAccessToken Invoice API
  slug: open-hint-health-invoice-api
- collection_type: open
  name: Hint Health AccountAccessToken InvoicePayment API
  slug: open-hint-health-invoicepayment-api
- collection_type: open
  name: Hint Health AccountAccessToken LabInteraction API
  slug: open-hint-health-labinteraction-api
- collection_type: open
  name: Hint Health AccountAccessToken LeadSource API
  slug: open-hint-health-leadsource-api
- collection_type: open
  name: Hint Health AccountAccessToken Location API
  slug: open-hint-health-location-api
- collection_type: open
  name: Hint Health AccountAccessToken Membership API
  slug: open-hint-health-membership-api
- collection_type: open
  name: Hint Health AccountAccessToken MembershipContract API
  slug: open-hint-health-membershipcontract-api
- collection_type: open
  name: Hint Health AccountAccessToken MembershipMember API
  slug: open-hint-health-membershipmember-api
- collection_type: open
  name: Hint Health AccountAccessToken OAuth API
  slug: open-hint-health-oauth-api
- collection_type: open
  name: Hint Health AccountAccessToken Partner API
  slug: open-hint-health-partner-api
- collection_type: open
  name: Hint Health AccountAccessToken PartnerCharge API
  slug: open-hint-health-partnercharge-api
- collection_type: open
  name: Hint Health AccountAccessToken PartnerInteraction API
  slug: open-hint-health-partnerinteraction-api
- collection_type: open
  name: Hint Health AccountAccessToken Patient API
  slug: open-hint-health-patient-api
- collection_type: open
  name: Hint Health AccountAccessToken PaymentMethod API
  slug: open-hint-health-paymentmethod-api
- collection_type: open
  name: Hint Health AccountAccessToken Plan API
  slug: open-hint-health-plan-api
- collection_type: open
  name: Hint Health AccountAccessToken Practice API
  slug: open-hint-health-practice-api
- collection_type: open
  name: Hint Health AccountAccessToken Practitioner API
  slug: open-hint-health-practitioner-api
- collection_type: open
  name: Hint Health AccountAccessToken Quote API
  slug: open-hint-health-quote-api
- collection_type: open
  name: Hint Health AccountAccessToken SignupAttempt API
  slug: open-hint-health-signupattempt-api
- collection_type: open
  name: Hint Health AccountAccessToken SocialSecurityNumber API
  slug: open-hint-health-socialsecuritynumber-api
- collection_type: open
  name: Hint Health AccountAccessToken Sponsorship API
  slug: open-hint-health-sponsorship-api
- collection_type: open
  name: Hint Health AccountAccessToken Supplements API
  slug: open-hint-health-supplements-api
- collection_type: open
  name: Hint Health AccountAccessToken User API
  slug: open-hint-health-user-api
- collection_type: open
  name: Hint Health AccountAccessToken WebhookEndpoint API
  slug: open-hint-health-webhookendpoint-api
common:
- group: design
  href: https://artifacts.apis.io/hint-health/rules/hint-health-rules.yml
  title: ''
  type: Spectral
  url: rules/hint-health-rules.yml
- group: design
  href: https://artifacts.apis.io/hint-health/rules/hint-health-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/hint-health-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/hint-health/json-ld/hint-health-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hint-health-context.jsonld
- group: design
  href: https://artifacts.apis.io/hint-health/vocabulary/hint-health-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hint-health-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://www.hint.com/security
- group: operate
  href: https://artifacts.apis.io/hint-health/lifecycle/hint-health-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/hint-health-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/hint-health/hosts/hint-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hint-health-hosts.yml
- group: other
  href: https://artifacts.apis.io/hint-health/vendors/hint-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hint-health-vendors.yml
- group: auth
  href: https://artifacts.apis.io/hint-health/security/hint-health-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hint-health-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/hint-health/overlays/hint-health-cancellationreason-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hint-health-cancellationreason-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/hint-health/overlays/hint-health-creditline-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hint-health-creditline-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/hint-health/overlays/hint-health-formresponse-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hint-health-formresponse-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/hint-health/overlays/hint-health-leadsource-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hint-health-leadsource-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/hint-health/overlays/hint-health-oauth-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hint-health-oauth-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/hint-health/overlays/hint-health-paymentmethod-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hint-health-paymentmethod-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/hint-health/overlays/hint-health-webhookendpoint-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hint-health-webhookendpoint-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/hint-health/capabilities/hint-health-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/hint-health-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/hint-health/agentic-access/hint-health-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hint-health-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/hint-health/security/hint-health-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hint-health-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/hint-health/security/hint-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hint-health-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/hint-health/authentication/hint-health-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hint-health-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.hint.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.hint.com/docs/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hinthealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hint-health
- group: company
  title: ''
  type: Blog
  url: https://blog.hint.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hint.com/core/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hint.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/HintHealth
- group: commercial
  href: https://artifacts.apis.io/hint-health/plans/hint-health-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hint-health-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/hint-health/rate-limits/hint-health-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hint-health-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/hint-health/finops/hint-health-finops.yml
  title: ''
  type: FinOps
  url: finops/hint-health-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.hint.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.hint.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.hint.com/docs/requesting-a-sandbox-and-api-access
- group: operate
  title: ''
  type: Support
  url: https://www.hint.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.hint.com/get-started
- group: start
  title: ''
  type: Login
  url: https://accounts.hint.com/oauth/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hint.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hint.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.hint.com/security
- group: design
  href: https://artifacts.apis.io/hint-health/conformance/hint-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hint-health-conformance.yml
- group: design
  href: https://artifacts.apis.io/hint-health/conventions/hint-health-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hint-health-conventions.yml
- group: design
  href: https://artifacts.apis.io/hint-health/conventions/hint-health-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/hint-health-conventions.yml
- group: design
  href: https://artifacts.apis.io/hint-health/errors/hint-health-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hint-health-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hint-health/lifecycle/hint-health-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hint-health-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/hint-health/packages/hint-health-packages.yml
  title: ''
  type: Packages
  url: packages/hint-health-packages.yml
- group: build
  href: https://artifacts.apis.io/hint-health/packages/hint-health-packages.yml
  title: ''
  type: SDKs
  url: packages/hint-health-packages.yml
- group: start
  href: https://artifacts.apis.io/hint-health/sandbox/hint-health-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/hint-health-sandbox.yml
- group: design
  href: https://artifacts.apis.io/hint-health/components/hint-health-components.yml
  title: ''
  type: Components
  url: components/hint-health-components.yml
- group: design
  href: https://artifacts.apis.io/hint-health/data-model/hint-health-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hint-health-data-model.yml
- group: design
  href: https://artifacts.apis.io/hint-health/asyncapi/hint-health-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/hint-health-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/hint-health/mcp/hint-health-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hint-health-mcp.yml
- group: build
  href: https://artifacts.apis.io/hint-health/mcp/hint-health-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/hint-health-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/hint-health/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/hint-health/llms/hint-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hint-health-llms.txt
created: '2026-06-13'
description: Hint Health is the leading direct primary care (DPC) technology platform, powering thousands of DPC practices with software for membership management, automated billing, clinical workflows, and provider networks. The Hint REST API provides programmatic access to clinic operations including patient enrollment, membership billing, practice configuration, clinical data management, charges, invoices, webhooks, and OAuth-based partner integrations.
examples:
- key_count: 6
  name: Accountaccesstoken Createacccesstoken Response 200
  slug: accountaccesstoken-createacccesstoken-response-200
- key_count: 6
  name: Affiliate Listaffiliates Response 200
  slug: affiliate-listaffiliates-response-200
- key_count: 6
  name: Affiliate Showpatientaffiliate Response 200
  slug: affiliate-showpatientaffiliate-response-200
- key_count: 6
  name: Affiliatebill Listaffiliatebills Response 200
  slug: affiliatebill-listaffiliatebills-response-200
- key_count: 6
  name: Cancellationreason Listcancellationreasons Response 200
  slug: cancellationreason-listcancellationreasons-response-200
- key_count: 6
  name: Charge Createcharge Response 201
  slug: charge-createcharge-response-201
- key_count: 6
  name: Chargeitem Createchargeitem Response 200
  slug: chargeitem-createchargeitem-response-200
- key_count: 6
  name: Chargeitem Listallchargeitems Response 200
  slug: chargeitem-listallchargeitems-response-200
- key_count: 6
  name: Chargeitem Showchargeitem Response 200
  slug: chargeitem-showchargeitem-response-200
- key_count: 6
  name: Chargeitem Updatechargeitem Response 200
  slug: chargeitem-updatechargeitem-response-200
- key_count: 6
  name: Clinicalnoteinteraction Createclinicalnoteinteraction Response 200
  slug: clinicalnoteinteraction-createclinicalnoteinteraction-response-200
- key_count: 6
  name: Clinicalnoteinteraction Showclinicalnoteinteraction Response 200
  slug: clinicalnoteinteraction-showclinicalnoteinteraction-response-200
- key_count: 6
  name: Clinicalnoteinteraction Updateclinicalnoteinteraction Response 200
  slug: clinicalnoteinteraction-updateclinicalnoteinteraction-response-200
- key_count: 6
  name: Company Createcompany Response 200
  slug: company-createcompany-response-200
- key_count: 6
  name: Company Deactivatecompany Response 200
  slug: company-deactivatecompany-response-200
- key_count: 6
  name: Company Listallcompanies Response 200
  slug: company-listallcompanies-response-200
- key_count: 6
  name: Company Showcompany Response 200
  slug: company-showcompany-response-200
- key_count: 6
  name: Company Updatecompany Response 200
  slug: company-updatecompany-response-200
- key_count: 6
  name: Companyplan Createcompanyplan Response 200
  slug: companyplan-createcompanyplan-response-200
- key_count: 6
  name: Companyplan Destroycompanyplan Response 200
  slug: companyplan-destroycompanyplan-response-200
- key_count: 6
  name: Companyplan Listcompanyplans Response 200
  slug: companyplan-listcompanyplans-response-200
- key_count: 6
  name: Companyplan Updatecompanyplan Response 200
  slug: companyplan-updatecompanyplan-response-200
- key_count: 6
  name: Coupon Listallcoupons Response 200
  slug: coupon-listallcoupons-response-200
- key_count: 6
  name: Coupon Showcoupon Response 200
  slug: coupon-showcoupon-response-200
- key_count: 6
  name: Credit Createcredit Response 201
  slug: credit-createcredit-response-201
- key_count: 6
  name: Credit Listallcredits Response 200
  slug: credit-listallcredits-response-200
- key_count: 6
  name: Credit Updatecredit Response 200
  slug: credit-updatecredit-response-200
- key_count: 6
  name: Creditcategory Createcreditcategory Response 200
  slug: creditcategory-createcreditcategory-response-200
- key_count: 6
  name: Creditcategory Listcreditcategories Response 200
  slug: creditcategory-listcreditcategories-response-200
- key_count: 6
  name: Creditcategory Showcreditcategory Response 200
  slug: creditcategory-showcreditcategory-response-200
- key_count: 6
  name: Creditcategory Updatecreditcategory Response 200
  slug: creditcategory-updatecreditcategory-response-200
- key_count: 6
  name: Creditline Listcreditlines Response 200
  slug: creditline-listcreditlines-response-200
- key_count: 6
  name: Customerinvoice Createcustomerinvoice Response 200
  slug: customerinvoice-createcustomerinvoice-response-200
- key_count: 6
  name: Customerinvoice Createpdf Response 200
  slug: customerinvoice-createpdf-response-200
- key_count: 6
  name: Customerinvoice Issuecustomerinvoice Response 200
  slug: customerinvoice-issuecustomerinvoice-response-200
- key_count: 6
  name: Customerinvoice Listallcustomerinvoices Response 200
  slug: customerinvoice-listallcustomerinvoices-response-200
- key_count: 6
  name: Customerinvoice Returntodraft Response 200
  slug: customerinvoice-returntodraft-response-200
- key_count: 6
  name: Customerinvoice Showcustomerinvoice Response 200
  slug: customerinvoice-showcustomerinvoice-response-200
- key_count: 6
  name: Customerinvoice Updatecustomerinvoice Response 200
  slug: customerinvoice-updatecustomerinvoice-response-200
- key_count: 6
  name: Customerinvoice Voidcustomerinvoice Response 200
  slug: customerinvoice-voidcustomerinvoice-response-200
- key_count: 6
  name: Customerinvoicecharge Createcustomerinvoicecharge Response 201
  slug: customerinvoicecharge-createcustomerinvoicecharge-response-201
- key_count: 6
  name: Customerinvoicecharge Updatecustomerinvoicecharge Response 200
  slug: customerinvoicecharge-updatecustomerinvoicecharge-response-200
- key_count: 6
  name: Customerinvoicepayment Createpayment Response 200
  slug: customerinvoicepayment-createpayment-response-200
- key_count: 6
  name: Customerinvoicepayment Listallpayments Response 200
  slug: customerinvoicepayment-listallpayments-response-200
- key_count: 6
  name: Customerinvoicepayment Showpayment Response 200
  slug: customerinvoicepayment-showpayment-response-200
- key_count: 6
  name: Documentinteraction Createdocumentinteraction Response 200
  slug: documentinteraction-createdocumentinteraction-response-200
- key_count: 6
  name: Documentinteraction Showdocumentinteraction Response 200
  slug: documentinteraction-showdocumentinteraction-response-200
- key_count: 6
  name: Documentinteraction Updatedocumentinteraction Response 200
  slug: documentinteraction-updatedocumentinteraction-response-200
- key_count: 6
  name: Employeedivision Listallemployeedivisions Response 200
  slug: employeedivision-listallemployeedivisions-response-200
- key_count: 6
  name: Formresponse Listallformresponses Response 200
  slug: formresponse-listallformresponses-response-200
- key_count: 6
  name: Formresponse Showformresponse Response 200
  slug: formresponse-showformresponse-response-200
- key_count: 6
  name: Globalwebhookendpoint Createwebhookendpointlegacy Response 200
  slug: globalwebhookendpoint-createwebhookendpointlegacy-response-200
- key_count: 6
  name: Globalwebhookendpoint Showwebhookendpointlegacy Response 200
  slug: globalwebhookendpoint-showwebhookendpointlegacy-response-200
- key_count: 6
  name: Globalwebhookendpoint Updatewebhookendpointlegacy Response 200
  slug: globalwebhookendpoint-updatewebhookendpointlegacy-response-200
- key_count: 6
  name: Globalwebhookendpoint Webhookendpointslegacy Response 200
  slug: globalwebhookendpoint-webhookendpointslegacy-response-200
- key_count: 6
  name: Integration Activateintegration Response 200
  slug: integration-activateintegration-response-200
- key_count: 6
  name: Integration Deactivateintegration Response 200
  slug: integration-deactivateintegration-response-200
- key_count: 6
  name: Integration Listallintegrations Response 200
  slug: integration-listallintegrations-response-200
- key_count: 6
  name: Integration Showintegration Response 200
  slug: integration-showintegration-response-200
- key_count: 6
  name: Integration Updateintegration Response 200
  slug: integration-updateintegration-response-200
- key_count: 6
  name: Integrationrecord Listallintegrationrecords Response 200
  slug: integrationrecord-listallintegrationrecords-response-200
- key_count: 6
  name: Interaction Listallinteractions Response 200
  slug: interaction-listallinteractions-response-200
- key_count: 6
  name: Interactionnotifications Createinteractionnotification Response 200
  slug: interactionnotifications-createinteractionnotification-response-200
- key_count: 6
  name: Invoice Listallinvoices Response 200
  slug: invoice-listallinvoices-response-200
- key_count: 6
  name: Invoice Showinvoice Response 200
  slug: invoice-showinvoice-response-200
- key_count: 6
  name: Invoicepayment Createpayment Response 200
  slug: invoicepayment-createpayment-response-200
- key_count: 6
  name: Invoicepayment Listallpayments Response 200
  slug: invoicepayment-listallpayments-response-200
- key_count: 6
  name: Invoicepayment Showpayment Response 200
  slug: invoicepayment-showpayment-response-200
- key_count: 6
  name: Labinteraction Createlabinteraction Response 200
  slug: labinteraction-createlabinteraction-response-200
- key_count: 6
  name: Labinteraction Showlabinteraction Response 200
  slug: labinteraction-showlabinteraction-response-200
- key_count: 6
  name: Labinteraction Updatelabinteraction Response 200
  slug: labinteraction-updatelabinteraction-response-200
- key_count: 6
  name: Leadsource Leadsource Response 200
  slug: leadsource-leadsource-response-200
- key_count: 6
  name: Leadsource Leadsources Response 200
  slug: leadsource-leadsources-response-200
- key_count: 6
  name: Leadsource Updateleadsource Response 200
  slug: leadsource-updateleadsource-response-200
- key_count: 6
  name: Location Createlocation Response 200
  slug: location-createlocation-response-200
- key_count: 6
  name: Location Listlocations Response 200
  slug: location-listlocations-response-200
- key_count: 6
  name: Location Showlocation Response 200
  slug: location-showlocation-response-200
- key_count: 6
  name: Location Updatelocation Response 200
  slug: location-updatelocation-response-200
- key_count: 6
  name: Membership Billmembership Response 200
  slug: membership-billmembership-response-200
- key_count: 6
  name: Membership Cancelmembership Response 200
  slug: membership-cancelmembership-response-200
- key_count: 6
  name: Membership Confirmmembership Response 200
  slug: membership-confirmmembership-response-200
- key_count: 6
  name: Membership Createmembership Response 200
  slug: membership-createmembership-response-200
- key_count: 6
  name: Membership Listallmemberships Response 200
  slug: membership-listallmemberships-response-200
- key_count: 6
  name: Membership Newmembership Response 200
  slug: membership-newmembership-response-200
- key_count: 6
  name: Membership Showmembership Response 200
  slug: membership-showmembership-response-200
- key_count: 6
  name: Membership Updatemembership Response 200
  slug: membership-updatemembership-response-200
- key_count: 6
  name: Membershipcontract Listallmembershipcontracts Response 200
  slug: membershipcontract-listallmembershipcontracts-response-200
- key_count: 6
  name: Membershipcontract Renewmembershipcontract Response 200
  slug: membershipcontract-renewmembershipcontract-response-200
- key_count: 6
  name: Membershipcontract Updatemembershipcontract Response 200
  slug: membershipcontract-updatemembershipcontract-response-200
- key_count: 6
  name: Membershipmember Cancelmembershipmember Response 200
  slug: membershipmember-cancelmembershipmember-response-200
- key_count: 6
  name: Membershipmember Createmembershipmember Response 200
  slug: membershipmember-createmembershipmember-response-200
- key_count: 6
  name: Membershipmember Destroymembershipmember Response 200
  slug: membershipmember-destroymembershipmember-response-200
- key_count: 6
  name: Membershipmember Listmembershipmembers Response 200
  slug: membershipmember-listmembershipmembers-response-200
- key_count: 6
  name: Membershipmember Showmembershipmember Response 200
  slug: membershipmember-showmembershipmember-response-200
- key_count: 6
  name: Membershipmember Updatemembershipmember Response 200
  slug: membershipmember-updatemembershipmember-response-200
- key_count: 6
  name: Oauth Oauthtokens Response 200
  slug: oauth-oauthtokens-response-200
- key_count: 6
  name: Partner Showpartnerlegacy Response 200
  slug: partner-showpartnerlegacy-response-200
- key_count: 6
  name: Partner Updatepartnerlegacy Response 200
  slug: partner-updatepartnerlegacy-response-200
- key_count: 6
  name: Partnercharge Createpartnercharge Response 200
  slug: partnercharge-createpartnercharge-response-200
- key_count: 6
  name: Partnercharge Showpartnercharge Response 200
  slug: partnercharge-showpartnercharge-response-200
- key_count: 6
  name: Partnerinteraction Createpartnerinteraction Response 200
  slug: partnerinteraction-createpartnerinteraction-response-200
- key_count: 6
  name: Partnerinteraction Showpartnerinteraction Response 200
  slug: partnerinteraction-showpartnerinteraction-response-200
- key_count: 6
  name: Partnerinteraction Updatepartnerinteraction Response 200
  slug: partnerinteraction-updatepartnerinteraction-response-200
- key_count: 6
  name: Patient Createpatient Response 200
  slug: patient-createpatient-response-200
- key_count: 6
  name: Patient Listallpatients Response 200
  slug: patient-listallpatients-response-200
- key_count: 6
  name: Patient Matchpatients Response 200
  slug: patient-matchpatients-response-200
- key_count: 6
  name: Patient Showpatient Response 200
  slug: patient-showpatient-response-200
- key_count: 6
  name: Patient Updatepatient Response 200
  slug: patient-updatepatient-response-200
- key_count: 6
  name: Paymentmethod Createpaymentmethod Response 201
  slug: paymentmethod-createpaymentmethod-response-201
- key_count: 6
  name: Paymentmethod Createsetupintent Response 201
  slug: paymentmethod-createsetupintent-response-201
- key_count: 6
  name: Paymentmethod Listallpaymentmethods Response 200
  slug: paymentmethod-listallpaymentmethods-response-200
- key_count: 6
  name: Paymentmethod Showpaymentmethod Response 200
  slug: paymentmethod-showpaymentmethod-response-200
- key_count: 6
  name: Plan Listallplans Response 200
  slug: plan-listallplans-response-200
- key_count: 6
  name: Practice Getpractice Response 200
  slug: practice-getpractice-response-200
- key_count: 6
  name: Practice Updatepractice Response 200
  slug: practice-updatepractice-response-200
- key_count: 6
  name: Practitioner Createpractitioner Response 200
  slug: practitioner-createpractitioner-response-200
- key_count: 6
  name: Practitioner Providerpractitioners Response 200
  slug: practitioner-providerpractitioners-response-200
- key_count: 6
  name: Practitioner Showpractitioner Response 200
  slug: practitioner-showpractitioner-response-200
- key_count: 6
  name: Practitioner Updatepractitioner Response 200
  slug: practitioner-updatepractitioner-response-200
- key_count: 6
  name: Quote Createquote Response 200
  slug: quote-createquote-response-200
- key_count: 6
  name: Signupattempt Listsignupattempts Response 200
  slug: signupattempt-listsignupattempts-response-200
- key_count: 6
  name: Signupattempt Showsignupattempt Response 200
  slug: signupattempt-showsignupattempt-response-200
- key_count: 6
  name: Socialsecuritynumber Showsocialsecuritynumber Response 200
  slug: socialsecuritynumber-showsocialsecuritynumber-response-200
- key_count: 6
  name: Sponsorship Createsponsorship Response 200
  slug: sponsorship-createsponsorship-response-200
- key_count: 6
  name: Sponsorship Destroysponsorship Response 200
  slug: sponsorship-destroysponsorship-response-200
- key_count: 6
  name: Sponsorship Listsponsorships Response 200
  slug: sponsorship-listsponsorships-response-200
- key_count: 6
  name: Sponsorship Showsponsorhip Response 200
  slug: sponsorship-showsponsorhip-response-200
- key_count: 6
  name: Sponsorship Updatesponsorship Response 200
  slug: sponsorship-updatesponsorship-response-200
- key_count: 6
  name: Supplements Createsupplement Response 200
  slug: supplements-createsupplement-response-200
- key_count: 6
  name: Supplements Listallpatientsupplements Response 200
  slug: supplements-listallpatientsupplements-response-200
- key_count: 6
  name: Supplements Showsupplement Response 200
  slug: supplements-showsupplement-response-200
- key_count: 6
  name: Supplements Updatesupplement Response 200
  slug: supplements-updatesupplement-response-200
- key_count: 6
  name: User Listusers Response 200
  slug: user-listusers-response-200
- key_count: 6
  name: Webhookendpoint Createwebhookendpointlegacy Response 200
  slug: webhookendpoint-createwebhookendpointlegacy-response-200
- key_count: 6
  name: Webhookendpoint Showwebhookendpointlegacy Response 200
  slug: webhookendpoint-showwebhookendpointlegacy-response-200
- key_count: 6
  name: Webhookendpoint Updatewebhookendpointlegacy Response 200
  slug: webhookendpoint-updatewebhookendpointlegacy-response-200
- key_count: 6
  name: Webhookendpoint Webhookendpointslegacy Response 200
  slug: webhookendpoint-webhookendpointslegacy-response-200
finops:
- has_sources: true
  method: derived
  name: Hint Health Finops
  primary_unit: practice
  service_category: ''
  slug: hint-health-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hint-health.png
json_schemas:
- name: Address
  property_count: 6
  slug: address
- name: Association
  property_count: 1
  slug: association
- name: Category
  property_count: 2
  slug: category
- name: ChargeItem
  property_count: 6
  slug: chargeitem
- name: Common.EmergencyContactBlueprint_shared
  property_count: 7
  slug: common-emergencycontactblueprint_shared
- name: Common.PhoneBlueprint_shared
  property_count: 3
  slug: common-phoneblueprint_shared
- name: Common.RecordBlueprint_min
  property_count: 1
  slug: common-recordblueprint_min
- name: Common.SocialSecurityNumberBlueprint_masked
  property_count: 1
  slug: common-socialsecuritynumberblueprint_masked
- name: CompanyCreateSanitizer
  property_count: 4
  slug: companycreatesanitizer
- name: CompanyUpdateSanitizer
  property_count: 3
  slug: companyupdatesanitizer
- name: EmergencyContact
  property_count: 5
  slug: emergencycontact
- name: AppSanitizer
  property_count: 7
  slug: hint-health-app-sanitizer
- name: CompanyCreateSanitizer
  property_count: 4
  slug: hint-health-company-create-sanitizer
- name: CompanyUpdateSanitizer
  property_count: 3
  slug: hint-health-company-update-sanitizer
- name: Interaction.ClinicalNoteSanitizer
  property_count: 10
  slug: hint-health-interaction-clinical-note-sanitizer
- name: Interaction.LabSanitizer
  property_count: 9
  slug: hint-health-interaction-lab-sanitizer
- name: MembershipCreateSanitizer
  property_count: 9
  slug: hint-health-membership-create-sanitizer
- name: MembershipPatientSanitizer
  property_count: 4
  slug: hint-health-membership-patient-sanitizer
- name: MembershipUpdateSanitizer
  property_count: 8
  slug: hint-health-membership-update-sanitizer
- name: Create_ApiKey
  property_count: 1
  slug: hint-health-partner-api-keys-controller-create-body
- name: Update_Backend
  property_count: 13
  slug: hint-health-partner-backends-controller-update-body
- name: Create_InstallationApiKey
  property_count: 1
  slug: hint-health-partner-installations-api-keys-controller-create-body
- name: Partner.Installations.ApiKeysController.update_body
  property_count: 1
  slug: hint-health-partner-installations-api-keys-controller-update-body
- name: Create_InstallationWebhookEndpoint
  property_count: 1
  slug: hint-health-partner-installations-webhook-endpoints-controller-create-body
- name: Partner.Installations.WebhookEndpointsController.update_body
  property_count: 1
  slug: hint-health-partner-installations-webhook-endpoints-controller-update-body
- name: Create_AppSurface
  property_count: 12
  slug: hint-health-partner-partner-product-apps-surfaces-controller-create-body
- name: Update_AppSurface
  property_count: 11
  slug: hint-health-partner-partner-product-apps-surfaces-controller-update-body
- name: Update_Partner
  property_count: 2
  slug: hint-health-partner-partners-controller-update-body
- name: Update_WebhookEndpoint
  property_count: 1
  slug: hint-health-partner-webhook-endpoints-controller-update-body
- name: Platform.IntegrationBlueprint_all
  property_count: 0
  slug: hint-health-platform-integration-blueprint-all
- name: Platform.IntegrationBlueprint_one
  property_count: 8
  slug: hint-health-platform-integration-blueprint-one
- name: Platform.IntegrationBlueprint_one_with_access_token
  property_count: 12
  slug: hint-health-platform-integration-blueprint-one-with-access-token
- name: Update_Integration
  property_count: 1
  slug: hint-health-platform-integrations-controller-update-body
- name: OAuth
  property_count: 3
  slug: hint-health-platform-oauths-controller-tokens-body
- name: Platform.PartnerBlueprint_one
  property_count: 9
  slug: hint-health-platform-partner-blueprint-one
- name: Update_Partner_Legacy
  property_count: 7
  slug: hint-health-platform-partners-controller-update-body
- name: Platform.WebhookEndpointBlueprint_all
  property_count: 0
  slug: hint-health-platform-webhook-endpoint-blueprint-all
- name: Platform.WebhookEndpointBlueprint_one
  property_count: 5
  slug: hint-health-platform-webhook-endpoint-blueprint-one
- name: Platform.WebhookEndpointsController.create_body
  property_count: 1
  slug: hint-health-platform-webhook-endpoints-controller-create-body
- name: Update_WebhookEndpoint_Legacy
  property_count: 1
  slug: hint-health-platform-webhook-endpoints-controller-update-body
- name: ProductCategorySanitizer
  property_count: 2
  slug: hint-health-product-category-sanitizer
- name: ProductHighlightSanitizer
  property_count: 4
  slug: hint-health-product-highlight-sanitizer
- name: ProductLinkSanitizer
  property_count: 6
  slug: hint-health-product-link-sanitizer
- name: ProductOverviewSanitizer
  property_count: 2
  slug: hint-health-product-overview-sanitizer
- name: ProductPreconditionSanitizer
  property_count: 2
  slug: hint-health-product-precondition-sanitizer
- name: ProductSanitizer
  property_count: 7
  slug: hint-health-product-sanitizer
- name: ProductTestimonialSanitizer
  property_count: 5
  slug: hint-health-product-testimonial-sanitizer
- name: Provider.Affiliates.PatientsController.create_body
  property_count: 1
  slug: hint-health-provider-affiliates-patients-controller-create-body
- name: Create_Charge_Item
  property_count: 4
  slug: hint-health-provider-charge-items-controller-create-body
- name: Create_Charge_Item
  property_count: 4
  slug: hint-health-provider-charge-items-controller-update-body
- name: Provider.ChargesController.create_body
  property_count: 9
  slug: hint-health-provider-charges-controller-create-body
- name: Create_Company_Plan
  property_count: 2
  slug: hint-health-provider-company-plans-controller-create-body
- name: Update_Company_Plan
  property_count: 1
  slug: hint-health-provider-company-plans-controller-update-body
- name: Create_Sponsorship
  property_count: 5
  slug: hint-health-provider-company-sponsorships-controller-create-body
- name: Update_Sponsorship
  property_count: 2
  slug: hint-health-provider-company-sponsorships-controller-update-body
- name: Provider.CreditCategoriesController.create_body
  property_count: 1
  slug: hint-health-provider-credit-categories-controller-create-body
- name: Provider.CreditCategoriesController.update_body
  property_count: 1
  slug: hint-health-provider-credit-categories-controller-update-body
- name: Create_Credit
  property_count: 4
  slug: hint-health-provider-credits-controller-create-body
- name: Update_Credit
  property_count: 2
  slug: hint-health-provider-credits-controller-update-body
- name: Provider.CustomerInvoices.ChargesController.create_body
  property_count: 10
  slug: hint-health-provider-customer-invoices-charges-controller-create-body
- name: Provider.CustomerInvoices.ChargesController.update_body
  property_count: 10
  slug: hint-health-provider-customer-invoices-charges-controller-update-body
- name: Create_Customer_Invoice
  property_count: 3
  slug: hint-health-provider-customer-invoices-controller-create-body
- name: Create_Customer_Invoice
  property_count: 3
  slug: hint-health-provider-customer-invoices-controller-update-body
- name: Create_InteractionNotification
  property_count: 1
  slug: hint-health-provider-interactions-notifications-controller-create-body
- name: Create_LeadSource
  property_count: 1
  slug: hint-health-provider-lead-sources-controller-create-body
- name: Create_LeadSource
  property_count: 1
  slug: hint-health-provider-lead-sources-controller-update-body
- name: Provider.MembersController.cancel_body
  property_count: 3
  slug: hint-health-provider-members-controller-cancel-body
- name: Provider.MembershipContractsController.renew_body
  property_count: 1
  slug: hint-health-provider-membership-contracts-controller-renew-body
- name: Provider.MembershipContractsController.update_body
  property_count: 2
  slug: hint-health-provider-membership-contracts-controller-update-body
- name: Provider.MembershipsController.bill_body
  property_count: 1
  slug: hint-health-provider-memberships-controller-bill-body
- name: Provider.MembershipsController.cancel_body
  property_count: 3
  slug: hint-health-provider-memberships-controller-cancel-body
- name: Create_PartnerCharge
  property_count: 6
  slug: hint-health-provider-partner-charges-controller-create-body
- name: Create_Patient
  property_count: 43
  slug: hint-health-provider-patients-controller-create-body
- name: Match_Patients
  property_count: 6
  slug: hint-health-provider-patients-controller-matching-body
- name: Create_Patient
  property_count: 42
  slug: hint-health-provider-patients-controller-update-body
- name: Create_DocumentInteraction
  property_count: 7
  slug: hint-health-provider-patients-interactions-document-controller-create-body
- name: Update_DocumentInteraction
  property_count: 7
  slug: hint-health-provider-patients-interactions-document-controller-update-body
- name: Create_PartnerInteraction
  property_count: 5
  slug: hint-health-provider-patients-interactions-partner-controller-create-body
- name: Update_PartnerInteraction
  property_count: 5
  slug: hint-health-provider-patients-interactions-partner-controller-update-body
- name: Provider.Patients.PaymentMethodsController.create_body
  property_count: 2
  slug: hint-health-provider-patients-payment-methods-controller-create-body
- name: Provider.Patients.PaymentMethods.SetupController.create_body
  property_count: 2
  slug: hint-health-provider-patients-payment-methods-setup-controller-create-body
- name: Create_Supplement
  property_count: 8
  slug: hint-health-provider-patients-supplements-controller-create-body
- name: Update_Supplement
  property_count: 8
  slug: hint-health-provider-patients-supplements-controller-update-body
- name: Create Payment
  property_count: 6
  slug: hint-health-provider-payments-controller-create-body
- name: Update_Practice
  property_count: 12
  slug: hint-health-provider-practices-controller-update-body
- name: Create_Practitioner
  property_count: 10
  slug: hint-health-provider-practitioners-controller-create-body
- name: Create_Practitioner
  property_count: 10
  slug: hint-health-provider-practitioners-controller-update-body
- name: Public.AffiliateAncillaryChargeBlueprint_all
  property_count: 0
  slug: hint-health-public-affiliate-ancillary-charge-blueprint-all
- name: Public.AffiliateBillBlueprint_all
  property_count: 0
  slug: hint-health-public-affiliate-bill-blueprint-all
- name: Public.AffiliationBlueprint_affiliate_min
  property_count: 2
  slug: hint-health-public-affiliation-blueprint-affiliate-min
- name: Public.AffiliationBlueprint_all
  property_count: 0
  slug: hint-health-public-affiliation-blueprint-all
- name: Public.ApiKeyBlueprint_all
  property_count: 0
  slug: hint-health-public-api-key-blueprint-all
- name: Public.ApiKeyBlueprint_one
  property_count: 6
  slug: hint-health-public-api-key-blueprint-one
- name: Public.AppBlueprint_one
  property_count: 11
  slug: hint-health-public-app-blueprint-one
- name: Public.AppSurfaceBlueprint_one
  property_count: 13
  slug: hint-health-public-app-surface-blueprint-one
- name: Public.AppointmentBlueprint_all
  property_count: 0
  slug: hint-health-public-appointment-blueprint-all
- name: Public.AppointmentTypeBlueprint_all
  property_count: 0
  slug: hint-health-public-appointment-type-blueprint-all
- name: Public.BackendBlueprint_all
  property_count: 0
  slug: hint-health-public-backend-blueprint-all
- name: Public.BackendBlueprint_one
  property_count: 17
  slug: hint-health-public-backend-blueprint-one
- name: Public.CancellationReasonBlueprint_all
  property_count: 0
  slug: hint-health-public-cancellation-reason-blueprint-all
- name: Public.ChargeBlueprint_one_with_invoice
  property_count: 20
  slug: hint-health-public-charge-blueprint-one-with-invoice
- name: Public.ChargeItemBlueprint_all
  property_count: 0
  slug: hint-health-public-charge-item-blueprint-all
- name: Public.ChargeItemBlueprint_one
  property_count: 10
  slug: hint-health-public-charge-item-blueprint-one
- name: Public.CompanyBlueprint_all
  property_count: 0
  slug: hint-health-public-company-blueprint-all
- name: Public.CompanyBlueprint_one
  property_count: 10
  slug: hint-health-public-company-blueprint-one
- name: Public.CompanyPlanBlueprint_all
  property_count: 0
  slug: hint-health-public-company-plan-blueprint-all
- name: Public.CompanyPlanBlueprint_one
  property_count: 4
  slug: hint-health-public-company-plan-blueprint-one
- name: Public.CouponBlueprint_all
  property_count: 0
  slug: hint-health-public-coupon-blueprint-all
- name: Public.CouponBlueprint_one
  property_count: 13
  slug: hint-health-public-coupon-blueprint-one
- name: Public.CreditBlueprint_all
  property_count: 0
  slug: hint-health-public-credit-blueprint-all
- name: Public.CreditBlueprint_one
  property_count: 8
  slug: hint-health-public-credit-blueprint-one
- name: Public.CreditCategoryBlueprint_all
  property_count: 0
  slug: hint-health-public-credit-category-blueprint-all
- name: Public.CreditCategoryBlueprint_one
  property_count: 4
  slug: hint-health-public-credit-category-blueprint-one
- name: Public.CreditLineBlueprint_all
  property_count: 0
  slug: hint-health-public-credit-line-blueprint-all
- name: Public.CustomerInvoiceBlueprint_all
  property_count: 0
  slug: hint-health-public-customer-invoice-blueprint-all
- name: Public.CustomerInvoiceBlueprint_one_2
  property_count: 25
  slug: hint-health-public-customer-invoice-blueprint-one-2
- name: Public.CustomerInvoiceBlueprint_one
  property_count: 24
  slug: hint-health-public-customer-invoice-blueprint-one
- name: Public.EmployeeDivisionBlueprint_all
  property_count: 0
  slug: hint-health-public-employee-division-blueprint-all
- name: Public.FormResponseBlueprint_all
  property_count: 0
  slug: hint-health-public-form-response-blueprint-all
- name: Public.FormResponseBlueprint_one
  property_count: 5
  slug: hint-health-public-form-response-blueprint-one
- name: Public.InstallationBlueprint_one_with_credential
  property_count: 8
  slug: hint-health-public-installation-blueprint-one-with-credential
- name: Public.InteractionBlueprint_all
  property_count: 0
  slug: hint-health-public-interaction-blueprint-all
- name: Public.InteractionBlueprint_one
  property_count: 6
  slug: hint-health-public-interaction-blueprint-one
- name: Public.Interaction.ClinicalNoteBlueprint_one
  property_count: 11
  slug: hint-health-public-interaction-clinical-note-blueprint-one
- name: Public.Interaction.FileBlueprint_download_url
  property_count: 4
  slug: hint-health-public-interaction-file-blueprint-download-url
- name: Public.Interaction.LabBlueprint_one
  property_count: 8
  slug: hint-health-public-interaction-lab-blueprint-one
- name: Public.InteractionNotificationBlueprint_one
  property_count: 2
  slug: hint-health-public-interaction-notification-blueprint-one
- name: Public.LeadSourceBlueprint_all
  property_count: 0
  slug: hint-health-public-lead-source-blueprint-all
- name: Public.LeadSourceBlueprint_one
  property_count: 4
  slug: hint-health-public-lead-source-blueprint-one
- name: Public.LocationBlueprint_all
  property_count: 0
  slug: hint-health-public-location-blueprint-all
- name: Public.LocationBlueprint_one
  property_count: 14
  slug: hint-health-public-location-blueprint-one
- name: Public.MembershipBlueprint_all
  property_count: 0
  slug: hint-health-public-membership-blueprint-all
- name: Public.MembershipBlueprint_one
  property_count: 33
  slug: hint-health-public-membership-blueprint-one
- name: Public.MembershipContractBlueprint_all
  property_count: 0
  slug: hint-health-public-membership-contract-blueprint-all
- name: Public.MembershipContractBlueprint_one
  property_count: 4
  slug: hint-health-public-membership-contract-blueprint-one
- name: Public.MembershipMemberBlueprint_all
  property_count: 0
  slug: hint-health-public-membership-member-blueprint-all
- name: Public.MembershipMemberBlueprint_one
  property_count: 10
  slug: hint-health-public-membership-member-blueprint-one
- name: Public.PartnerBlueprint_one
  property_count: 4
  slug: hint-health-public-partner-blueprint-one
- name: Public.PartnerChargeBlueprint_all
  property_count: 0
  slug: hint-health-public-partner-charge-blueprint-all
- name: Public.PartnerChargeBlueprint_one
  property_count: 3
  slug: hint-health-public-partner-charge-blueprint-one
- name: Public.PartnerProductHighlightBlueprint_all
  property_count: 0
  slug: hint-health-public-partner-product-highlight-blueprint-all
- name: Public.PartnerProductHighlightBlueprint_one
  property_count: 5
  slug: hint-health-public-partner-product-highlight-blueprint-one
- name: Public.PartnerProductLinkBlueprint_all
  property_count: 0
  slug: hint-health-public-partner-product-link-blueprint-all
- name: Public.PartnerProductLinkBlueprint_one
  property_count: 8
  slug: hint-health-public-partner-product-link-blueprint-one
- name: Public.PartnerProductOverviewBlueprint_one
  property_count: 2
  slug: hint-health-public-partner-product-overview-blueprint-one
- name: Public.PartnerProductPreconditionBlueprint_all
  property_count: 0
  slug: hint-health-public-partner-product-precondition-blueprint-all
- name: Public.PartnerProductPreconditionBlueprint_one
  property_count: 3
  slug: hint-health-public-partner-product-precondition-blueprint-one
- name: Public.PatientBlueprint_all
  property_count: 0
  slug: hint-health-public-patient-blueprint-all
- name: Public.PatientBlueprint_one
  property_count: 67
  slug: hint-health-public-patient-blueprint-one
- name: Public.PaymentBlueprint_all
  property_count: 0
  slug: hint-health-public-payment-blueprint-all
- name: Public.PaymentBlueprint_one
  property_count: 9
  slug: hint-health-public-payment-blueprint-one
- name: Public.PdfBlueprint_one
  property_count: 1
  slug: hint-health-public-pdf-blueprint-one
- name: Public.PlanBlueprint_all
  property_count: 0
  slug: hint-health-public-plan-blueprint-all
- name: Public.PracticeBlueprint_one
  property_count: 13
  slug: hint-health-public-practice-blueprint-one
- name: Public.PractitionerBlueprint_all
  property_count: 0
  slug: hint-health-public-practitioner-blueprint-all
- name: Public.PractitionerBlueprint_one
  property_count: 21
  slug: hint-health-public-practitioner-blueprint-one
- name: Public.ProductBlueprint_all
  property_count: 0
  slug: hint-health-public-product-blueprint-all
- name: Public.ProductBlueprint_one
  property_count: 8
  slug: hint-health-public-product-blueprint-one
- name: Public.ProductCategoryBlueprint_all
  property_count: 0
  slug: hint-health-public-product-category-blueprint-all
- name: Public.ProductCategoryBlueprint_one
  property_count: 2
  slug: hint-health-public-product-category-blueprint-one
- name: Public.ProductTestimonialBlueprint_all
  property_count: 0
  slug: hint-health-public-product-testimonial-blueprint-all
- name: Public.ProductTestimonialBlueprint_one
  property_count: 6
  slug: hint-health-public-product-testimonial-blueprint-one
- name: Public.QuoteBlueprint_one
  property_count: 7
  slug: hint-health-public-quote-blueprint-one
- name: Public.SignupAttemptBlueprint_all
  property_count: 0
  slug: hint-health-public-signup-attempt-blueprint-all
- name: Public.SignupAttemptBlueprint_one
  property_count: 12
  slug: hint-health-public-signup-attempt-blueprint-one
- name: Public.SocialSecurityNumberBlueprint_one
  property_count: 2
  slug: hint-health-public-social-security-number-blueprint-one
- name: Public.SupplementBlueprint_all
  property_count: 0
  slug: hint-health-public-supplement-blueprint-all
- name: Public.SupplementBlueprint_one
  property_count: 6
  slug: hint-health-public-supplement-blueprint-one
- name: Public.UserBlueprint_all
  property_count: 0
  slug: hint-health-public-user-blueprint-all
- name: Public.WebhookEndpointBlueprint_all
  property_count: 0
  slug: hint-health-public-webhook-endpoint-blueprint-all
- name: Public.WebhookEndpointBlueprint_one
  property_count: 6
  slug: hint-health-public-webhook-endpoint-blueprint-one
- name: Public.WebhookRequestBlueprint_all
  property_count: 0
  slug: hint-health-public-webhook-request-blueprint-all
- name: QuoteSanitizer
  property_count: 5
  slug: hint-health-quote-sanitizer
- name: Interaction.ClinicalNoteSanitizer
  property_count: 10
  slug: interaction-clinicalnotesanitizer
- name: Interaction.LabSanitizer.ActionSanitizer
  property_count: 2
  slug: interaction-labsanitizer-actionsanitizer
- name: Interaction.LabSanitizer.OrderSanitizer
  property_count: 10
  slug: interaction-labsanitizer-ordersanitizer
- name: Interaction.LabSanitizer.ReportSanitizer
  property_count: 4
  slug: interaction-labsanitizer-reportsanitizer
- name: Interaction.LabSanitizer.ResultCodeSanitizer
  property_count: 2
  slug: interaction-labsanitizer-resultcodesanitizer
- name: Interaction.LabSanitizer.ResultQuantitySanitizer
  property_count: 2
  slug: interaction-labsanitizer-resultquantitysanitizer
- name: Interaction.LabSanitizer.ResultRangeSanitizer
  property_count: 3
  slug: interaction-labsanitizer-resultrangesanitizer
- name: Interaction.LabSanitizer.ResultSanitizer
  property_count: 10
  slug: interaction-labsanitizer-resultsanitizer
- name: Interaction.LabSanitizer.SubjectSanitizer
  property_count: 2
  slug: interaction-labsanitizer-subjectsanitizer
- name: Interaction.LabSanitizer
  property_count: 9
  slug: interaction-labsanitizer
- name: MembershipCreateSanitizer
  property_count: 9
  slug: membershipcreatesanitizer
- name: MembershipPatientSanitizer.PatientSanitizer
  property_count: 2
  slug: membershippatientsanitizer-patientsanitizer
- name: MembershipPatientSanitizer
  property_count: 4
  slug: membershippatientsanitizer
- name: MembershipUpdateSanitizer.MembershipPatient
  property_count: 4
  slug: membershipupdatesanitizer-membershippatient
- name: MembershipUpdateSanitizer.Patient
  property_count: 2
  slug: membershipupdatesanitizer-patient
- name: MembershipUpdateSanitizer
  property_count: 8
  slug: membershipupdatesanitizer
- name: Npi
  property_count: 1
  slug: npi
- name: PartnerChargeLine
  property_count: 4
  slug: partnerchargeline
- name: PaymentSource
  property_count: 2
  slug: paymentsource
- name: PhoneNumber
  property_count: 4
  slug: phonenumber
- name: Platform.ApiKeyBlueprint_shared
  property_count: 4
  slug: platform-apikeyblueprint_shared
- name: Platform.IntegrationBlueprint_all
  property_count: 0
  slug: platform-integrationblueprint_all
- name: Platform.IntegrationBlueprint_one
  property_count: 8
  slug: platform-integrationblueprint_one
- name: Platform.IntegrationBlueprint_one_with_access_token
  property_count: 12
  slug: platform-integrationblueprint_one_with_access_token
- name: Update_Integration
  property_count: 1
  slug: platform-integrationscontroller-update_body
- name: OAuth
  property_count: 3
  slug: platform-oauthscontroller-tokens_body
- name: Platform.PartnerBlueprint_one
  property_count: 9
  slug: platform-partnerblueprint_one
- name: Platform.PartnerProductBlueprint_min
  property_count: 3
  slug: platform-partnerproductblueprint_min
- name: Update_Partner_Legacy
  property_count: 7
  slug: platform-partnerscontroller-update_body
- name: Platform.PracticeBlueprint_for_integration
  property_count: 2
  slug: platform-practiceblueprint_for_integration
- name: Platform.UserBlueprint_min
  property_count: 3
  slug: platform-userblueprint_min
- name: Platform.WebhookEndpointBlueprint_all
  property_count: 0
  slug: platform-webhookendpointblueprint_all
- name: Platform.WebhookEndpointBlueprint_one
  property_count: 5
  slug: platform-webhookendpointblueprint_one
- name: Platform.WebhookEndpointsController.create_body
  property_count: 1
  slug: platform-webhookendpointscontroller-create_body
- name: Update_WebhookEndpoint_Legacy
  property_count: 1
  slug: platform-webhookendpointscontroller-update_body
- name: Provider.Affiliates.PatientsController.create_body
  property_count: 1
  slug: provider-affiliates-patientscontroller-create_body
- name: Create_Charge_Item
  property_count: 4
  slug: provider-chargeitemscontroller-create_body
- name: Create_Charge_Item
  property_count: 4
  slug: provider-chargeitemscontroller-update_body
- name: Provider.ChargesController.create_body
  property_count: 9
  slug: provider-chargescontroller-create_body
- name: Create_Company_Plan
  property_count: 2
  slug: provider-companyplanscontroller-create_body
- name: Update_Company_Plan
  property_count: 1
  slug: provider-companyplanscontroller-update_body
- name: Create_Sponsorship
  property_count: 5
  slug: provider-companysponsorshipscontroller-create_body
- name: Update_Sponsorship
  property_count: 2
  slug: provider-companysponsorshipscontroller-update_body
- name: Provider.CreditCategoriesController.create_body
  property_count: 1
  slug: provider-creditcategoriescontroller-create_body
- name: Provider.CreditCategoriesController.update_body
  property_count: 1
  slug: provider-creditcategoriescontroller-update_body
- name: Create_Credit
  property_count: 4
  slug: provider-creditscontroller-create_body
- name: Update_Credit
  property_count: 2
  slug: provider-creditscontroller-update_body
- name: Provider.CustomerInvoices.ChargesController.create_body
  property_count: 10
  slug: provider-customerinvoices-chargescontroller-create_body
- name: Provider.CustomerInvoices.ChargesController.update_body
  property_count: 10
  slug: provider-customerinvoices-chargescontroller-update_body
- name: Create_Customer_Invoice
  property_count: 3
  slug: provider-customerinvoicescontroller-create_body
- name: Create_Customer_Invoice
  property_count: 3
  slug: provider-customerinvoicescontroller-update_body
- name: Create_InteractionNotification
  property_count: 1
  slug: provider-interactions-notificationscontroller-create_body
- name: Create_LeadSource
  property_count: 1
  slug: provider-leadsourcescontroller-create_body
- name: Create_LeadSource
  property_count: 1
  slug: provider-leadsourcescontroller-update_body
- name: Provider.LocationsController.create_body
  property_count: 10
  slug: provider-locationscontroller-create_body
- name: Provider.LocationsController.update_body
  property_count: 10
  slug: provider-locationscontroller-update_body
- name: Provider.MembersController.cancel_body
  property_count: 3
  slug: provider-memberscontroller-cancel_body
- name: Provider.MembershipContractsController.renew_body
  property_count: 1
  slug: provider-membershipcontractscontroller-renew_body
- name: Provider.MembershipContractsController.update_body
  property_count: 2
  slug: provider-membershipcontractscontroller-update_body
- name: Provider.MembershipsController.bill_body
  property_count: 1
  slug: provider-membershipscontroller-bill_body
- name: Provider.MembershipsController.cancel_body
  property_count: 3
  slug: provider-membershipscontroller-cancel_body
- name: Create_PartnerCharge
  property_count: 6
  slug: provider-partnerchargescontroller-create_body
- name: Create_DocumentInteraction
  property_count: 7
  slug: provider-patients-interactions-documentcontroller-create_body
- name: Update_DocumentInteraction
  property_count: 7
  slug: provider-patients-interactions-documentcontroller-update_body
- name: Create_PartnerInteraction
  property_count: 5
  slug: provider-patients-interactions-partnercontroller-create_body
- name: Update_PartnerInteraction
  property_count: 5
  slug: provider-patients-interactions-partnercontroller-update_body
- name: Provider.Patients.PaymentMethods.SetupController.create_body
  property_count: 2
  slug: provider-patients-paymentmethods-setupcontroller-create_body
- name: Provider.Patients.PaymentMethodsController.create_body
  property_count: 2
  slug: provider-patients-paymentmethodscontroller-create_body
- name: Create_Supplement
  property_count: 8
  slug: provider-patients-supplementscontroller-create_body
- name: Update_Supplement
  property_count: 8
  slug: provider-patients-supplementscontroller-update_body
- name: Create_Patient
  property_count: 43
  slug: provider-patientscontroller-create_body
- name: Match_Patients
  property_count: 6
  slug: provider-patientscontroller-matching_body
- name: Create_Patient
  property_count: 42
  slug: provider-patientscontroller-update_body
- name: Create Payment
  property_count: 6
  slug: provider-paymentscontroller-create_body
- name: Update_Practice
  property_count: 12
  slug: provider-practicescontroller-update_body
- name: Create_Practitioner
  property_count: 10
  slug: provider-practitionerscontroller-create_body
- name: Create_Practitioner
  property_count: 10
  slug: provider-practitionerscontroller-update_body
- name: Public.AddressBlueprint_leaf
  property_count: 9
  slug: public-addressblueprint_leaf
- name: Public.AffiliateBillBlueprint_all
  property_count: 0
  slug: public-affiliatebillblueprint_all
- name: Public.AffiliationBlueprint_affiliate_min
  property_count: 2
  slug: public-affiliationblueprint_affiliate_min
- name: Public.AffiliationBlueprint_all
  property_count: 0
  slug: public-affiliationblueprint_all
- name: Public.CancellationReasonBlueprint_all
  property_count: 0
  slug: public-cancellationreasonblueprint_all
- name: Public.CategoryBlueprint_one
  property_count: 4
  slug: public-categoryblueprint_one
- name: Public.ChargeBlueprint_one
  property_count: 19
  slug: public-chargeblueprint_one
- name: Public.ChargeBlueprint_one_with_invoice
  property_count: 20
  slug: public-chargeblueprint_one_with_invoice
- name: Public.ChargeItemBlueprint_all
  property_count: 0
  slug: public-chargeitemblueprint_all
- name: Public.ChargeItemBlueprint_one
  property_count: 10
  slug: public-chargeitemblueprint_one
- name: Public.CompanyAccountBlueprint_for_membership_one
  property_count: 2
  slug: public-companyaccountblueprint_for_membership_one
- name: Public.CompanyAccountBlueprint_min
  property_count: 1
  slug: public-companyaccountblueprint_min
- name: Public.CompanyBlueprint_all
  property_count: 0
  slug: public-companyblueprint_all
- name: Public.CompanyBlueprint_leaf
  property_count: 2
  slug: public-companyblueprint_leaf
- name: Public.CompanyBlueprint_one
  property_count: 10
  slug: public-companyblueprint_one
- name: Public.CompanyPlanBlueprint_all
  property_count: 0
  slug: public-companyplanblueprint_all
- name: Public.CompanyPlanBlueprint_one
  property_count: 4
  slug: public-companyplanblueprint_one
- name: Public.CompanySponsorshipBlueprint_for_patient
  property_count: 6
  slug: public-companysponsorshipblueprint_for_patient
- name: Public.CouponBlueprint_all
  property_count: 0
  slug: public-couponblueprint_all
- name: Public.CouponBlueprint_one
  property_count: 13
  slug: public-couponblueprint_one
- name: Public.CreditBlueprint_all
  property_count: 0
  slug: public-creditblueprint_all
- name: Public.CreditBlueprint_min
  property_count: 1
  slug: public-creditblueprint_min
- name: Public.CreditBlueprint_one
  property_count: 8
  slug: public-creditblueprint_one
- name: Public.CreditCategoryBlueprint_all
  property_count: 0
  slug: public-creditcategoryblueprint_all
- name: Public.CreditCategoryBlueprint_min
  property_count: 2
  slug: public-creditcategoryblueprint_min
- name: Public.CreditCategoryBlueprint_one
  property_count: 4
  slug: public-creditcategoryblueprint_one
- name: Public.CreditLineBlueprint_all
  property_count: 0
  slug: public-creditlineblueprint_all
- name: Public.CustomerInvoiceBlueprint_all
  property_count: 0
  slug: public-customerinvoiceblueprint_all
- name: Public.CustomerInvoiceBlueprint_one
  property_count: 24
  slug: public-customerinvoiceblueprint_one
- name: Public.EmployeeDivisionBlueprint_all
  property_count: 0
  slug: public-employeedivisionblueprint_all
- name: Public.EmployeeDivisionBlueprint_leaf
  property_count: 2
  slug: public-employeedivisionblueprint_leaf
- name: Public.ExternalRecordBlueprint_min
  property_count: 2
  slug: public-externalrecordblueprint_min
- name: Public.FormBlueprint_leaf
  property_count: 5
  slug: public-formblueprint_leaf
- name: Public.FormItemBlueprint_leaf
  property_count: 5
  slug: public-formitemblueprint_leaf
- name: Public.FormResponseBlueprint_all
  property_count: 0
  slug: public-formresponseblueprint_all
- name: Public.FormResponseBlueprint_one
  property_count: 5
  slug: public-formresponseblueprint_one
- name: Public.FormResponseItemBlueprint_leaf
  property_count: 3
  slug: public-formresponseitemblueprint_leaf
- name: Public.Interaction.ClinicalNoteBlueprint_one
  property_count: 11
  slug: public-interaction-clinicalnoteblueprint_one
- name: Public.Interaction.Lab.Order.ActionBlueprint_leaf
  property_count: 2
  slug: public-interaction-lab-order-actionblueprint_leaf
- name: Public.Interaction.Lab.Order.SubjectBlueprint_leaf
  property_count: 2
  slug: public-interaction-lab-order-subjectblueprint_leaf
- name: Public.Interaction.Lab.OrderBlueprint_leaf
  property_count: 10
  slug: public-interaction-lab-orderblueprint_leaf
- name: Public.Interaction.Lab.ReportBlueprint_leaf
  property_count: 4
  slug: public-interaction-lab-reportblueprint_leaf
- name: Public.Interaction.Lab.Result.CodeBlueprint_leaf
  property_count: 2
  slug: public-interaction-lab-result-codeblueprint_leaf
- name: Public.Interaction.Lab.Result.QuantityBlueprint_leaf
  property_count: 2
  slug: public-interaction-lab-result-quantityblueprint_leaf
- name: Public.Interaction.Lab.Result.RangeBlueprint_leaf
  property_count: 3
  slug: public-interaction-lab-result-rangeblueprint_leaf
- name: Public.Interaction.Lab.ResultBlueprint_leaf
  property_count: 10
  slug: public-interaction-lab-resultblueprint_leaf
- name: Public.Interaction.LabBlueprint_one
  property_count: 8
  slug: public-interaction-labblueprint_one
- name: Public.InteractionBlueprint_all
  property_count: 0
  slug: public-interactionblueprint_all
- name: Public.InteractionBlueprint_one
  property_count: 6
  slug: public-interactionblueprint_one
- name: Public.InteractionNotificationBlueprint_one
  property_count: 2
  slug: public-interactionnotificationblueprint_one
- name: Public.KnownPracticeBlueprint_min
  property_count: 2
  slug: public-knownpracticeblueprint_min
- name: Public.LeadSourceBlueprint_all
  property_count: 0
  slug: public-leadsourceblueprint_all
- name: Public.LeadSourceBlueprint_leaf
  property_count: 2
  slug: public-leadsourceblueprint_leaf
- name: Public.LeadSourceBlueprint_one
  property_count: 4
  slug: public-leadsourceblueprint_one
- name: Public.LocationBlueprint_all
  property_count: 0
  slug: public-locationblueprint_all
- name: Public.LocationBlueprint_min
  property_count: 2
  slug: public-locationblueprint_min
- name: Public.LocationBlueprint_one
  property_count: 14
  slug: public-locationblueprint_one
- name: Public.LocationBlueprint_shared
  property_count: 8
  slug: public-locationblueprint_shared
- name: Public.LocationGroupBlueprint_leaf
  property_count: 5
  slug: public-locationgroupblueprint_leaf
- name: Public.MembershipBillBlueprint_shared_with_invoice
  property_count: 14
  slug: public-membershipbillblueprint_shared_with_invoice
- name: Public.MembershipBlueprint_all
  property_count: 0
  slug: public-membershipblueprint_all
- name: Public.MembershipBlueprint_min
  property_count: 1
  slug: public-membershipblueprint_min
- name: Public.MembershipBlueprint_one
  property_count: 33
  slug: public-membershipblueprint_one
- name: Public.MembershipContractBlueprint_all
  property_count: 0
  slug: public-membershipcontractblueprint_all
- name: Public.MembershipContractBlueprint_one
  property_count: 4
  slug: public-membershipcontractblueprint_one
- name: Public.MembershipMemberBlueprint_all
  property_count: 0
  slug: public-membershipmemberblueprint_all
- name: Public.MembershipMemberBlueprint_for_patient
  property_count: 8
  slug: public-membershipmemberblueprint_for_patient
- name: Public.MembershipMemberBlueprint_one
  property_count: 10
  slug: public-membershipmemberblueprint_one
- name: Public.MembershipPatientBlueprint_for_membership_one
  property_count: 10
  slug: public-membershippatientblueprint_for_membership_one
- name: Public.MembershipPatientBlueprint_leaf_with_patient
  property_count: 8
  slug: public-membershippatientblueprint_leaf_with_patient
- name: Public.MembershipPatientBlueprint_one
  property_count: 11
  slug: public-membershippatientblueprint_one
- name: Public.NpiBlueprint_shared
  property_count: 5
  slug: public-npiblueprint_shared
- name: Public.PartnerAppUserBlueprint_leaf
  property_count: 3
  slug: public-partnerappuserblueprint_leaf
- name: Public.PartnerChargeBlueprint_all
  property_count: 0
  slug: public-partnerchargeblueprint_all
- name: Public.PartnerChargeBlueprint_one
  property_count: 3
  slug: public-partnerchargeblueprint_one
- name: Public.PartnerProductBlueprint_leaf
  property_count: 2
  slug: public-partnerproductblueprint_leaf
- name: Public.PatientBlueprint_account
  property_count: 2
  slug: public-patientblueprint_account
- name: Public.PatientBlueprint_all
  property_count: 0
  slug: public-patientblueprint_all
- name: Public.PatientBlueprint_leaf
  property_count: 54
  slug: public-patientblueprint_leaf
- name: Public.PatientBlueprint_min
  property_count: 2
  slug: public-patientblueprint_min
- name: Public.PatientBlueprint_one
  property_count: 67
  slug: public-patientblueprint_one
- name: Public.Payable.InvoiceBlueprint_for_membership_bill
  property_count: 8
  slug: public-payable-invoiceblueprint_for_membership_bill
- name: Public.Payable.InvoiceBlueprint_min_with_owner
  property_count: 4
  slug: public-payable-invoiceblueprint_min_with_owner
- name: Public.Payable.InvoiceBlueprint_one
  property_count: 8
  slug: public-payable-invoiceblueprint_one
- name: Public.Payable.OwnerBlueprint_min
  property_count: 2
  slug: public-payable-ownerblueprint_min
- name: Public.PaymentBlueprint_all
  property_count: 0
  slug: public-paymentblueprint_all
- name: Public.PaymentBlueprint_one
  property_count: 9
  slug: public-paymentblueprint_one
- name: Public.PdfBlueprint_one
  property_count: 1
  slug: public-pdfblueprint_one
- name: Public.PhoneBlueprint_leaf
  property_count: 2
  slug: public-phoneblueprint_leaf
- name: Public.PlanBlueprint_all
  property_count: 0
  slug: public-planblueprint_all
- name: Public.PlanBlueprint_min
  property_count: 3
  slug: public-planblueprint_min
- name: Public.PracticeBlueprint_one
  property_count: 13
  slug: public-practiceblueprint_one
- name: Public.PractitionerBlueprint_all
  property_count: 0
  slug: public-practitionerblueprint_all
- name: Public.PractitionerBlueprint_min
  property_count: 2
  slug: public-practitionerblueprint_min
- name: Public.PractitionerBlueprint_one
  property_count: 21
  slug: public-practitionerblueprint_one
- name: Public.QuoteBlueprint_one
  property_count: 7
  slug: public-quoteblueprint_one
- name: Public.SignupAttemptBlueprint_all
  property_count: 0
  slug: public-signupattemptblueprint_all
- name: Public.SignupAttemptBlueprint_one
  property_count: 12
  slug: public-signupattemptblueprint_one
- name: Public.SignupPageBlueprint_leaf
  property_count: 2
  slug: public-signuppageblueprint_leaf
- name: Public.SocialSecurityNumberBlueprint_one
  property_count: 2
  slug: public-socialsecuritynumberblueprint_one
- name: Public.SourceBlueprint_leaf
  property_count: 2
  slug: public-sourceblueprint_leaf
- name: Public.SpecialtyBlueprint_all
  property_count: 0
  slug: public-specialtyblueprint_all
- name: Public.SupplementBlueprint_all
  property_count: 0
  slug: public-supplementblueprint_all
- name: Public.SupplementBlueprint_one
  property_count: 6
  slug: public-supplementblueprint_one
- name: Public.UserBlueprint_all
  property_count: 0
  slug: public-userblueprint_all
- name: QuoteSanitizer.MemberSanitizer
  property_count: 5
  slug: quotesanitizer-membersanitizer
- name: QuoteSanitizer
  property_count: 5
  slug: quotesanitizer
- name: Create_SSN
  property_count: 1
  slug: socialsecuritynumber
jsonld:
- class_count: 2
  name: Hint Health Context
  property_count: 66
  slug: hint-health-context
layout: provider
mcp_servers:
- description: Hint publishes a hosted, remote MCP server that exposes its public developer documentation and API reference to MCP-capable agents. It is documented at developers.hint.com/docs/hint-mcp-server and ans
  name: Hint Health MCP Server
  slug: hint-health-mcp-server
modified: '2026-08-15'
name: Hint Health
nav: Providers
network: true
overview: 'Hint Health publishes 67 API contracts indexed on the [APIs.io](https://apis.io/) network, including AccountAccessToken API, Affiliate API, AffiliateBill API, and 64 more. Tagged areas include Direct Primary Care, DPC, Healthcare, Membership Management, and Patient Enrollment.


  The Hint Health catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Hint Health''s developer surface includes authentication, documentation, engineering blog, pricing, API reference, getting-started guide, support, and 49 more developer resources.'
plans:
- name: Hint Health Plans Pricing
  plan_count: 4
  slug: hint-health-plans-pricing
- name: Hint Health Price Estimates
  plan_count: 0
  slug: hint-health-price-estimates
random_paper: 6
rate_limits:
- limit_count: 2
  name: Hint Health Rate Limits
  slug: hint-health-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Hint Health — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: hint-health-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Hint Health API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: hint-health-rules
score:
  band: exemplar
  composite: 78.3
  coverage:
    artifact_dirs: 36
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.2
  facets:
    access_clarity: 100.0
    contract_governance: 35.6
    contract_quality: 71.2
    developer_ergonomics: 78.6
    discoverability: 75.0
    operational_transparency: 65.8
  previous_composite: 75.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 26.9
      total: 67
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/hint-health/hint-health-2026-06-20T182747.png
security:
- kind: authentication
  name: Hint Health Authentication
  slug: hint-health-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Hint Health Domain Security
  slug: hint-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hint Health Vulnerability Disclosure
  slug: hint-health-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Hint Health Trust Center
  slug: hint-health-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA
skill_count: 17
skills:
- name: hint-health-audit-skill
  slug: hint-health-audit-skill
- name: hint-health-bill-and-collect-invoice
  slug: hint-health-bill-and-collect-invoice
- name: hint-health-common-api-conventions
  slug: hint-health-common-api-conventions
- name: hint-health-common-brand-styles
  slug: hint-health-common-brand-styles
- name: hint-health-common-caching-patterns
  slug: hint-health-common-caching-patterns
- name: hint-health-common-marketplace-contract
  slug: hint-health-common-marketplace-contract
- name: hint-health-common-node-template
  slug: hint-health-common-node-template
- name: hint-health-common-provider-api-fields
  slug: hint-health-common-provider-api-fields
- name: hint-health-common-provider-api
  slug: hint-health-common-provider-api
- name: hint-health-common-sidebar-icons
  slug: hint-health-common-sidebar-icons
- name: hint-health-create-app-skill
  slug: hint-health-create-app-skill
- name: hint-health-enroll-patient-and-membership
  slug: hint-health-enroll-patient-and-membership
- name: hint-health-fill-listing-skill
  slug: hint-health-fill-listing-skill
- name: hint-health-marketplace-readme
  slug: hint-health-marketplace-readme
- name: hint-health-marketplace-skill
  slug: hint-health-marketplace-skill
- name: hint-health-retrofit-skill
  slug: hint-health-retrofit-skill
- name: hint-health-write-clinical-interaction
  slug: hint-health-write-clinical-interaction
slug: hint-health
tags:
- Direct Primary Care
- DPC
- Healthcare
- Membership Management
- Patient Enrollment
- Medical Billing
- Electronic Health Records
- Health Plans
website: https://www.hint.com/
---
