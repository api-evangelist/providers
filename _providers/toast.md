---
access_model:
  confidence: high
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 38
  human_in_the_loop: 1
  name: Toast Agentic Access
  operation_count: 123
  slug: toast-agentic-access
  summary_line: 123 operations · 38 acting · 1 human-in-the-loop
api_count: 20
apis:
- baseURL: https://toast-api-server/authentication/v1
  baseurl_source: spec
  description: The Authentication API from Toast — 1 operation(s) for authentication.
  name: Toast Authentication API
  phrasing_intents:
  - id: authenticationLoginPost
    intent: Get an API authentication token
    question: Where do I get an access token for calling the Toast platform APIs?
  phrasing_ops: 1
  slug: toast-authentication-api
- baseURL: https://toast-api-server/partners/v1
  baseurl_source: spec
  description: The ConnectedRestaurants API from Toast — 1 operation(s) for connectedrestaurants.
  name: Toast ConnectedRestaurants API
  phrasing_intents:
  - id: connectedRestaurantsGet
    intent: List restaurants connected to my integration
    question: Which restaurants have connected to my partner integration?
  phrasing_ops: 1
  slug: toast-connectedrestaurants-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: Related to price reduction applied to restaurant orders. For example, a restaurant might apply a discount for a promotion.
  name: Toast Discounts API
  phrasing_intents:
  - id: discountsGuidGet
    intent: Look up one configured discount
    question: How do I view the setup of a single discount at a restaurant?
  - id: discountsGet
    intent: List a restaurant's configured discounts
    question: Which discounts has a restaurant configured?
  - id: ordersChecksAppliedDiscountsPost
    intent: Apply a discount to a whole check
    question: How do I add a check-level discount to an existing order?
  - id: ordersChecksSelectionsAppliedDiscountsPost
    intent: Apply a discount to one item on a check
    question: Can I discount a single menu item on a check rather than the whole check?
  - id: applicableDiscountsPost
    intent: Find discounts that apply to an order
    question: Which discounts would apply to the checks and items in an order before I submit it?
  phrasing_ops: 5
  slug: toast-discounts-api
- baseURL: https://toast-api-server/labor/v1
  baseurl_source: spec
  description: The Employees API from Toast — 6 operation(s) for employees.
  name: Toast Employees API
  phrasing_intents:
  - id: employeesGet
    intent: List restaurant employees
    question: Who are the employees on staff at a restaurant?
  - id: employeesPost
    intent: Add a new employee
    question: How do I create a new employee record at a restaurant?
  - id: employeesEmployeeIdGet
    intent: Look up one employee
    question: What information does Toast hold for one particular employee?
  - id: employeesEmployeeIdDelete
    intent: Delete an employee record
    question: What happens to a staff member's login when their employee record is deleted?
  - id: employeesEmployeeIdPatch
    intent: Update an employee's name or passcode
    question: How do I change an employee's name, chosen name or passcode?
  - id: employeesEmployeeIdExternalIdPost
    intent: Add an external ID to an employee
    question: Can I attach an external identifier to an employee who does not have one yet?
  - id: employeesEmployeeIdExternalIdPut
    intent: Set or replace an employee's external ID
    question: How do I overwrite an employee's existing external identifier?
  - id: employeesEmployeeIdUnarchivePut
    intent: Unarchive an employee
    question: How do I restore an archived employee so they can sign into the POS again?
  phrasing_ops: 10
  slug: toast-employees-api
- baseURL: https://toast-api-server/restaurants/v1
  baseurl_source: spec
  description: The Groups API from Toast — 1 operation(s) for groups.
  name: Toast Groups API
  phrasing_intents:
  - id: groupsManagementGroupGuidRestaurantsGet
    intent: List restaurants in a management group
    question: Which restaurants belong to a particular management group?
  phrasing_ops: 1
  slug: toast-groups-api
- baseURL: https://toast-api-server/labor/v1
  baseurl_source: spec
  description: The Jobs API from Toast — 3 operation(s) for jobs.
  name: Toast Jobs API
  phrasing_intents:
  - id: jobsGet
    intent: List employee jobs at a restaurant
    question: Which employee jobs are configured at a restaurant?
  - id: jobsJobIdGet
    intent: Look up one job
    question: What details are stored for one specific employee job?
  - id: jobsJobIdExternalIdPost
    intent: Add an external ID to a job
    question: Can I attach an external identifier to a job that does not have one?
  - id: jobsJobIdExternalIdPut
    intent: Set or replace a job's external ID
    question: How do I overwrite the external identifier already on a job?
  phrasing_ops: 4
  slug: toast-jobs-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Menus API from Toast — 1 operation(s) for menus.
  name: Toast Menus API
  phrasing_intents:
  - id: menusGuidGet
    intent: Look up one menu
    question: How do I get one specific menu, like the dessert menu, for a restaurant?
  - id: menusGet
    intent: List a restaurant's menus
    question: Which menus such as drinks, dinner and dessert does a restaurant have?
  phrasing_ops: 2
  slug: toast-menus-api
- baseURL: https://toast-api-server/menus/v2
  baseurl_source: spec
  description: The Metadata API from Toast — 1 operation(s) for metadata.
  name: Toast Metadata API
  phrasing_intents:
  - id: metadataGet
    intent: Check when a restaurant's menu last changed
    question: How can I tell if a restaurant's menu data has been updated before downloading it again?
  phrasing_ops: 1
  slug: toast-metadata-api
- baseURL: https://toast-api-server/orders/v2
  baseurl_source: spec
  description: Related to orders made by restaurant guests. For example, a restaurant guest orders items from a menu. Toast platform orders include one or more guest check.
  name: Toast Orders API
  phrasing_intents:
  - id: pricesPost
    intent: Calculate prices and taxes for an order
    question: What would the total, tax and service charges be for an order before submitting it?
  - id: ordersGuidGet
    intent: Look up one order
    question: Where can I see full details for a single order by its GUID?
  - id: ordersBulkGet
    intent: Get full order details for a time period
    question: Can I download complete order details for every order opened in a business day?
  - id: ordersOrderGuidChecksCheckGuidSelectionsPost
    intent: Add items to an existing check
    question: Is it possible to add more menu items to a check that is already open?
  - id: ordersOrderGuidDeliveryInfoPatch
    intent: Update an order's delivery details
    question: Can I mark a delivery order as dispatched or delivered?
  - id: voidOrder
    intent: Void an order
    question: How do I void an order along with its items and payments?
  - id: ordersPost
    intent: Place a new order
    question: How do I submit a new order to a restaurant?
  - id: ordersGet
    intent: List order GUIDs for a period (deprecated)
    question: Is there an older endpoint that returns only the GUIDs of orders opened in a time window?
  phrasing_ops: 8
  slug: toast-orders-api
- baseURL: https://toast-api-server/orders/v2
  baseurl_source: spec
  description: Related to guests' payments for restaurant orders. Toast platform payments apply to a check in an order.
  name: Toast Payments API
  phrasing_intents:
  - id: paymentsGet
    intent: List payment GUIDs for a business day
    question: Which payments were made during a restaurant business day?
  - id: paymentsGuidGet
    intent: Look up one payment
    question: What does the full record of one payment look like?
  - id: ordersChecksPaymentsPost
    intent: Add payments to a check
    question: How do I record a payment against a check in an existing order?
  - id: ordersOrderGuidChecksCheckGuidPaymentsPaymentGuidPatch
    intent: Change the tip on a payment
    question: Can a guest's tip be adjusted on a payment after the check is paid?
  phrasing_ops: 4
  slug: toast-payments-api
- baseURL: https://toast-api-server/partners/v1
  baseurl_source: spec
  description: The Restaurants API from Toast — 2 operation(s) for restaurants.
  name: Toast Restaurants API
  phrasing_intents:
  - id: restaurantsGet
    intent: List restaurants my client can access
    question: Which restaurants can my partner API client access?
  - id: restaurantsRestaurantGuidGet
    intent: Get a restaurant's configuration
    question: How do I get the detailed configuration of one restaurant?
  phrasing_ops: 2
  slug: toast-restaurants-api
- baseURL: https://toast-api-server/labor/v1
  baseurl_source: spec
  description: The Shifts API from Toast — 2 operation(s) for shifts.
  name: Toast Shifts API
  phrasing_intents:
  - id: shiftsGet
    intent: List scheduled employee shifts
    question: Which employee shifts are scheduled between two dates?
  - id: shiftsPost
    intent: Schedule a new employee shift
    question: How do I add a scheduled shift for an employee?
  - id: shiftsShiftIdGet
    intent: Look up one scheduled shift
    question: What are the details of one particular scheduled shift?
  - id: shiftsShiftIdPut
    intent: Replace an existing shift
    question: How do I change the times of a shift that is already scheduled?
  - id: shiftsShiftIdDelete
    intent: Delete a scheduled shift
    question: What happens if I delete a shift that was already deleted?
  phrasing_ops: 5
  slug: toast-shifts-api
- baseURL: https://toast-api-server/stock
  baseurl_source: spec
  description: The Stock API from Toast — 3 operation(s) for stock.
  name: Toast Stock API
  phrasing_intents:
  - id: getInventory
    intent: List menu items that are out of stock or limited
    question: Which menu items are out of stock or running on a limited quantity?
  - id: postInventorySearch
    intent: Check stock for specific menu items
    question: Can I check the stock status of a particular list of menu items?
  - id: updateInventory
    intent: Update stock for specific menu items
    question: How do I mark a menu item as out of stock?
  phrasing_ops: 3
  slug: toast-stock-api
- baseURL: https://toast-api-server/labor/v1
  baseurl_source: spec
  description: The Time entries API from Toast — 2 operation(s) for time entries.
  name: Toast Time entries API
  phrasing_intents:
  - id: timeEntriesGet
    intent: List employee clock-in time entries
    question: When did employees clock in and out, including breaks, on a given business day?
  - id: timeEntriesTimeEntryIdGet
    intent: Look up one time entry
    question: What were the start, end and break times for one employee time entry?
  phrasing_ops: 2
  slug: toast-time-entries-api
- baseURL: https://toast-api-server/era/v1
  baseurl_source: spec
  description: The analytics API endpoints for aggregated sales reporting data covering sales and labor information.
  name: Toast Aggregated sales API
  phrasing_intents:
  - id: postMetricsReportingDataCustomTimeRangeRequest
    intent: Request aggregated sales for a custom date range
    question: How do I request aggregated sales totals across my restaurants for an arbitrary span of business dates?
  - id: postMetricsReportingDataSpecificTimeRangeRequest
    intent: Request aggregated sales for a preset time range
    question: Can I request daily or weekly sales metrics using a preset time range instead of custom dates?
  - id: getMetricsReportingData
    intent: Fetch the results of a sales metrics report
    question: How do I download the aggregated sales numbers once my metrics report request is ready?
  - id: getMetricsReportingDataSpecificTimeRange
    intent: Fetch sales metrics via the deprecated time-range path
    question: Is there an older endpoint that returns sales metrics results using both the time range and the report GUID?
  phrasing_ops: 4
  slug: toast-aggregated-sales-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Alternate Payment Types API from Toast — 2 operation(s) for alternate payment types.
  name: Toast Alternate Payment Types API
  phrasing_intents:
  - id: alternatePaymentTypesGuidGet
    intent: Look up one alternate payment type
    question: How do I see the details of a single non-standard tender, like a house account, configured at a restaurant?
  - id: alternatePaymentTypesGet
    intent: List a restaurant's alternate payment types
    question: Which alternate forms of payment has a restaurant set up?
  phrasing_ops: 2
  slug: toast-alternate-payment-types-api
- baseURL: https://toast-api-server/restaurant-availability/v1
  baseurl_source: spec
  description: The availability API from Toast — 1 operation(s) for availability.
  name: Toast Availability API
  phrasing_intents:
  - id: availabilityGet
    intent: Check if a restaurant accepts online orders
    question: Is this restaurant currently online or offline for online ordering?
  phrasing_ops: 1
  slug: toast-availability-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Break Types API from Toast — 2 operation(s) for break types.
  name: Toast Break Types API
  phrasing_intents:
  - id: breakTypesGuidGet
    intent: Look up one break type
    question: How do I see the settings for one specific break type at a restaurant?
  - id: breakTypesGet
    intent: List a restaurant's break types
    question: Which employee break types are configured at my restaurant?
  phrasing_ops: 2
  slug: toast-break-types-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Cash Drawers API from Toast — 2 operation(s) for cash drawers.
  name: Toast Cash Drawers API
  phrasing_intents:
  - id: cashDrawersGuidGet
    intent: Look up one cash drawer device
    question: How do I get details for one specific cash drawer at a restaurant?
  - id: cashDrawersGet
    intent: List a restaurant's cash drawers
    question: Which cash drawer devices does a restaurant have?
  phrasing_ops: 2
  slug: toast-cash-drawers-api
- baseURL: https://toast-api-server/era/v1
  baseurl_source: spec
  description: The analytics API endpoints for check reporting data.
  name: Toast Check API
  phrasing_intents:
  - id: postCheckReportingDataSpecificTimeRangeRequest
    intent: Request check-level reporting data
    question: How do I request a report of checks for a range of business dates?
  - id: getCheckReportingData
    intent: Fetch the results of a check report
    question: Where do I retrieve the check data once my check report request finishes?
  phrasing_ops: 2
  slug: toast-check-api
- baseURL: https://toast-api-server/cashmgmt/v1
  baseurl_source: spec
  description: The Deposits API from Toast — 1 operation(s) for deposits.
  name: Toast Deposits API
  phrasing_intents:
  - id: depositsGet
    intent: List cash deposits for a business day
    question: How much cash was pulled from the restaurant for bank deposit on a given day?
  phrasing_ops: 1
  slug: toast-deposits-api
- baseURL: https://toast-api-server/device-details/v1
  baseurl_source: spec
  description: The Device details API from Toast — 1 operation(s) for device details.
  name: Toast Device details API
  phrasing_intents:
  - id: getDeviceInfo
    intent: Get device details for a restaurant location
    question: What POS terminals, handhelds and printers are installed at a location?
  phrasing_ops: 1
  slug: toast-device-details-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Dining Options API from Toast — 2 operation(s) for dining options.
  name: Toast Dining Options API
  phrasing_intents:
  - id: diningOptionsGuidGet
    intent: Look up one dining option
    question: How do I see details for one service type, like take out, at a restaurant?
  - id: diningOptionsGet
    intent: List a restaurant's dining options
    question: Which dining options such as dine in, take out or delivery does a restaurant offer?
  phrasing_ops: 2
  slug: toast-dining-options-api
- baseURL: https://toast-api-server/cashmgmt/v1
  baseurl_source: spec
  description: The Entries API from Toast — 1 operation(s) for entries.
  name: Toast Entries API
  phrasing_intents:
  - id: entriesGet
    intent: List cash drawer entries for a day
    question: How much cash was added to or taken out of the cash drawers on a given business day?
  phrasing_ops: 1
  slug: toast-entries-api
- baseURL: https://toast-api-server/kitchen/v1
  baseurl_source: spec
  description: The Export API from Toast — 1 operation(s) for export.
  name: Toast Export API
  phrasing_intents:
  - id: itemFulfillmentsGet
    intent: Export item fulfillments for a business date
    question: Can I export all item fulfillments for a single business date?
  phrasing_ops: 1
  slug: toast-export-api
- baseURL: https://toast-api-server/era/v1
  baseurl_source: spec
  description: The analytics API endpoint for guest reporting data organized by payment.
  name: Toast Guest API
  phrasing_intents:
  - id: postGuestReportPaymentDateSpecificTimeRange
    intent: Request guest data organized by payment
    question: How do I request a report of guest data organized by payment for a date range?
  - id: getGuestByPaymentDateReportingData
    intent: Fetch guest-by-payment report results
    question: Where do I collect the guest data once my guest-by-payment request is done?
  phrasing_ops: 2
  slug: toast-guest-api
- baseURL: https://toast-api-server/era/v1
  baseurl_source: spec
  description: The analytics API endpoints for labor reporting data. This only supports hourly job and employee data.
  name: Toast Labor API
  phrasing_intents:
  - id: postLaborReportingDataSpecificTimeRangeRequest
    intent: Request labor reporting data
    question: How do I request labor data for my restaurants over a date range?
  - id: getLaborReportingData
    intent: Fetch labor report results
    question: Where do I get the labor numbers once my labor report request is ready?
  phrasing_ops: 2
  slug: toast-labor-api
- baseURL: https://toast-api-server/era/v1
  baseurl_source: spec
  description: The analytics API endpoints for menu reporting data.
  name: Toast Menu API
  phrasing_intents:
  - id: postMenuReportCustomTimeRange
    intent: Request menu sales data for custom dates
    question: How do I request menu performance data for any start and end business date?
  - id: postMenuReportSpecificTimeRange
    intent: Request menu data for a preset time range
    question: Can I request menu reporting data for a fixed period like one day?
  - id: getMenuReportingData
    intent: Fetch menu report results
    question: Where do I retrieve menu reporting data after my request completes?
  phrasing_ops: 3
  slug: toast-menu-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Menu Groups API from Toast — 2 operation(s) for menu groups.
  name: Toast Menu Groups API
  phrasing_intents:
  - id: menuGroupsGuidGet
    intent: Look up one menu group
    question: How do I see the details of one section of a menu, like appetizers?
  - id: menuGroupsGet
    intent: List a restaurant's menu groups
    question: Which menu sections are configured across a restaurant's menus?
  phrasing_ops: 2
  slug: toast-menu-groups-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Menu Items API from Toast — 2 operation(s) for menu items.
  name: Toast Menu Items API
  phrasing_intents:
  - id: menuItemsGuidGet
    intent: Look up one menu item or modifier
    question: How do I get the details of a single dish or modifier on a restaurant's menu?
  - id: menuItemsGet
    intent: List a restaurant's menu items and modifiers
    question: Which items and modifiers can guests order from a restaurant?
  phrasing_ops: 2
  slug: toast-menu-items-api
- baseURL: https://toast-api-server/ccpartner/v1
  baseurl_source: spec
  description: The Merchants API from Toast — 1 operation(s) for merchants.
  name: Toast Merchants API
  phrasing_intents:
  - id: merchantsMerchantUuidPaymentsPaymentUuidPut
    intent: Authorize a credit card payment
    question: How do I authorize a credit card so funds are held until capture or void?
  phrasing_ops: 1
  slug: toast-merchants-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Modifier Groups API from Toast — 2 operation(s) for modifier groups.
  name: Toast Modifier Groups API
  phrasing_intents:
  - id: menuOptionGroupsGuidGet
    intent: Look up one modifier group
    question: How do I see one modifier group, like salad dressing choices?
  - id: menuOptionGroupsGet
    intent: List a restaurant's modifier groups
    question: Which modifier groups are set up for a restaurant's menu items?
  phrasing_ops: 2
  slug: toast-modifier-groups-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The No Sale Reasons API from Toast — 2 operation(s) for no sale reasons.
  name: Toast No Sale Reasons API
  phrasing_intents:
  - id: noSaleReasonsGuidGet
    intent: Look up one no sale reason
    question: How do I see why a cash drawer may be opened without a sale for one reason code?
  - id: noSaleReasonsGet
    intent: List a restaurant's no sale reasons
    question: Which no sale reasons are configured at a restaurant?
  phrasing_ops: 2
  slug: toast-no-sale-reasons-api
- baseURL: https://toast-api-server/ordermgmt-config/v1
  baseurl_source: spec
  description: Operations related to online ordering schedules
  name: Toast Ordering Schedule API
  phrasing_intents:
  - id: orderingScheduleGet
    intent: Get a location's online ordering schedule
    question: What hours does a restaurant location accept online orders?
  phrasing_ops: 1
  slug: toast-ordering-schedule-api
- baseURL: https://toast-api-server/era/v1
  baseurl_source: spec
  description: The analytics API endpoint for payout reporting data organized by payments.
  name: Toast Payout by payments API
  phrasing_intents:
  - id: postPayoutReportPaymentsSpecificTimeRange
    intent: Request payout data organized by payment
    question: How do I request payout data broken down by individual payment?
  - id: getPayoutPaymentsReportingData
    intent: Fetch payout-by-payment report results
    question: Where do I get the payout data by payment once my request is ready?
  phrasing_ops: 2
  slug: toast-payout-by-payments-api
- baseURL: https://toast-api-server/era/v1
  baseurl_source: spec
  description: The analytics API endpoint for payout reporting data organized by sales date.
  name: Toast Payout by sales date API
  phrasing_intents:
  - id: postPayoutReportSalesDateSpecificTimeRange
    intent: Request payout data organized by sales date
    question: How do I request payouts grouped by the date the sales happened?
  - id: getPayoutSalesDateReportingData
    intent: Fetch payout-by-sales-date report results
    question: Where do I retrieve payout data by sales date after requesting it?
  phrasing_ops: 2
  slug: toast-payout-by-sales-date-api
- baseURL: https://toast-api-server/era/v1
  baseurl_source: spec
  description: The analytics API endpoint for payout reporting data organized by settled date.
  name: Toast Payout by settled date API
  phrasing_intents:
  - id: postPayoutReportSettledDateSpecificTimeRange
    intent: Request payout data organized by settled date
    question: How do I request payouts grouped by the date funds settled?
  - id: getPayoutSettledDateReportingData
    intent: Fetch payout-by-settled-date report results
    question: Where do I retrieve payout data by settled date once it is ready?
  phrasing_ops: 2
  slug: toast-payout-by-settled-date-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Payout Reasons API from Toast — 2 operation(s) for payout reasons.
  name: Toast Payout Reasons API
  phrasing_intents:
  - id: payoutReasonsGuidGet
    intent: Look up one cash payout reason
    question: How do I see one recurring cash expense reason, like window washing?
  - id: payoutReasonsGet
    intent: List a restaurant's cash payout reasons
    question: Which recurring cash expenses are configured as payout reasons?
  phrasing_ops: 2
  slug: toast-payout-reasons-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Pre Modifier Groups API from Toast — 2 operation(s) for pre modifier groups.
  name: Toast Pre Modifier Groups API
  phrasing_intents:
  - id: preModifierGroupsGuidGet
    intent: Look up one pre-modifier group
    question: How do I see the details of one pre-modifier group?
  - id: preModifierGroupsGet
    intent: List a restaurant's pre-modifier groups
    question: Which pre-modifier groups are configured at a restaurant?
  phrasing_ops: 2
  slug: toast-pre-modifier-groups-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Pre Modifiers API from Toast — 2 operation(s) for pre modifiers.
  name: Toast Pre Modifiers API
  phrasing_intents:
  - id: preModifiersGuidGet
    intent: Look up one pre-modifier
    question: How do I see one pre-modifier, like extra or light?
  - id: preModifiersGet
    intent: List a restaurant's pre-modifiers
    question: Which pre-modifiers are configured at a restaurant?
  phrasing_ops: 2
  slug: toast-pre-modifiers-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Price Groups API from Toast — 2 operation(s) for price groups.
  name: Toast Price Groups API
  phrasing_intents:
  - id: priceGroupsGuidGet
    intent: Look up one menu price level
    question: How do I see one variable price level used for menu items?
  - id: priceGroupsGet
    intent: List a restaurant's menu price levels
    question: Which price levels are configured for menu items at a restaurant?
  phrasing_ops: 2
  slug: toast-price-groups-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Printers API from Toast — 2 operation(s) for printers.
  name: Toast Printers API
  phrasing_intents:
  - id: printersGuidGet
    intent: Look up one printer
    question: How do I see the configuration of one printer at a restaurant?
  - id: printersGet
    intent: List a restaurant's printers
    question: Which printer devices are configured at a restaurant?
  phrasing_ops: 2
  slug: toast-printers-api
- baseURL: https://toast-api-server/kitchen/v1
  baseurl_source: spec
  description: The Published API from Toast — 3 operation(s) for published.
  name: Toast Published API
  phrasing_intents:
  - id: prepStationsGet
    intent: List a restaurant's kitchen prep stations
    question: Which prep stations, like kitchen printers or KDS screens, receive orders at a restaurant?
  - id: prepStationsGuidGet
    intent: Look up one prep station
    question: How do I see the configuration of a single prep station?
  - id: getPackagingConfig
    intent: Get a restaurant's packaging configuration
    question: What packaging options, like utensils or bags, has a restaurant published?
  phrasing_ops: 3
  slug: toast-published-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Restaurant Services API from Toast — 2 operation(s) for restaurant services.
  name: Toast Restaurant Services API
  phrasing_intents:
  - id: restaurantServicesGuidGet
    intent: Look up one restaurant service period
    question: How do I see the details of one service period, like lunch?
  - id: restaurantServicesGet
    intent: List a restaurant's service periods
    question: Which service periods, such as lunch and dinner, does a restaurant offer?
  phrasing_ops: 2
  slug: toast-restaurant-services-api
- baseURL: https://toast-api-server/era/v1
  baseurl_source: spec
  description: The analytics API endpoint for providing information about restaurants in a management group.
  name: Toast Restaurants information API
  phrasing_intents:
  - id: getManagementGroupRestaurantsInformation
    intent: List restaurants in my management group
    question: Which restaurants are in my management group and are they activated?
  phrasing_ops: 1
  slug: toast-restaurants-information-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Revenue Centers API from Toast — 2 operation(s) for revenue centers.
  name: Toast Revenue Centers API
  phrasing_intents:
  - id: revenueCentersGuidGet
    intent: Look up one revenue center
    question: How do I see one revenue center used for income reporting?
  - id: revenueCentersGet
    intent: List a restaurant's revenue centers
    question: Which revenue centers split a restaurant's income for reporting?
  phrasing_ops: 2
  slug: toast-revenue-centers-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Sales Categories API from Toast — 2 operation(s) for sales categories.
  name: Toast Sales Categories API
  phrasing_intents:
  - id: salesCategoriesGuidGet
    intent: Look up one sales category
    question: How do I see one sales category, like alcohol, used to analyze purchases?
  - id: salesCategoriesGet
    intent: List a restaurant's sales categories
    question: Which sales categories, such as food and alcohol, does a restaurant use?
  phrasing_ops: 2
  slug: toast-sales-categories-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Service Areas API from Toast — 2 operation(s) for service areas.
  name: Toast Service Areas API
  phrasing_intents:
  - id: serviceAreasGuidGet
    intent: Look up one service area
    question: How do I see one physical service area, like the patio?
  - id: serviceAreasGet
    intent: List a restaurant's service areas
    question: Which service areas, such as dining room and patio, does a restaurant have?
  phrasing_ops: 2
  slug: toast-service-areas-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Service Charges API from Toast — 2 operation(s) for service charges.
  name: Toast Service Charges API
  phrasing_intents:
  - id: serviceChargesGuidGet
    intent: Look up one service charge type
    question: How do I see one fee type, like an automatic gratuity for large parties?
  - id: serviceChargesGet
    intent: List a restaurant's service charges
    question: Which fees and service charges are applied to sales at a restaurant?
  phrasing_ops: 2
  slug: toast-service-charges-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Tables API from Toast — 2 operation(s) for tables.
  name: Toast Tables API
  phrasing_intents:
  - id: tablesGuidGet
    intent: Look up one dining table
    question: How do I see the configuration of one dining table?
  - id: tablesGet
    intent: List a restaurant's dining tables
    question: Which dining tables are configured at a restaurant?
  phrasing_ops: 2
  slug: toast-tables-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Tax Rates API from Toast — 2 operation(s) for tax rates.
  name: Toast Tax Rates API
  phrasing_intents:
  - id: taxRatesGuidGet
    intent: Look up one tax rate
    question: How do I see the details of one tax rate applied to sales?
  - id: taxRatesGet
    intent: List a restaurant's tax rates
    question: Which tax rates are applied to sales at a restaurant?
  phrasing_ops: 2
  slug: toast-tax-rates-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Tip Withholding API from Toast — 1 operation(s) for tip withholding.
  name: Toast Tip Withholding API
  phrasing_intents:
  - id: tipWithholdingGet
    intent: Get the credit card tip withholding rate
    question: What percentage of credit card tips does a restaurant withhold from employees?
  phrasing_ops: 1
  slug: toast-tip-withholding-api
- baseURL: https://toast-api-server/config/v2
  baseurl_source: spec
  description: The Void Reasons API from Toast — 2 operation(s) for void reasons.
  name: Toast Void Reasons API
  phrasing_intents:
  - id: voidReasonsGuidGet
    intent: Look up one void reason
    question: How do I see one reason code used when voiding a sale?
  - id: voidReasonsGet
    intent: List a restaurant's void reasons
    question: Which reasons for voiding a sale are configured at a restaurant?
  phrasing_ops: 2
  slug: toast-void-reasons-api
- baseURL: https://toast-api-server/yourapiname/v1
  baseurl_source: spec
  description: The Yourendpointname API from Toast — 1 operation(s) for yourendpointname.
  name: Toast Yourendpointname API
  phrasing_intents:
  - id: yourendpointnamePost
    intent: Receive gift card transaction information
    question: What gift card transaction details does the platform send to a gift card provider's endpoint?
  phrasing_ops: 1
  slug: toast-yourendpointname-api
- description: 'Read-access to a restaurant''s configuration entities — menus, modifier groups, employees, jobs, dining options, service areas, revenue centers, sales categories, discounts, service charges, and table '
  name: Toast Configuration API
  slug: toast-configuration-api
- description: Next-generation read API for Toast menus, exposing the same menu / menu group / item / modifier / option model as V2 in a refreshed shape aligned with Toast's newer platform services.
  name: Toast Menus API (V3)
  slug: toast-menus-v3-api
- description: Read configuration that governs how orders flow through Toast — throttling, prep-time rules, surge controls, and order-management settings used by online-ordering and delivery integrations.
  name: Toast Order Management Configuration API
  slug: toast-order-management-config-api
- description: Returns whether a restaurant is currently accepting online orders, its expected prep times, and per-channel availability so ordering partners and delivery marketplaces can route demand appropriately.
  name: Toast Restaurant Availability API
  slug: toast-restaurant-availability-api
- description: Read tokenized credit-card information attached to orders for receipts, returns, and reconciliation. Toast Payments handles acceptance natively; this API exposes the resulting tokenized card records.
  name: Toast Credit Cards API
  slug: toast-credit-cards-api
- description: Records and retrieves cash entries — paid in, paid out, deposits, drawer counts — that flow into a restaurant's cash-management ledger and reconciliation reports.
  name: Toast Cash Management API
  slug: toast-cash-management-api
- description: Surfaces kitchen tickets, prep stations, ticket items, and ticket events to support kitchen-display integrations and out-of-band prep orchestration.
  name: Toast Kitchen API
  slug: toast-kitchen-api
- description: Read configuration about packaging — containers, lids, utensils, and packaging instructions — that off-premises orders and delivery handoff workflows must respect.
  name: Toast Packaging Configuration API
  slug: toast-packaging-configuration-api
- description: Analytics and reporting endpoints for Restaurant Management Suites Pro customers — sales, labor, productivity, and operational performance data exposed for BI integrations and warehouse pipelines.
  name: Toast Analytics API
  slug: toast-analytics-api
- description: Specification for integrating third-party gift-card programs with Toast — Toast calls the partner's endpoints to look up balances, authorize, redeem, and reload gift cards inline with a check.
  name: Toast Gift Cards Integration
  slug: toast-gift-cards-integration
- description: Specification for integrating third-party loyalty programs with Toast — discovery, lookup, accrual, and redemption callbacks that Toast invokes against partner endpoints during a transaction.
  name: Toast Loyalty Integration
  slug: toast-loyalty-integration
- description: Specification for integrating alternative tender types into Toast — callback endpoints partners implement so Toast can validate, authorize, and reconcile non-card forms of payment at checkout.
  name: Toast Tender Integration
  slug: toast-tender-integration
artifact_total: 434
asyncapis:
- description: ''
  name: Toast Webhooks
  slug: toast-webhooks
collections:
- collection_type: open
  name: Toast Authentication API
  slug: open-toast-authentication-api
- collection_type: open
  name: Toast Authentication ConnectedRestaurants API
  slug: open-toast-connectedrestaurants-api
- collection_type: open
  name: Toast Authentication Discounts API
  slug: open-toast-discounts-api
- collection_type: open
  name: Toast Authentication Employees API
  slug: open-toast-employees-api
- collection_type: open
  name: Toast Authentication Groups API
  slug: open-toast-groups-api
- collection_type: open
  name: Toast Authentication Jobs API
  slug: open-toast-jobs-api
- collection_type: open
  name: Toast Authentication Menus API
  slug: open-toast-menus-api
- collection_type: open
  name: Toast Authentication Metadata API
  slug: open-toast-metadata-api
- collection_type: open
  name: Toast Authentication Orders API
  slug: open-toast-orders-api
- collection_type: open
  name: Toast Authentication Payments API
  slug: open-toast-payments-api
- collection_type: open
  name: Toast Authentication Restaurants API
  slug: open-toast-restaurants-api
- collection_type: open
  name: Toast Authentication Shifts API
  slug: open-toast-shifts-api
- collection_type: open
  name: Toast Authentication Stock API
  slug: open-toast-stock-api
- collection_type: open
  name: Toast Authentication Time entries API
  slug: open-toast-time-entries-api
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://doc.toasttab.com/doc/devguide/apiIntegrationTypes.html
- group: other
  href: https://artifacts.apis.io/toast/capabilities/toast-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/toast-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/toast/overlays/toast-configuration-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/toast-configuration-overlay.yaml
- group: other
  href: https://artifacts.apis.io/toast/overlays/toast-analytics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/toast-analytics-overlay.yaml
- group: other
  href: https://artifacts.apis.io/toast/overlays/toast-cash-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/toast-cash-management-overlay.yaml
- group: other
  href: https://artifacts.apis.io/toast/overlays/toast-kitchen-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/toast-kitchen-overlay.yaml
- group: other
  href: https://artifacts.apis.io/toast/overlays/toast-credit-cards-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/toast-credit-cards-overlay.yaml
- group: other
  href: https://artifacts.apis.io/toast/overlays/toast-menus-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/toast-menus-v3-overlay.yaml
- group: other
  href: https://artifacts.apis.io/toast/overlays/toast-gift-cards-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/toast-gift-cards-overlay.yaml
- group: other
  href: https://artifacts.apis.io/toast/overlays/toast-loyalty-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/toast-loyalty-overlay.yaml
- group: other
  href: https://artifacts.apis.io/toast/overlays/toast-tender-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/toast-tender-overlay.yaml
- group: other
  href: https://artifacts.apis.io/toast/overlays/toast-device-details-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/toast-device-details-overlay.yaml
- group: other
  href: https://artifacts.apis.io/toast/overlays/toast-packaging-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/toast-packaging-overlay.yaml
- group: other
  href: https://artifacts.apis.io/toast/overlays/toast-ordermgmt-configuration-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/toast-ordermgmt-configuration-overlay.yaml
- group: other
  href: https://artifacts.apis.io/toast/overlays/toast-restaurant-availability-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/toast-restaurant-availability-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/toast/agentic-access/toast-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/toast-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/toast/security/toast-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/toast-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/toast/security/toast-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/toast-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/toast/authentication/toast-authentication.yml
  title: ''
  type: Authentication
  url: authentication/toast-authentication.yml
- group: auth
  href: https://artifacts.apis.io/toast/scopes/toast-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/toast-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/toast-inc
- group: company
  title: ''
  type: Website
  url: https://pos.toasttab.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.toasttab.com/doc/devguide/index.html
- group: start
  title: ''
  type: Portal
  url: https://doc.toasttab.com/openapi/
- group: start
  title: ''
  type: Signup
  url: https://developers.toasttab.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/toasttab
- group: design
  href: https://artifacts.apis.io/toast/rules/toast-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/toast-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/toast/vocabulary/toast-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/toast-vocabulary.yaml
- group: build
  href: https://artifacts.apis.io/toast/packages/toast-packages.yml
  title: ''
  type: Packages
  url: packages/toast-packages.yml
- group: agent
  href: https://artifacts.apis.io/toast/well-known/toast-well-known.yml
  title: ''
  type: WellKnownProbe
  url: well-known/toast-well-known.yml
- group: agent
  href: https://artifacts.apis.io/toast/mcp/toast-mcp.yml
  title: ''
  type: MCPCandidate
  url: mcp/toast-mcp.yml
- group: agent
  href: https://artifacts.apis.io/toast/llms/toast-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/toast-llms.txt
- group: design
  href: https://artifacts.apis.io/toast/conformance/toast-conformance.yml
  title: ''
  type: Conformance
  url: conformance/toast-conformance.yml
- group: design
  href: https://artifacts.apis.io/toast/errors/toast-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/toast-problem-types.yml
- group: build
  href: https://artifacts.apis.io/toast/errors/toast-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/toast-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/toast/lifecycle/toast-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/toast-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.toasttab.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://doc.toasttab.com/doc/devguide/apiDeprecatedApiFunctions.html
- group: auth
  href: https://artifacts.apis.io/toast/security/toast-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/toast-vulnerability-disclosure.yml
- group: start
  href: https://artifacts.apis.io/toast/sandbox/toast-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/toast-sandbox.yml
- group: design
  href: https://artifacts.apis.io/toast/conventions/toast-conventions.yml
  title: ''
  type: Conventions
  url: conventions/toast-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://api-updates.toasttab.com/
- group: design
  href: https://artifacts.apis.io/toast/data-model/toast-data-model.yml
  title: ''
  type: DataModel
  url: data-model/toast-data-model.yml
- group: design
  href: https://artifacts.apis.io/toast/asyncapi/toast-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/toast-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/toast/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/toast/plans/toast-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/toast-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/toast/rate-limits/toast-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/toast-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/toast/finops/toast-finops.yml
  title: ''
  type: FinOps
  url: finops/toast-finops.yml
- group: docs
  title: ''
  type: APIReference
  url: https://doc.toasttab.com/openapi/
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.toasttab.com/doc/devguide/portalHowToBuildAToastIntegration.html
- group: operate
  title: ''
  type: Support
  url: https://doc.toasttab.com/doc/devguide/apiSupport.html
- group: operate
  title: ''
  type: HelpCenter
  url: https://central.toasttab.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pos.toasttab.com/api-terms-of-use
- group: start
  title: ''
  type: DeveloperPortal
  url: https://doc.toasttab.com/openapi/
- group: build
  href: https://artifacts.apis.io/toast/examples/authentication-authentication-request-example.json
  title: ''
  type: Examples
  url: examples/authentication-authentication-request-example.json
- group: build
  href: https://artifacts.apis.io/toast/examples/authentication-authentication-response-example.json
  title: ''
  type: Examples
  url: examples/authentication-authentication-response-example.json
- group: build
  href: https://artifacts.apis.io/toast/examples/authentication-authentication-token-example.json
  title: ''
  type: Examples
  url: examples/authentication-authentication-token-example.json
- group: build
  href: https://artifacts.apis.io/toast/examples/labor-employee-example.json
  title: ''
  type: Examples
  url: examples/labor-employee-example.json
- group: build
  href: https://artifacts.apis.io/toast/examples/labor-external-reference-example.json
  title: ''
  type: Examples
  url: examples/labor-external-reference-example.json
- group: build
  href: https://artifacts.apis.io/toast/examples/labor-job-example.json
  title: ''
  type: Examples
  url: examples/labor-job-example.json
- group: build
  href: https://artifacts.apis.io/toast/examples/labor-job-wage-override-example.json
  title: ''
  type: Examples
  url: examples/labor-job-wage-override-example.json
- group: build
  href: https://artifacts.apis.io/toast/examples/labor-schedule-config-example.json
  title: ''
  type: Examples
  url: examples/labor-schedule-config-example.json
- group: build
  href: https://artifacts.apis.io/toast/examples/labor-shift-example.json
  title: ''
  type: Examples
  url: examples/labor-shift-example.json
- group: build
  href: https://artifacts.apis.io/toast/examples/labor-time-entry-break-example.json
  title: ''
  type: Examples
  url: examples/labor-time-entry-break-example.json
- group: build
  href: https://artifacts.apis.io/toast/examples/labor-time-entry-example.json
  title: ''
  type: Examples
  url: examples/labor-time-entry-example.json
- group: build
  href: https://artifacts.apis.io/toast/examples/labor-toast-reference-example.json
  title: ''
  type: Examples
  url: examples/labor-toast-reference-example.json
- group: docs
  href: https://artifacts.apis.io/toast/json-schema/authentication-authentication-request-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/authentication-authentication-request-schema.json
- group: docs
  href: https://artifacts.apis.io/toast/json-schema/authentication-authentication-response-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/authentication-authentication-response-schema.json
- group: docs
  href: https://artifacts.apis.io/toast/json-schema/authentication-authentication-token-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/authentication-authentication-token-schema.json
- group: docs
  href: https://artifacts.apis.io/toast/json-schema/labor-employee-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/labor-employee-schema.json
- group: docs
  href: https://artifacts.apis.io/toast/json-schema/labor-external-reference-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/labor-external-reference-schema.json
- group: docs
  href: https://artifacts.apis.io/toast/json-schema/labor-job-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/labor-job-schema.json
- group: docs
  href: https://artifacts.apis.io/toast/json-schema/labor-job-wage-override-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/labor-job-wage-override-schema.json
- group: docs
  href: https://artifacts.apis.io/toast/json-schema/labor-schedule-config-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/labor-schedule-config-schema.json
- group: docs
  href: https://artifacts.apis.io/toast/json-schema/labor-shift-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/labor-shift-schema.json
- group: docs
  href: https://artifacts.apis.io/toast/json-schema/labor-time-entry-break-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/labor-time-entry-break-schema.json
- group: docs
  href: https://artifacts.apis.io/toast/json-schema/labor-time-entry-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/labor-time-entry-schema.json
- group: docs
  href: https://artifacts.apis.io/toast/json-schema/labor-toast-reference-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/labor-toast-reference-schema.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.toasttab.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.toasttab.com/
created: '2025-02-08'
description: Toast is a restaurant technology platform providing cloud-based point-of-sale, payment processing, and business management tools for the restaurant industry. The Toast platform exposes REST APIs enabling technology partners to build integrations for orders, menus, labor management, restaurant configuration, inventory/stock management, authentication, and partner ecosystem access. APIs use OAuth 2.0 client credentials authentication with GUIDs for resource identification. Toast serves 120,000+ restaurant locations and offers both partner integrations (requiring formal partnership) and custom integrations via the developer portal.
examples:
- key_count: 3
  name: Authentication Authentication Request Example
  slug: authentication-authentication-request-example
- key_count: 1
  name: Authentication Authentication Response Example
  slug: authentication-authentication-response-example
- key_count: 6
  name: Authentication Authentication Token Example
  slug: authentication-authentication-token-example
- key_count: 15
  name: Labor Employee Example
  slug: labor-employee-example
- key_count: 1
  name: Labor External Reference Example
  slug: labor-external-reference-example
- key_count: 10
  name: Labor Job Example
  slug: labor-job-example
- key_count: 1
  name: Labor Job Wage Override Example
  slug: labor-job-wage-override-example
- key_count: 5
  name: Labor Schedule Config Example
  slug: labor-schedule-config-example
- key_count: 6
  name: Labor Shift Example
  slug: labor-shift-example
- key_count: 7
  name: Labor Time Entry Break Example
  slug: labor-time-entry-break-example
- key_count: 17
  name: Labor Time Entry Example
  slug: labor-time-entry-example
- key_count: 2
  name: Labor Toast Reference Example
  slug: labor-toast-reference-example
- key_count: 1
  name: Menus Alcohol Example
  slug: menus-alcohol-example
- key_count: 5
  name: Menus Allergen Item Example
  slug: menus-allergen-item-example
- key_count: 2
  name: Menus Availability Example
  slug: menus-availability-example
- key_count: 6
  name: Menus Catalog Product Example
  slug: menus-catalog-product-example
- key_count: 4
  name: Menus Catalog Product Option Example
  slug: menus-catalog-product-option-example
- key_count: 3
  name: Menus Catalog Product Option Value Example
  slug: menus-catalog-product-option-value-example
- key_count: 4
  name: Menus Catalog Product Variant Example
  slug: menus-catalog-product-variant-example
- key_count: 3
  name: Menus Catalog Product Variant Option Example
  slug: menus-catalog-product-variant-option-example
- key_count: 2
  name: Menus Item Tag Example
  slug: menus-item-tag-example
- key_count: 6
  name: Menus Menu Example
  slug: menus-menu-example
- key_count: 6
  name: Menus Menu Group Example
  slug: menus-menu-group-example
- key_count: 12
  name: Menus Menu Item Example
  slug: menus-menu-item-example
- key_count: 2
  name: Menus Metadata Example
  slug: menus-metadata-example
- key_count: 13
  name: Menus Modifier Group Example
  slug: menus-modifier-group-example
- key_count: 11
  name: Menus Modifier Option Example
  slug: menus-modifier-option-example
- key_count: 2
  name: Menus Modifier Option Tax Info Example
  slug: menus-modifier-option-tax-info-example
- key_count: 4
  name: Menus Portion Example
  slug: menus-portion-example
- key_count: 7
  name: Menus Pre Modifier Example
  slug: menus-pre-modifier-example
- key_count: 3
  name: Menus Pre Modifier Group Example
  slug: menus-pre-modifier-group-example
- key_count: 3
  name: Menus Pricing Rules Example
  slug: menus-pricing-rules-example
- key_count: 7
  name: Menus Restaurant Example
  slug: menus-restaurant-example
- key_count: 2
  name: Menus Sales Category Example
  slug: menus-sales-category-example
- key_count: 2
  name: Menus Schedule Example
  slug: menus-schedule-example
- key_count: 2
  name: Menus Sequence Price Example
  slug: menus-sequence-price-example
- key_count: 3
  name: Menus Size Sequence Pricing Rule Example
  slug: menus-size-sequence-pricing-rule-example
- key_count: 2
  name: Menus Time Range Example
  slug: menus-time-range-example
- key_count: 3
  name: Menus Time Specific Price Example
  slug: menus-time-specific-price-example
- key_count: 2
  name: Orders Applicable Discount Example
  slug: orders-applicable-discount-example
- key_count: 1
  name: Orders Applicable Discounts Request Example
  slug: orders-applicable-discounts-request-example
- key_count: 9
  name: Orders Applied Discount Example
  slug: orders-applied-discount-example
- key_count: 3
  name: Orders Applied Discount Reason Example
  slug: orders-applied-discount-reason-example
- key_count: 1
  name: Orders Applied Discount Trigger Example
  slug: orders-applied-discount-trigger-example
- key_count: 5
  name: Orders Applied Loyalty Info Example
  slug: orders-applied-loyalty-info-example
- key_count: 1
  name: Orders Applied Packaging Info Example
  slug: orders-applied-packaging-info-example
- key_count: 4
  name: Orders Applied Packaging Item Example
  slug: orders-applied-packaging-item-example
- key_count: 12
  name: Orders Applied Service Charge Example
  slug: orders-applied-service-charge-example
- key_count: 9
  name: Orders Applied Tax Rate Example
  slug: orders-applied-tax-rate-example
- key_count: 18
  name: Orders Check Example
  slug: orders-check-example
- key_count: 2
  name: Orders Config Reference Example
  slug: orders-config-reference-example
- key_count: 3
  name: Orders Curbside Pickup Info Example
  slug: orders-curbside-pickup-info-example
- key_count: 5
  name: Orders Customer Example
  slug: orders-customer-example
- key_count: 13
  name: Orders Delivery Info Example
  slug: orders-delivery-info-example
- key_count: 6
  name: Orders Delivery Service Info Example
  slug: orders-delivery-service-info-example
- key_count: 1
  name: Orders Device Example
  slug: orders-device-example
- key_count: 1
  name: Orders External Reference Example
  slug: orders-external-reference-example
- key_count: 2
  name: Orders Fulfillment Example
  slug: orders-fulfillment-example
- key_count: 2
  name: Orders Gift Card Info Example
  slug: orders-gift-card-info-example
- key_count: 2
  name: Orders Loyalty Details Example
  slug: orders-loyalty-details-example
- key_count: 2
  name: Orders Marketplace Facilitator Tax Info Example
  slug: orders-marketplace-facilitator-tax-info-example
- key_count: 14
  name: Orders Order Example
  slug: orders-order-example
- key_count: 1
  name: Orders Order Response Example
  slug: orders-order-response-example
- key_count: 13
  name: Orders Payment Example
  slug: orders-payment-example
- key_count: 2
  name: Orders Refund Details Example
  slug: orders-refund-details-example
- key_count: 4
  name: Orders Refund Example
  slug: orders-refund-example
- key_count: 13
  name: Orders Selection Example
  slug: orders-selection-example
- key_count: 2
  name: Orders Toast Reference Example
  slug: orders-toast-reference-example
- key_count: 1
  name: Orders Update Payment Request Example
  slug: orders-update-payment-request-example
- key_count: 2
  name: Orders Void Information Example
  slug: orders-void-information-example
- key_count: 10
  name: Partners Paginated Response Example
  slug: partners-paginated-response-example
- key_count: 12
  name: Partners Partner Access External Rep Example
  slug: partners-partner-access-external-rep-example
- key_count: 4
  name: Restaurants Day Schedule Example
  slug: restaurants-day-schedule-example
- key_count: 3
  name: Restaurants Delivery Example
  slug: restaurants-delivery-example
- key_count: 3
  name: Restaurants Delivery Payment Options Example
  slug: restaurants-delivery-payment-options-example
- key_count: 10
  name: Restaurants General Example
  slug: restaurants-general-example
- key_count: 2
  name: Restaurants Hours Example
  slug: restaurants-hours-example
- key_count: 4
  name: Restaurants Image Example
  slug: restaurants-image-example
- key_count: 11
  name: Restaurants Location Example
  slug: restaurants-location-example
- key_count: 4
  name: Restaurants Online Ordering Example
  slug: restaurants-online-ordering-example
- key_count: 1
  name: Restaurants Payment Options Example
  slug: restaurants-payment-options-example
- key_count: 8
  name: Restaurants Prep Times Example
  slug: restaurants-prep-times-example
- key_count: 1
  name: Restaurants Restaurant Example
  slug: restaurants-restaurant-example
- key_count: 1
  name: Restaurants Restaurant Info Example
  slug: restaurants-restaurant-info-example
- key_count: 1
  name: Restaurants Schedules Example
  slug: restaurants-schedules-example
- key_count: 2
  name: Restaurants Service Example
  slug: restaurants-service-example
- key_count: 4
  name: Restaurants Takeout Payment Options Example
  slug: restaurants-takeout-payment-options-example
- key_count: 6
  name: Restaurants Ur Ls Example
  slug: restaurants-ur-ls-example
- key_count: 7
  name: Restaurants Week Schedule Example
  slug: restaurants-week-schedule-example
- key_count: 3
  name: Stock Inventory Search Request Example
  slug: stock-inventory-search-request-example
- key_count: 6
  name: Stock Menu Item Inventory Example
  slug: stock-menu-item-inventory-example
features:
- description: Retrieve restaurant orders, checks, and payment data by GUID or bulk date queries.
  name: Orders API
- description: Full menu data retrieval including items, modifiers, prices, and availability.
  name: Menus API
- description: Employee CRUD operations, shift management, and payroll integration support.
  name: Labor Management API
- description: Location settings, payment options, and management group restaurant discovery.
  name: Restaurant Configuration API
- description: Inventory management for menu items and modifiers with stock level tracking.
  name: Stock and Inventory API
- description: Client credentials OAuth flow with GUID-scoped tokens for secure API access.
  name: OAuth 2.0 Authentication
- description: Formal partner program enabling multi-restaurant access and ecosystem integrations.
  name: Partner Integration Program
- description: Outbound integration webhooks for real-time event delivery (gift cards, loyalty, tender).
  name: Webhook Support
finops:
- has_sources: true
  method: derived
  name: Toast Finops
  primary_unit: ''
  service_category: ''
  slug: toast-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/toast.png
integrations:
- description: Third-party delivery platform integrated with Toast for order injection.
  name: DoorDash
- description: Delivery platform integration for menu sync and order management.
  name: UberEats
- description: Accounting integration for restaurant financial data via Toast reporting APIs.
  name: QuickBooks
- description: Payroll platform integration using Toast Labor API data.
  name: ADP
- description: Reservation system integration with Toast for guest management.
  name: OpenTable
json_schemas:
- name: AuthenticationRequest
  property_count: 3
  slug: authentication-authentication-request
- name: AuthenticationResponse
  property_count: 2
  slug: authentication-authentication-response
- name: AuthenticationToken
  property_count: 6
  slug: authentication-authentication-token
- name: Employee
  property_count: 15
  slug: labor-employee
- name: ExternalReference
  property_count: 1
  slug: labor-external-reference
- name: Job
  property_count: 10
  slug: labor-job
- name: JobWageOverride
  property_count: 2
  slug: labor-job-wage-override
- name: ScheduleConfig
  property_count: 5
  slug: labor-schedule-config
- name: Shift
  property_count: 9
  slug: labor-shift
- name: TimeEntryBreak
  property_count: 8
  slug: labor-time-entry-break
- name: TimeEntry
  property_count: 23
  slug: labor-time-entry
- name: ToastReference
  property_count: 2
  slug: labor-toast-reference
- name: Alcohol
  property_count: 1
  slug: menus-alcohol
- name: AllergenItem
  property_count: 5
  slug: menus-allergen-item
- name: Availability
  property_count: 2
  slug: menus-availability
- name: CatalogProductInfo
  property_count: 2
  slug: menus-catalog-product-info
- name: CatalogProductOption
  property_count: 4
  slug: menus-catalog-product-option
- name: CatalogProductOptionValue
  property_count: 3
  slug: menus-catalog-product-option-value
- name: CatalogProduct
  property_count: 6
  slug: menus-catalog-product
- name: CatalogProductVariantOption
  property_count: 4
  slug: menus-catalog-product-variant-option
- name: CatalogProductVariant
  property_count: 4
  slug: menus-catalog-product-variant
- name: ContentAdvisories
  property_count: 1
  slug: menus-content-advisories
- name: DimensionUnitOfMeasure
  property_count: 0
  slug: menus-dimension-unit-of-measure
- name: GuestCount
  property_count: 0
  slug: menus-guest-count
- name: Height
  property_count: 0
  slug: menus-height
- name: Image
  property_count: 0
  slug: menus-image
- name: Images
  property_count: 0
  slug: menus-images
- name: ItemTag
  property_count: 2
  slug: menus-item-tag
- name: Length
  property_count: 0
  slug: menus-length
- name: MasterId
  property_count: 0
  slug: menus-master-id
- name: MenuGroup
  property_count: 13
  slug: menus-menu-group
- name: MenuItem
  property_count: 42
  slug: menus-menu-item
- name: Menu
  property_count: 13
  slug: menus-menu
- name: Metadata
  property_count: 2
  slug: menus-metadata
- name: ModifierGroup
  property_count: 19
  slug: menus-modifier-group
- name: ModifierOption
  property_count: 40
  slug: menus-modifier-option
- name: ModifierOptionTaxInfo
  property_count: 2
  slug: menus-modifier-option-tax-info
- name: MultiLocationId
  property_count: 0
  slug: menus-multi-location-id
- name: Portion
  property_count: 4
  slug: menus-portion
- name: PosButtonColorDark
  property_count: 0
  slug: menus-pos-button-color-dark
- name: PosButtonColorLight
  property_count: 0
  slug: menus-pos-button-color-light
- name: PosName
  property_count: 0
  slug: menus-pos-name
- name: PreModifierGroup
  property_count: 4
  slug: menus-pre-modifier-group
- name: PreModifier
  property_count: 11
  slug: menus-pre-modifier
- name: PricingRules
  property_count: 3
  slug: menus-pricing-rules
- name: Restaurant
  property_count: 7
  slug: menus-restaurant
- name: SalesCategory
  property_count: 2
  slug: menus-sales-category
- name: Schedule
  property_count: 2
  slug: menus-schedule
- name: SequencePrice
  property_count: 2
  slug: menus-sequence-price
- name: SizeSequencePricingRule
  property_count: 3
  slug: menus-size-sequence-pricing-rule
- name: TimeRange
  property_count: 2
  slug: menus-time-range
- name: TimeSpecificPrice
  property_count: 3
  slug: menus-time-specific-price
- name: Visibility
  property_count: 0
  slug: menus-visibility
- name: Weight
  property_count: 0
  slug: menus-weight
- name: WeightUnitOfMeasure
  property_count: 0
  slug: menus-weight-unit-of-measure
- name: Width
  property_count: 0
  slug: menus-width
- name: ApplicableDiscount
  property_count: 3
  slug: orders-applicable-discount
- name: ApplicableDiscountsRequest
  property_count: 2
  slug: orders-applicable-discounts-request
- name: AppliedDiscountReason
  property_count: 4
  slug: orders-applied-discount-reason
- name: AppliedDiscount
  property_count: 13
  slug: orders-applied-discount
- name: AppliedDiscountTrigger
  property_count: 2
  slug: orders-applied-discount-trigger
- name: AppliedLoyaltyInfo
  property_count: 5
  slug: orders-applied-loyalty-info
- name: AppliedPackagingInfo
  property_count: 1
  slug: orders-applied-packaging-info
- name: AppliedPackagingItem
  property_count: 4
  slug: orders-applied-packaging-item
- name: AppliedServiceCharge
  property_count: 14
  slug: orders-applied-service-charge
- name: AppliedTaxRate
  property_count: 10
  slug: orders-applied-tax-rate
- name: Check
  property_count: 27
  slug: orders-check
- name: ConfigReference
  property_count: 2
  slug: orders-config-reference
- name: CurbsidePickupInfo
  property_count: 3
  slug: orders-curbside-pickup-info
- name: Customer
  property_count: 5
  slug: orders-customer
- name: DeliveryInfo
  property_count: 14
  slug: orders-delivery-info
- name: DeliveryServiceInfo
  property_count: 6
  slug: orders-delivery-service-info
- name: Device
  property_count: 1
  slug: orders-device
- name: ExternalReference
  property_count: 1
  slug: orders-external-reference
- name: Fulfillment
  property_count: 2
  slug: orders-fulfillment
- name: GiftCardInfo
  property_count: 2
  slug: orders-gift-card-info
- name: LoyaltyDetails
  property_count: 2
  slug: orders-loyalty-details
- name: MarketplaceFacilitatorTaxInfo
  property_count: 2
  slug: orders-marketplace-facilitator-tax-info
- name: OrderResponse
  property_count: 1
  slug: orders-order-response
- name: Order
  property_count: 36
  slug: orders-order
- name: Payment
  property_count: 27
  slug: orders-payment
- name: RefundDetails
  property_count: 3
  slug: orders-refund-details
- name: Refund
  property_count: 5
  slug: orders-refund
- name: RefundTransaction
  property_count: 0
  slug: orders-refund-transaction
- name: Selection
  property_count: 35
  slug: orders-selection
- name: ToastReference
  property_count: 2
  slug: orders-toast-reference
- name: UpdatePaymentRequest
  property_count: 1
  slug: orders-update-payment-request
- name: VoidInformation
  property_count: 5
  slug: orders-void-information
- name: PaginatedResponse
  property_count: 10
  slug: partners-paginated-response
- name: PartnerAccessExternalRep
  property_count: 12
  slug: partners-partner-access-external-rep
- name: DaySchedule
  property_count: 4
  slug: restaurants-day-schedule
- name: DeliveryPaymentOptions
  property_count: 3
  slug: restaurants-delivery-payment-options
- name: Delivery
  property_count: 3
  slug: restaurants-delivery
- name: General
  property_count: 10
  slug: restaurants-general
- name: Hours
  property_count: 2
  slug: restaurants-hours
- name: Image
  property_count: 4
  slug: restaurants-image
- name: Location
  property_count: 11
  slug: restaurants-location
- name: OnlineOrdering
  property_count: 5
  slug: restaurants-online-ordering
- name: PaymentOptions
  property_count: 3
  slug: restaurants-payment-options
- name: PrepTimes
  property_count: 8
  slug: restaurants-prep-times
- name: RestaurantInfo
  property_count: 8
  slug: restaurants-restaurant-info
- name: Restaurant
  property_count: 1
  slug: restaurants-restaurant
- name: Schedules
  property_count: 2
  slug: restaurants-schedules
- name: Service
  property_count: 3
  slug: restaurants-service
- name: TakeoutPaymentOptions
  property_count: 4
  slug: restaurants-takeout-payment-options
- name: URLs
  property_count: 6
  slug: restaurants-ur-ls
- name: WeekSchedule
  property_count: 7
  slug: restaurants-week-schedule
- name: InventorySearchRequest
  property_count: 3
  slug: stock-inventory-search-request
- name: MenuItemInventory
  property_count: 6
  slug: stock-menu-item-inventory
- name: ErrorMessage
  property_count: 9
  slug: toast-errormessage
- name: InventorySearchRequest
  property_count: 3
  slug: toast-inventorysearchrequest
- name: MenuItemInventory
  property_count: 6
  slug: toast-menuiteminventory
json_structures:
- name: Authentication Authentication Request Structure
  property_count: 3
  slug: authentication-authentication-request-structure
- name: Authentication Authentication Response Structure
  property_count: 2
  slug: authentication-authentication-response-structure
- name: Authentication Authentication Token Structure
  property_count: 6
  slug: authentication-authentication-token-structure
- name: Labor Employee Structure
  property_count: 0
  slug: labor-employee-structure
- name: Labor External Reference Structure
  property_count: 0
  slug: labor-external-reference-structure
- name: Labor Job Structure
  property_count: 0
  slug: labor-job-structure
- name: Labor Job Wage Override Structure
  property_count: 2
  slug: labor-job-wage-override-structure
- name: Labor Schedule Config Structure
  property_count: 5
  slug: labor-schedule-config-structure
- name: Labor Shift Structure
  property_count: 0
  slug: labor-shift-structure
- name: Labor Time Entry Break Structure
  property_count: 8
  slug: labor-time-entry-break-structure
- name: Labor Time Entry Structure
  property_count: 0
  slug: labor-time-entry-structure
- name: Labor Toast Reference Structure
  property_count: 2
  slug: labor-toast-reference-structure
- name: Menus Alcohol Structure
  property_count: 1
  slug: menus-alcohol-structure
- name: Menus Allergen Item Structure
  property_count: 5
  slug: menus-allergen-item-structure
- name: Menus Availability Structure
  property_count: 2
  slug: menus-availability-structure
- name: Menus Catalog Product Info Structure
  property_count: 2
  slug: menus-catalog-product-info-structure
- name: Menus Catalog Product Option Structure
  property_count: 4
  slug: menus-catalog-product-option-structure
- name: Menus Catalog Product Option Value Structure
  property_count: 3
  slug: menus-catalog-product-option-value-structure
- name: Menus Catalog Product Structure
  property_count: 6
  slug: menus-catalog-product-structure
- name: Menus Catalog Product Variant Option Structure
  property_count: 4
  slug: menus-catalog-product-variant-option-structure
- name: Menus Catalog Product Variant Structure
  property_count: 4
  slug: menus-catalog-product-variant-structure
- name: Menus Content Advisories Structure
  property_count: 1
  slug: menus-content-advisories-structure
- name: Menus Dimension Unit Of Measure Structure
  property_count: 0
  slug: menus-dimension-unit-of-measure-structure
- name: Menus Guest Count Structure
  property_count: 0
  slug: menus-guest-count-structure
- name: Menus Height Structure
  property_count: 0
  slug: menus-height-structure
- name: Menus Image Structure
  property_count: 0
  slug: menus-image-structure
- name: Menus Images Structure
  property_count: 0
  slug: menus-images-structure
- name: Menus Item Tag Structure
  property_count: 2
  slug: menus-item-tag-structure
- name: Menus Length Structure
  property_count: 0
  slug: menus-length-structure
- name: Menus Master Id Structure
  property_count: 0
  slug: menus-master-id-structure
- name: Menus Menu Group Structure
  property_count: 13
  slug: menus-menu-group-structure
- name: Menus Menu Item Structure
  property_count: 42
  slug: menus-menu-item-structure
- name: Menus Menu Structure
  property_count: 13
  slug: menus-menu-structure
- name: Menus Metadata Structure
  property_count: 2
  slug: menus-metadata-structure
- name: Menus Modifier Group Structure
  property_count: 19
  slug: menus-modifier-group-structure
- name: Menus Modifier Option Structure
  property_count: 40
  slug: menus-modifier-option-structure
- name: Menus Modifier Option Tax Info Structure
  property_count: 2
  slug: menus-modifier-option-tax-info-structure
- name: Menus Multi Location Id Structure
  property_count: 0
  slug: menus-multi-location-id-structure
- name: Menus Portion Structure
  property_count: 4
  slug: menus-portion-structure
- name: Menus Pos Button Color Dark Structure
  property_count: 0
  slug: menus-pos-button-color-dark-structure
- name: Menus Pos Button Color Light Structure
  property_count: 0
  slug: menus-pos-button-color-light-structure
- name: Menus Pos Name Structure
  property_count: 0
  slug: menus-pos-name-structure
- name: Menus Pre Modifier Group Structure
  property_count: 4
  slug: menus-pre-modifier-group-structure
- name: Menus Pre Modifier Structure
  property_count: 11
  slug: menus-pre-modifier-structure
- name: Menus Pricing Rules Structure
  property_count: 3
  slug: menus-pricing-rules-structure
- name: Menus Restaurant Structure
  property_count: 7
  slug: menus-restaurant-structure
- name: Menus Sales Category Structure
  property_count: 2
  slug: menus-sales-category-structure
- name: Menus Schedule Structure
  property_count: 2
  slug: menus-schedule-structure
- name: Menus Sequence Price Structure
  property_count: 2
  slug: menus-sequence-price-structure
- name: Menus Size Sequence Pricing Rule Structure
  property_count: 3
  slug: menus-size-sequence-pricing-rule-structure
- name: Menus Time Range Structure
  property_count: 2
  slug: menus-time-range-structure
- name: Menus Time Specific Price Structure
  property_count: 3
  slug: menus-time-specific-price-structure
- name: Menus Visibility Structure
  property_count: 0
  slug: menus-visibility-structure
- name: Menus Weight Structure
  property_count: 0
  slug: menus-weight-structure
- name: Menus Weight Unit Of Measure Structure
  property_count: 0
  slug: menus-weight-unit-of-measure-structure
- name: Menus Width Structure
  property_count: 0
  slug: menus-width-structure
- name: Orders Applicable Discount Structure
  property_count: 3
  slug: orders-applicable-discount-structure
- name: Orders Applicable Discounts Request Structure
  property_count: 2
  slug: orders-applicable-discounts-request-structure
- name: Orders Applied Discount Reason Structure
  property_count: 4
  slug: orders-applied-discount-reason-structure
- name: Orders Applied Discount Structure
  property_count: 0
  slug: orders-applied-discount-structure
- name: Orders Applied Discount Trigger Structure
  property_count: 2
  slug: orders-applied-discount-trigger-structure
- name: Orders Applied Loyalty Info Structure
  property_count: 0
  slug: orders-applied-loyalty-info-structure
- name: Orders Applied Packaging Info Structure
  property_count: 0
  slug: orders-applied-packaging-info-structure
- name: Orders Applied Packaging Item Structure
  property_count: 0
  slug: orders-applied-packaging-item-structure
- name: Orders Applied Service Charge Structure
  property_count: 0
  slug: orders-applied-service-charge-structure
- name: Orders Applied Tax Rate Structure
  property_count: 0
  slug: orders-applied-tax-rate-structure
- name: Orders Check Structure
  property_count: 0
  slug: orders-check-structure
- name: Orders Config Reference Structure
  property_count: 0
  slug: orders-config-reference-structure
- name: Orders Curbside Pickup Info Structure
  property_count: 0
  slug: orders-curbside-pickup-info-structure
- name: Orders Customer Structure
  property_count: 0
  slug: orders-customer-structure
- name: Orders Delivery Info Structure
  property_count: 14
  slug: orders-delivery-info-structure
- name: Orders Delivery Service Info Structure
  property_count: 0
  slug: orders-delivery-service-info-structure
- name: Orders Device Structure
  property_count: 1
  slug: orders-device-structure
- name: Orders External Reference Structure
  property_count: 0
  slug: orders-external-reference-structure
- name: Orders Fulfillment Structure
  property_count: 2
  slug: orders-fulfillment-structure
- name: Orders Gift Card Info Structure
  property_count: 0
  slug: orders-gift-card-info-structure
- name: Orders Loyalty Details Structure
  property_count: 2
  slug: orders-loyalty-details-structure
- name: Orders Marketplace Facilitator Tax Info Structure
  property_count: 2
  slug: orders-marketplace-facilitator-tax-info-structure
- name: Orders Order Response Structure
  property_count: 1
  slug: orders-order-response-structure
- name: Orders Order Structure
  property_count: 0
  slug: orders-order-structure
- name: Orders Payment Structure
  property_count: 0
  slug: orders-payment-structure
- name: Orders Refund Details Structure
  property_count: 3
  slug: orders-refund-details-structure
- name: Orders Refund Structure
  property_count: 5
  slug: orders-refund-structure
- name: Orders Refund Transaction Structure
  property_count: 0
  slug: orders-refund-transaction-structure
- name: Orders Selection Structure
  property_count: 0
  slug: orders-selection-structure
- name: Orders Toast Reference Structure
  property_count: 2
  slug: orders-toast-reference-structure
- name: Orders Update Payment Request Structure
  property_count: 1
  slug: orders-update-payment-request-structure
- name: Orders Void Information Structure
  property_count: 5
  slug: orders-void-information-structure
- name: Partners Paginated Response Structure
  property_count: 10
  slug: partners-paginated-response-structure
- name: Partners Partner Access External Rep Structure
  property_count: 12
  slug: partners-partner-access-external-rep-structure
- name: Restaurants Day Schedule Structure
  property_count: 4
  slug: restaurants-day-schedule-structure
- name: Restaurants Delivery Payment Options Structure
  property_count: 3
  slug: restaurants-delivery-payment-options-structure
- name: Restaurants Delivery Structure
  property_count: 3
  slug: restaurants-delivery-structure
- name: Restaurants General Structure
  property_count: 10
  slug: restaurants-general-structure
- name: Restaurants Hours Structure
  property_count: 2
  slug: restaurants-hours-structure
- name: Restaurants Image Structure
  property_count: 4
  slug: restaurants-image-structure
- name: Restaurants Location Structure
  property_count: 11
  slug: restaurants-location-structure
- name: Restaurants Online Ordering Structure
  property_count: 5
  slug: restaurants-online-ordering-structure
- name: Restaurants Payment Options Structure
  property_count: 3
  slug: restaurants-payment-options-structure
- name: Restaurants Prep Times Structure
  property_count: 8
  slug: restaurants-prep-times-structure
- name: Restaurants Restaurant Info Structure
  property_count: 8
  slug: restaurants-restaurant-info-structure
- name: Restaurants Restaurant Structure
  property_count: 1
  slug: restaurants-restaurant-structure
- name: Restaurants Schedules Structure
  property_count: 2
  slug: restaurants-schedules-structure
- name: Restaurants Service Structure
  property_count: 3
  slug: restaurants-service-structure
- name: Restaurants Takeout Payment Options Structure
  property_count: 4
  slug: restaurants-takeout-payment-options-structure
- name: Restaurants Ur Ls Structure
  property_count: 6
  slug: restaurants-ur-ls-structure
- name: Restaurants Week Schedule Structure
  property_count: 7
  slug: restaurants-week-schedule-structure
- name: Stock Inventory Search Request Structure
  property_count: 3
  slug: stock-inventory-search-request-structure
- name: Stock Menu Item Inventory Structure
  property_count: 6
  slug: stock-menu-item-inventory-structure
- name: Toast Structure
  property_count: 0
  slug: toast-structure
jsonld:
- class_count: 3
  name: Toast Authentication Context
  property_count: 11
  slug: toast-authentication-context
- class_count: 9
  name: Toast Labor Context
  property_count: 15
  slug: toast-labor-context
- class_count: 29
  name: Toast Menus Context
  property_count: 100
  slug: toast-menus-context
- class_count: 31
  name: Toast Orders Context
  property_count: 46
  slug: toast-orders-context
- class_count: 2
  name: Toast Partners Context
  property_count: 22
  slug: toast-partners-context
- class_count: 17
  name: Toast Restaurants Context
  property_count: 77
  slug: toast-restaurants-context
- class_count: 2
  name: Toast Stock Context
  property_count: 9
  slug: toast-stock-context
layout: provider
modified: '2026-08-27'
name: Toast
nav: Providers
network: true
overview: 'Toast publishes 66 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, ConnectedRestaurants API, Discounts API, and 63 more. Tagged areas include Food Service, Point-of-Sale, Restaurant, and Hospitality.


  The Toast catalog on APIs.io includes 1 event-driven AsyncAPI specification, 7 JSON-LD contexts, and 2 Spectral governance rulesets.


  Toast''s developer surface includes pricing, authentication, documentation, developer portal, signup flow, sandbox, changelog, and 73 more developer resources.'
plans:
- name: Toast Plans Pricing
  plan_count: 4
  slug: toast-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Toast Rate Limits
  slug: toast-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Toast — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: toast-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: Toast API Rules
  rule_count: 36
  severity_counts:
    error: 9
    hint: 0
    info: 14
    warn: 13
  slug: toast-spectral-rules
scopes:
- name: Toast Scopes
  scope_count: 28
  slug: toast-scopes
  summary_line: 28 scopes
score:
  band: exemplar
  composite: 68.5
  coverage:
    artifact_dirs: 34
    catalog_earned: 74.0
    catalog_earned_first_party: 24.0
    catalog_gap: 41.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 60.5
    contract_governance: 31.8
    contract_quality: 66.1
    developer_ergonomics: 63.7
    discoverability: 60.7
    operational_transparency: 92.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 69.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 3.7
      total: 54
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/toast/toast-2026-06-20T195427.png
security:
- kind: authentication
  name: Toast Authentication
  slug: toast-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Toast Domain Security
  slug: toast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Toast Vulnerability Disclosure
  slug: toast-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 4
skills:
- name: toast-labor-and-analytics
  slug: toast-labor-and-analytics
- name: toast-receive-webhooks
  slug: toast-receive-webhooks
- name: toast-submit-and-void-order
  slug: toast-submit-and-void-order
- name: toast-sync-menu-and-stock
  slug: toast-sync-menu-and-stock
slug: toast
tags:
- Food Service
- Point-of-Sale
- Restaurant
- Hospitality
use_cases:
- description: Connect third-party online ordering platforms to Toast POS for order injection and menu sync.
  name: Online Ordering Integration
- description: Sync Toast employee and shift data with payroll systems using the Labor API.
  name: Payroll and Labor Integration
- description: Pull order and payment data via bulk orders API for custom reporting and business intelligence.
  name: Reporting and Analytics
- description: Integrate restaurant inventory systems with Toast Stock API for real-time stock tracking.
  name: Inventory Management
- description: Build loyalty program and gift card integrations using Toast outbound webhook APIs.
  name: Loyalty and Gift Cards
- description: Partner integrations managing hundreds of restaurant locations via Partners API.
  name: Multi-Location Management
website: https://pos.toasttab.com/
---
