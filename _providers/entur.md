---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 390
  human_in_the_loop: 47
  name: Entur Agentic Access
  operation_count: 895
  slug: entur-agentic-access
  summary_line: 895 operations · 390 acting · 47 human-in-the-loop
api_count: 67
apis:
- description: Core journey planning service built on OpenTripPlanner, providing departure boards for individual stops and point-to-point journey planning for all public transport in Norway, including real-time info
  name: Journey Planner (GraphQL)
  slug: journey-planner-v3
- description: GraphQL service providing real-time positions and status for public transport vehicles across Norway, including location, delays, occupancy and journey data, with subscriptions for streaming. Open API
  name: Vehicle Positions (GraphQL)
  slug: vehicles-v2
- description: 'Aggregation service for shared mobility data in Norway: real-time information about shared bikes, e-scooters and other mobility services from multiple operators. Open GraphQL API; requests must includ'
  name: Mobility (GraphQL)
  slug: mobility-v2
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The admin/bucket-invalidation API from Entur — 2 operation(s) for admin/bucket-invalidation.
  name: Entur Admin/bucket Invalidation API
  slug: entur-admin-bucket-invalidation-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The admin/cache API from Entur — 8 operation(s) for admin/cache.
  name: Entur Admin/cache API
  slug: entur-admin-cache-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The amount-of-price-unit-products API from Entur — 3 operation(s) for amount-of-price-unit-products.
  name: Entur Amount Of Price Unit Products API
  slug: entur-amount-of-price-unit-products-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: OpenAPI specification endpoints.
  name: Entur API Documentation API
  slug: entur-api-documentation-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Api for verify credentials, generate and update password.
  name: Entur Authentication admin API
  slug: entur-authentication-admin-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Authentication endpoints for issuing OAuth tokens.
  name: Entur Authentication API
  slug: entur-authentication-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: A authtoken public key is used for validating a JSON Web Token (JWT), as defined in <a href="https://tools.ietf.org/html/rfc7519" target="_blank">RFC 7519</a>, included in the request from a BoB Clien
  name: Entur Authtoken Public Key API
  slug: entur-authtokenpublickey-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The Autocomplete API from Entur — 1 operation(s) for autocomplete.
  name: Entur Autocomplete API
  slug: entur-autocomplete-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The availability-conditions API from Entur — 2 operation(s) for availability-conditions.
  name: Entur Availability Conditions API
  slug: entur-availability-conditions-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The Booking API from Entur — 8 operation(s) for booking.
  name: Entur Booking API
  slug: entur-booking-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The capacities-controller API from Entur — 4 operation(s) for capacities-controller.
  name: Entur Capacities Controller API
  slug: entur-capacities-controller-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The capacity-controller-v-1 API from Entur — 1 operation(s) for capacity-controller-v-1.
  name: Entur Capacity Controller V 1 API
  slug: entur-capacity-controller-v-1-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The capped-discount-rights API from Entur — 3 operation(s) for capped-discount-rights.
  name: Entur Capped Discount Rights API
  slug: entur-capped-discount-rights-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Retrieve possible change options for an order.
  name: Entur Change Options API
  slug: entur-change-options-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The charging-moment-controller-v-1 API from Entur — 1 operation(s) for charging-moment-controller-v-1.
  name: Entur Charging Moment Controller V 1 API
  slug: entur-charging-moment-controller-v-1-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The charging-moments API from Entur — 2 operation(s) for charging-moments.
  name: Entur Charging Moments API
  slug: entur-charging-moments-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The charging-policies API from Entur — 1 operation(s) for charging-policies.
  name: Entur Charging Policies API
  slug: entur-charging-policies-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Updated lists of valid codes to use for different properties
  name: Entur Codes API
  slug: entur-codes-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Collection endpoints for retrieving resources and query results.
  name: Entur Collections API
  slug: entur-collections-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Administer companies and workplaces within the personnel ticket system
  name: Entur Companies API
  slug: entur-companies-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The companion-for-seat-controller API from Entur — 2 operation(s) for companion-for-seat-controller.
  name: Entur Companion For Seat Controller API
  slug: entur-companion-for-seat-controller-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The companion-profiles API from Entur — 3 operation(s) for companion-profiles.
  name: Entur Companion Profiles API
  slug: entur-companion-profiles-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Reduce the price of one or more orders to compensate customers without performing a full refund. Used when a price adjustment is sufficient instead of cancelling or refunding order lines.
  name: Entur Compensation API
  slug: entur-compensation-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Configurations directly configurable by partners. E.g. Webhooks.
  name: Entur Configurations API
  slug: entur-configurations-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Api for creating, fetching, modifying and deleting consents by admins
  name: Entur Consents admin API
  slug: entur-consents-admin-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Api for creating, fetching, modifying and deleting given consents by clients
  name: Entur Consents client API
  slug: entur-consents-client-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: API for displaying all consent info (Data warehouse API)
  name: Entur Consents DWH API
  slug: entur-consents-dwh-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: API for handling loyalty program contracts.
  name: Entur Contracts client API
  slug: entur-contracts-client-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Create and update credits. Create and execute credit transactions.
  name: Entur Credits API
  slug: entur-credits-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Api for creating, fetching and modifying customers account ids.
  name: Entur Customer accounts client API
  slug: entur-customer-accounts-client-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Find information about memberships and status a customer might have in programs.
  name: Entur Customers API
  slug: entur-customers-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Standard timetable dataset operations
  name: Entur Datasets API
  slug: entur-datasets-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The dated-service-journey-controller-beta API from Entur — 5 operation(s) for dated-service-journey-controller-beta.
  name: Entur Dated Service Journey Controller Beta API
  slug: entur-dated-service-journey-controller-beta-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The dated-service-journey-controller-v-1 API from Entur — 6 operation(s) for dated-service-journey-controller-v-1.
  name: Entur Dated Service Journey Controller V 1 API
  slug: entur-dated-service-journey-controller-v-1-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The day-types API from Entur — 3 operation(s) for day-types.
  name: Entur Day Types API
  slug: entur-day-types-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Endpoints deprecated in v2
  name: Entur Deprecated API
  slug: entur-deprecated-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Discovery endpoints for landing page, conformance, and API metadata.
  name: Entur Discovery API
  slug: entur-discovery-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The Distance API from Entur — 5 operation(s) for distance.
  name: Entur Distance API
  slug: entur-distance-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The distance-matrix-elements API from Entur — 4 operation(s) for distance-matrix-elements.
  name: Entur Distance Matrix Elements API
  slug: entur-distance-matrix-elements-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The distribution-channel-usages API from Entur — 1 operation(s) for distribution-channel-usages.
  name: Entur Distribution Channel Usages API
  slug: entur-distribution-channel-usages-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: A single domain name can be associated with each participant. The domain name is submitted to the metadata register in the participant registration process. It is used for dynamic key fetching via DNS
  name: Entur Domain Name API
  slug: entur-domainname-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: API for fetching employees in the personnel ticket system. An employee is the main entity of the pbsys system. They are hired by a Company and work at a WorkPlace. Employees are created from ImportedE
  name: Entur Employee API
  slug: entur-employee-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Import employees from an external system to be added to the personnel ticket system
  name: Entur Employee import API
  slug: entur-employee-import-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The entitlement-given API from Entur — 2 operation(s) for entitlement-given.
  name: Entur Entitlement Given API
  slug: entur-entitlement-given-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The entitlement-products API from Entur — 1 operation(s) for entitlement-products.
  name: Entur Entitlement Products API
  slug: entur-entitlement-products-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Manage EntitlementRequired instances. Defines what existing entitlement (e.g., a valid ticket) is required to purchase a product.
  name: Entur Entitlement Required API
  slug: entur-entitlement-required-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: API for handling personnel ticket entitlements.
  name: Entur Entitlements API
  slug: entur-entitlements-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The entitlements-required API from Entur — 2 operation(s) for entitlements-required.
  name: Entur Entitlements Required API
  slug: entur-entitlements-required-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Tag for example operations
  name: Entur Example API
  slug: entur-example-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The exchanging API from Entur — 4 operation(s) for exchanging.
  name: Entur Exchanging API
  slug: entur-exchanging-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The exchanging-possibilities API from Entur — 5 operation(s) for exchanging-possibilities.
  name: Entur Exchanging Possibilities API
  slug: entur-exchanging-possibilities-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The export API from Entur — 1 operation(s) for export.
  name: Entur Export API
  slug: entur-export-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Administration of family members. Each family member must be connected to an employee
  name: Entur Family members API
  slug: entur-family-members-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The fare-day-types API from Entur — 3 operation(s) for fare-day-types.
  name: Entur Fare Day Types API
  slug: entur-fare-day-types-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The fare-frames API from Entur — 4 operation(s) for fare-frames.
  name: Entur Fare Frames API
  slug: entur-fare-frames-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The fare-products API from Entur — 1 operation(s) for fare-products.
  name: Entur Fare Products API
  slug: entur-fare-products-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The fare-quota-factors API from Entur — 2 operation(s) for fare-quota-factors.
  name: Entur Fare Quota Factors API
  slug: entur-fare-quota-factors-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The fare-sections API from Entur — 2 operation(s) for fare-sections.
  name: Entur Fare Sections API
  slug: entur-fare-sections-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The fare-structure-element-usages API from Entur — 1 operation(s) for fare-structure-element-usages.
  name: Entur Fare Structure Element Usages API
  slug: entur-fare-structure-element-usages-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The fare-structure-elements API from Entur — 8 operation(s) for fare-structure-elements.
  name: Entur Fare Structure Elements API
  slug: entur-fare-structure-elements-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: A fare table holds the price(s) that a product references. A flat price is a table with a single selector-less entry; per-zone or per-distance pricing use the same shape with selector fields filled in
  name: Entur Fare table API
  slug: entur-fare-table-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The fare-table-usages API from Entur — 1 operation(s) for fare-table-usages.
  name: Entur Fare Table Usages API
  slug: entur-fare-table-usages-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The fare-tables API from Entur — 8 operation(s) for fare-tables.
  name: Entur Fare Tables API
  slug: entur-fare-tables-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The Fare Zone API from Entur — 3 operation(s) for fare zone.
  name: Entur Fare Zone API
  slug: entur-fare-zone-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Access fare zone definitions and boundaries used for ticket pricing calculations. Query by authority or specific zones.
  name: Entur Fare Zones API
  slug: entur-fare-zones-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Services related to fees on order.
  name: Entur Fees API
  slug: entur-fees-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Flexible transport dataset operations
  name: Entur Flexible Transport API
  slug: entur-flexible-transport-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The frequencies-of-use API from Entur — 3 operation(s) for frequencies-of-use.
  name: Entur Frequencies Of Use API
  slug: entur-frequencies-of-use-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The fulfilment-methods API from Entur — 2 operation(s) for fulfilment-methods.
  name: Entur Fulfilment Methods API
  slug: entur-fulfilment-methods-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The general-groups-of-entities API from Entur — 3 operation(s) for general-groups-of-entities.
  name: Entur General Groups Of Entities API
  slug: entur-general-groups-of-entities-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The generic-parameter-assignments API from Entur — 5 operation(s) for generic-parameter-assignments.
  name: Entur Generic Parameter Assignments API
  slug: entur-generic-parameter-assignments-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Query topographic places (municipalities, counties, countries) and tariff zones for geographic and administrative boundaries.
  name: Entur Geographic Areas API
  slug: entur-geographic-areas-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The geographical-intervals API from Entur — 6 operation(s) for geographical-intervals.
  name: Entur Geographical Intervals API
  slug: entur-geographical-intervals-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The geographical-structure-factors API from Entur — 2 operation(s) for geographical-structure-factors.
  name: Entur Geographical Structure Factors API
  slug: entur-geographical-structure-factors-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The geographical-structure-factors-usages API from Entur — 1 operation(s) for geographical-structure-factors-usages.
  name: Entur Geographical Structure Factors Usages API
  slug: entur-geographical-structure-factors-usages-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The group-of-distance-matrix-elements API from Entur — 2 operation(s) for group-of-distance-matrix-elements.
  name: Entur Group Of Distance Matrix Elements API
  slug: entur-group-of-distance-matrix-elements-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The group-tickets API from Entur — 4 operation(s) for group-tickets.
  name: Entur Group Tickets API
  slug: entur-group-tickets-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Access logical groupings of stop places and fare zones for organizational and operational purposes.
  name: Entur Groupings API
  slug: entur-groupings-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Create and manage settlements to be cleared by CLEOS
  name: Entur Incoming Settlements API
  slug: entur-incoming-settlements-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The interchangings API from Entur — 3 operation(s) for interchangings.
  name: Entur Interchangings API
  slug: entur-interchangings-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: A participant API implementation is made accessible to other participants through interface endpoints. A general description of each type of endpoint can be found in the <a href="https://samtrafiken.a
  name: Entur Interface Endpoint API
  slug: entur-interfaceendpoint-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The Inventory Admin API from Entur — 9 operation(s) for inventory admin.
  name: Entur Inventory Admin API
  slug: entur-inventory-admin-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The Inventory Client API from Entur — 7 operation(s) for inventory client.
  name: Entur Inventory Client API
  slug: entur-inventory-client-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: An issuer signature constraint lets a participant grant other participants (sales channels) permission to sign tickets issued by the participant. The purpose of issuer signature constraint is to contr
  name: Entur Issuer Signature Constraint API
  slug: entur-issuersignatureconstraint-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The Items API from Entur — 2 operation(s) for items.
  name: Entur Items API
  slug: entur-items-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The journey-patterns API from Entur — 3 operation(s) for journey-patterns.
  name: Entur Journey Patterns API
  slug: entur-journey-patterns-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The luggage-allowances API from Entur — 3 operation(s) for luggage-allowances.
  name: Entur Luggage Allowances API
  slug: entur-luggage-allowances-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Information and management of members in a program.
  name: Entur Members API
  slug: entur-members-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The meta-data API from Entur — 2 operation(s) for meta-data.
  name: Entur Meta Data API
  slug: entur-meta-data-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: An MTB public key is used for validating the issuer signature attached to an MTB. MTB keys are immutable. More information about MTB key management and algorithms can be found in <a href="https://bitb
  name: Entur Mtb Public Key API
  slug: entur-mtbpublickey-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The Netex API from Entur — 5 operation(s) for netex.
  name: Entur Netex API
  slug: entur-netex-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The Operator API from Entur — 1 operation(s) for operator.
  name: Entur Operator API
  slug: entur-operator-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Services related to order lines on order.
  name: Entur Order lines API
  slug: entur-order-lines-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Services for creating, updating, retrieving and deleting order notes.
  name: Entur Order Notes API
  slug: entur-order-notes-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Top level services for order
  name: Entur Orders API
  slug: entur-orders-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Discover, inspect and download generated data products
  name: Entur Outgoing Data Products API
  slug: entur-outgoing-data-products-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The parameter-usages API from Entur — 1 operation(s) for parameter-usages.
  name: Entur Parameter Usages API
  slug: entur-parameter-usages-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Find parking facilities associated with stop places, including capacity, pricing, and accessibility information.
  name: Entur Parking API
  slug: entur-parking-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Manage participant info for a participant
  name: Entur Participant Info API
  slug: entur-participantinfo-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Get all metadata for a certain participant.
  name: Entur Participant Metadata API
  slug: entur-participantmetadata-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Get all metadata for all registered participants.
  name: Entur Participant Metadata File API
  slug: entur-participantmetadatafile-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Create, send, and query receipts
  name: Entur Partner Receipts API
  slug: entur-partner-receipts-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Register and manage payment agreements for recurring billing.
  name: Entur Payment Agreements API
  slug: entur-payment-agreements-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Create, update, deactivate and retrieve payments. Create, initiate, capture, cancel, and retrieve payment transactions
  name: Entur Payments API
  slug: entur-payments-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Services for generating and sending pdf tickets.
  name: Entur PDF Tickets API
  slug: entur-pdf-tickets-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The penalty Policy API from Entur — 2 operation(s) for penalty policy.
  name: Entur penalty Policy API
  slug: entur-penalty-policy-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The penalty-policy-possibilities API from Entur — 5 operation(s) for penalty-policy-possibilities.
  name: Entur Penalty Policy Possibilities API
  slug: entur-penalty-policy-possibilities-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The period-tickets API from Entur — 1 operation(s) for period-tickets.
  name: Entur Period Tickets API
  slug: entur-period-tickets-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The Place API from Entur — 1 operation(s) for place.
  name: Entur Place API
  slug: entur-place-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The preassigned-products API from Entur — 7 operation(s) for preassigned-products.
  name: Entur Preassigned Products API
  slug: entur-preassigned-products-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Api for creating, fetching, modifying and deleting preferences a customer can have
  name: Entur Preferences admin API
  slug: entur-preferences-admin-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The preview-controller API from Entur — 5 operation(s) for preview-controller.
  name: Entur Preview Controller API
  slug: entur-preview-controller-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The pricing-parameter-set API from Entur — 1 operation(s) for pricing-parameter-set.
  name: Entur Pricing Parameter Set API
  slug: entur-pricing-parameter-set-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Get all personal information stored about a customer.
  name: Entur Privacy API
  slug: entur-privacy-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Process endpoints for creating and mutating packages, offers, and refunds.
  name: Entur Processes API
  slug: entur-processes-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The product-attribute-controller API from Entur — 2 operation(s) for product-attribute-controller.
  name: Entur Product Attribute Controller API
  slug: entur-product-attribute-controller-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The product-tree-explanations API from Entur — 2 operation(s) for product-tree-explanations.
  name: Entur Product Tree Explanations API
  slug: entur-product-tree-explanations-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The product-usages API from Entur — 1 operation(s) for product-usages.
  name: Entur Product Usages API
  slug: entur-product-usages-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: API for managing profile connections. A profile connection is a connection between two customer profiles, |where one profile is the main profile and the other profile is the connected profile. The mai
  name: Entur Profile connections API
  slug: entur-profile-connections-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Api for creating, fetching, modifying and deleting customers and related information.
  name: Entur Profiles client API
  slug: entur-profiles-client-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Get information about a program.
  name: Entur Programs API
  slug: entur-programs-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: A purchase window defines when a product can be purchased relative to the time of travel — for example up to 90 days before and at least one hour before departure, or only until the day before travel.
  name: Entur Purchase window API
  slug: entur-purchase-window-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The purchase-windows API from Entur — 4 operation(s) for purchase-windows.
  name: Entur Purchase Windows API
  slug: entur-purchase-windows-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The QR Code API from Entur — 1 operation(s) for qr code.
  name: Entur QR Code API
  slug: entur-qr-code-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Access detailed information about quays (platforms, boarding positions) and their relationship to stop places. Query by ID or retrieve version history.
  name: Entur Quays API
  slug: entur-quays-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Give access to the original NeTEx datasets delivered by data providers
  name: Entur Raw Timetable Data API
  slug: entur-raw-timetable-data-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The readiness-controller API from Entur — 1 operation(s) for readiness-controller.
  name: Entur Readiness Controller API
  slug: entur-readiness-controller-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The rebooking-controller API from Entur — 5 operation(s) for rebooking-controller.
  name: Entur Rebooking Controller API
  slug: entur-rebooking-controller-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The rebooking-v-1-controller API from Entur — 2 operation(s) for rebooking-v-1-controller.
  name: Entur Rebooking V 1 Controller API
  slug: entur-rebooking-v-1-controller-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Set up and manage stored payment methods.
  name: Entur Recurring Payments API
  slug: entur-recurring-payments-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Check refundable options and perform refunds on customer orders.
  name: Entur Refund API
  slug: entur-refund-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The refunding API from Entur — 4 operation(s) for refunding.
  name: Entur Refunding API
  slug: entur-refunding-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The refunding-possibilities API from Entur — 4 operation(s) for refunding-possibilities.
  name: Entur Refunding Possibilities API
  slug: entur-refunding-possibilities-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The replacing API from Entur — 2 operation(s) for replacing.
  name: Entur Replacing API
  slug: entur-replacing-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Api for getting tax and FIP reports
  name: Entur Reports API
  slug: entur-reports-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The reservation-controller API from Entur — 21 operation(s) for reservation-controller.
  name: Entur Reservation Controller API
  slug: entur-reservation-controller-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The reservation-controller-beta API from Entur — 7 operation(s) for reservation-controller-beta.
  name: Entur Reservation Controller Beta API
  slug: entur-reservation-controller-beta-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Services related to reservations on order.
  name: Entur Reservations API
  slug: entur-reservations-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Add regular products to order through offer.
  name: Entur Reserve Offers API
  slug: entur-reserve-offers-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Add external products to order.
  name: Entur Reserve Third Party Products API
  slug: entur-reserve-third-party-products-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The reserving API from Entur — 4 operation(s) for reserving.
  name: Entur Reserving API
  slug: entur-reserving-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The Reverse API from Entur — 1 operation(s) for reverse.
  name: Entur Reverse API
  slug: entur-reverse-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The reverting API from Entur — 2 operation(s) for reverting.
  name: Entur Reverting API
  slug: entur-reverting-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The round-trips API from Entur — 4 operation(s) for round-trips.
  name: Entur Round Trips API
  slug: entur-round-trips-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The roundings API from Entur — 3 operation(s) for roundings.
  name: Entur Roundings API
  slug: entur-roundings-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The sale-discount-rights API from Entur — 6 operation(s) for sale-discount-rights.
  name: Entur Sale Discount Rights API
  slug: entur-sale-discount-rights-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Fine-grained modification of sales packages. The client sends a full request body and has full control over the sales package content.
  name: Entur Sales package API
  slug: entur-sales-package-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Assign the supplement products to sales packages without knowledge of the full sales package structure.
  name: Entur Sales package assignment API
  slug: entur-sales-package-assignment-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The sales-packages API from Entur — 9 operation(s) for sales-packages.
  name: Entur Sales Packages API
  slug: entur-sales-packages-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Retrieve scheduled stop points used in route planning and timetables, and their mappings to physical stop places.
  name: Entur Scheduled Stop Points API
  slug: entur-scheduled-stop-points-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Endpoints that are available for generating offers by various means.
  name: Entur Search offers API
  slug: entur-search-offers-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The seat-capacity-controller API from Entur — 3 operation(s) for seat-capacity-controller.
  name: Entur Seat Capacity Controller API
  slug: entur-seat-capacity-controller-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The seat-capacity-controller-beta API from Entur — 2 operation(s) for seat-capacity-controller-beta.
  name: Entur Seat Capacity Controller Beta API
  slug: entur-seat-capacity-controller-beta-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The seat-display-controller API from Entur — 1 operation(s) for seat-display-controller.
  name: Entur Seat Display Controller API
  slug: entur-seat-display-controller-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The seat-type-controller API from Entur — 2 operation(s) for seat-type-controller.
  name: Entur Seat Type Controller API
  slug: entur-seat-type-controller-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The seating-offer-controller API from Entur — 9 operation(s) for seating-offer-controller.
  name: Entur Seating Offer Controller API
  slug: entur-seating-offer-controller-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The security-policy API from Entur — 4 operation(s) for security-policy.
  name: Entur Security Policy API
  slug: entur-security-policy-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The service-facility-sets API from Entur — 3 operation(s) for service-facility-sets.
  name: Entur Service Facility Sets API
  slug: entur-service-facility-sets-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The SharedMobilityInternal API from Entur — 2 operation(s) for sharedmobilityinternal.
  name: Entur Shared Mobility Internal API
  slug: entur-sharedmobilityinternal-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Opprette og slette skyssrettigheter for elever.
  name: Entur Skoleskyss API
  slug: entur-skoleskyss-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The sorting-controller API from Entur — 1 operation(s) for sorting-controller.
  name: Entur Sorting Controller API
  slug: entur-sorting-controller-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Query and retrieve stop place information including stations, terminals, bus stops, and ferry ports. Includes filtering by transport mode, location, and other attributes.
  name: Entur Stop Places API
  slug: entur-stop-places-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: 'A supplement product can be purchased in addition to a preassigned fare product. Examples of supplement product types include: - Seat reservation - Bicycle - Animal - Meal - Wi-fi - Luggage - Parking'
  name: Entur Supplement product API
  slug: entur-supplement-product-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: This API is deprecated and will be removed in future releases. Please migrate to the new API version. New api will support all supplementProductTypeEnums according to the netex-standard
  name: Entur Supplement Products API
  slug: entur-supplement-products-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The Support API from Entur — 1 operation(s) for support.
  name: Entur Support API
  slug: entur-support-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The swagger-controller API from Entur — 1 operation(s) for swagger-controller.
  name: Entur Swagger Controller API
  slug: entur-swagger-controller-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The tariffs API from Entur — 3 operation(s) for tariffs.
  name: Entur Tariffs API
  slug: entur-tariffs-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Api for creating, fetching, modifying and deleting temporary customer profiles.
  name: Entur Temporary profiles client API
  slug: entur-temporary-profiles-client-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The text-in-language API from Entur — 1 operation(s) for text-in-language.
  name: Entur Text In Language API
  slug: entur-text-in-language-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Get third party products for an order
  name: Entur Third Party Products by Order API
  slug: entur-third-party-products-by-order-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The third-party-reservation-controller API from Entur — 1 operation(s) for third-party-reservation-controller.
  name: Entur Third Party Reservation Controller API
  slug: entur-third-party-reservation-controller-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Services regarding ticket distribution group level.
  name: Entur Ticket Distribution Groups API
  slug: entur-ticket-distribution-groups-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Services regarding ticket distribution level.
  name: Entur Ticket Distributions API
  slug: entur-ticket-distributions-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: List generated ticket right holders
  name: Entur Ticket right holders API
  slug: entur-ticket-right-holders-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: List generated ticket rights
  name: Entur Ticket rights API
  slug: entur-ticket-rights-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The timebands API from Entur — 2 operation(s) for timebands.
  name: Entur Timebands API
  slug: entur-timebands-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Status of a timetable data delivery
  name: Entur Timetable Delivery Status API
  slug: entur-timetable-delivery-status-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Status of the latest import dates for timetable datasets by codespace
  name: Entur Timetable Import Info API
  slug: entur-timetable-import-info-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The transferabilities API from Entur — 2 operation(s) for transferabilities.
  name: Entur Transferabilities API
  slug: entur-transferabilities-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The transferability-possibilities API from Entur — 5 operation(s) for transferability-possibilities.
  name: Entur Transferability Possibilities API
  slug: entur-transferability-possibilities-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: API for retrieving contact info for all travellers on a given journey. Given a serviceJourneyId or, preferably, an originalServiceJourneyId, returns contact info for the travellers on this journey
  name: Entur Traveller information API
  slug: entur-traveller-information-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Services related to travellers on order.
  name: Entur Travellers API
  slug: entur-travellers-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The type-of-concession API from Entur — 4 operation(s) for type-of-concession.
  name: Entur Type Of Concession API
  slug: entur-type-of-concession-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The type-of-fare-products API from Entur — 4 operation(s) for type-of-fare-products.
  name: Entur Type Of Fare Products API
  slug: entur-type-of-fare-products-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The type-of-responsibility-role API from Entur — 2 operation(s) for type-of-responsibility-role.
  name: Entur Type Of Responsibility Role API
  slug: entur-type-of-responsibility-role-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The type-of-usage-parameters API from Entur — 3 operation(s) for type-of-usage-parameters.
  name: Entur Type Of Usage Parameters API
  slug: entur-type-of-usage-parameters-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Manage UsageValidityPeriod instances. Defines how long a product is valid after purchase or activation (e.g., single trip, 60 minutes, 30 days).
  name: Entur Usage Validity Period API
  slug: entur-usage-validity-period-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The usage-validity-periods API from Entur — 5 operation(s) for usage-validity-periods.
  name: Entur Usage Validity Periods API
  slug: entur-usage-validity-periods-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The user-profiles API from Entur — 4 operation(s) for user-profiles.
  name: Entur User Profiles API
  slug: entur-user-profiles-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The uvp-for-number-of-zones API from Entur — 4 operation(s) for uvp-for-number-of-zones.
  name: Entur Uvp For Number Of Zones API
  slug: entur-uvp-for-number-of-zones-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The valid-betweens API from Entur — 6 operation(s) for valid-betweens.
  name: Entur Valid Betweens API
  slug: entur-valid-betweens-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The validable-elements API from Entur — 6 operation(s) for validable-elements.
  name: Entur Validable Elements API
  slug: entur-validable-elements-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The validable-elements-usages API from Entur — 1 operation(s) for validable-elements-usages.
  name: Entur Validable Elements Usages API
  slug: entur-validable-elements-usages-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The vat-register API from Entur — 2 operation(s) for vat-register.
  name: Entur Vat Register API
  slug: entur-vat-register-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: Version management endpoints
  name: Entur Version API
  slug: entur-version-api
- baseURL: https://api.entur.io/cleos-reporting
  baseurl_source: declared
  description: The versions API from Entur — 5 operation(s) for versions.
  name: Entur Versions API
  slug: entur-versions-api
artifact_total: 331
asyncapis:
- description: ''
  name: Entur Webhooks
  slug: entur-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/capabilities/entur-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/entur-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/agentic-access/entur-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/entur-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/rate-limits/entur-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/entur-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/rules/entur-rules.yml
  title: ''
  type: Spectral
  url: rules/entur-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/rules/entur-api-guidelines-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/entur-api-guidelines-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/json-ld/entur-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/entur-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/vocabulary/entur-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/entur-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/asyncapi/entur-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/entur-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/data-model/entur-data-model.yml
  title: ''
  type: DataModel
  url: data-model/entur-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/conventions/entur-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/entur-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/conventions/entur-conventions.yml
  title: ''
  type: Conventions
  url: conventions/entur-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/sandbox/entur-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/entur-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/security/entur-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/entur-vulnerability-disclosure.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/lifecycle/entur-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/entur-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/lifecycle/entur-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/entur-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/errors/entur-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/entur-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/conformance/entur-conformance.yml
  title: ''
  type: Conformance
  url: conformance/entur-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/overlays/entur-clearing-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/entur-clearing-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/llms/entur-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/entur-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/mcp/entur-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/entur-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/mcp/entur-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/entur-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/well-known/entur-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/entur-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/well-known/entur-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/entur-dev-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/well-known/entur-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/entur-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/hosts/entur-hosts.yml
  title: ''
  type: Hosts
  url: hosts/entur-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/vendors/entur-vendors.yml
  title: ''
  type: Vendors
  url: vendors/entur-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/packages/entur-packages.yml
  title: ''
  type: SDKs
  url: packages/entur-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/packages/entur-packages.yml
  title: ''
  type: Packages
  url: packages/entur-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/scopes/entur-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/entur-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/authentication/entur-authentication.yml
  title: ''
  type: Authentication
  url: authentication/entur-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/security/entur-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/entur-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/security/entur-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/entur-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://entur.no/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/entur/api-guidelines/blob/f92bec1065e08092b8c5ee62677ff9345ed1a174/.spectral.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.entur.no/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.entur.no/guides
- group: docs
  title: ''
  type: APIReference
  url: https://developer.entur.no/apis/open
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.entur.no/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developer.entur.no/docs/authentication
- group: other
  title: ''
  type: OpenData
  url: https://developer.entur.no/open-data
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/entur
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.entur.no/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://om.entur.no/personvern
- group: operate
  title: ''
  type: Support
  url: https://om.entur.no/kontakt-oss
- group: company
  title: ''
  type: Blog
  url: https://om.entur.no/aktuelle-saker
- group: company
  title: ''
  type: About
  url: https://om.entur.no/om-entur
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/entur-as/
created: '2026-10-09'
description: Entur AS is a Norwegian state-owned technology company ("et statlig eid teknologiselskap") that works to make it easier to choose public transport across Norway. It runs the national journey planner at entur.no and its app, sells tickets, and operates the national data platform for public transport. Through Entur for Developers it publishes open services (journey planner, geocoder, real-time vehicle and mobility data) and open data for free, plus partner services that require authentication.
image: https://entur.no/static/favicon/apple-touch-icon.png
json_schemas:
- name: AddSupplementProductsRequest
  property_count: 2
  slug: entur-add-supplement-products-request
- name: AmountOfPriceUnitProduct
  property_count: 31
  slug: entur-amount-of-price-unit-product
- name: Asset
  property_count: 14
  slug: entur-asset
- name: Booking
  property_count: 12
  slug: entur-booking-response
- name: CappedDiscountRight
  property_count: 31
  slug: entur-capped-discount-right
- name: ChangeOrderLinesRequest
  property_count: 3
  slug: entur-change-order-lines-request
- name: collectionInfo
  property_count: 13
  slug: entur-collection-info
- name: CompensationOperationRequest
  property_count: 3
  slug: entur-compensation-operation-request
- name: CompensationRequest
  property_count: 1
  slug: entur-compensation-request
- name: ConsentBaseRequest
  property_count: 7
  slug: entur-consent-base-request
- name: ConsentBaseResponse
  property_count: 10
  slug: entur-consent-base-response
- name: ConsentCrmResponse
  property_count: 15
  slug: entur-consent-crm-response
- name: ContractResponse
  property_count: 21
  slug: entur-contract-response
- name: CoordinateDistanceResponse
  property_count: 5
  slug: entur-coordinate-distance-response
- name: Credit
  property_count: 10
  slug: entur-credit-response
- name: CurrentLevelSummaryQuery
  property_count: 5
  slug: entur-current-level-summary-query
- name: CurrentLevelSummary
  property_count: 7
  slug: entur-current-level-summary
- name: customerInput
  property_count: 14
  slug: entur-customer-input
- name: CustomerMembership
  property_count: 4
  slug: entur-customer-membership
- name: CustomerPostRequest
  property_count: 22
  slug: entur-customer-post-request
- name: CustomerPutRequest
  property_count: 20
  slug: entur-customer-put-request
- name: CustomerResponse
  property_count: 44
  slug: entur-customer-response
- name: DeleteSkoleskyssResponse
  property_count: 3
  slug: entur-delete-skoleskyss-response
- name: DistanceCalculationResponse
  property_count: 5
  slug: entur-distance-calculation-response
- name: DryRunRefundResponse
  property_count: 4
  slug: entur-dry-run-refund-response
- name: EcardOwnershipResponse
  property_count: 13
  slug: entur-ecard-ownership-response
- name: EmployeeResponse
  property_count: 43
  slug: entur-employee-response
- name: EntitlementResponse
  property_count: 16
  slug: entur-entitlement-response
- name: Exchanging
  property_count: 31
  slug: entur-exchanging
- name: extendExpiryTimeInput
  property_count: 3
  slug: entur-extend-expiry-time-input
- name: FareTableRequest
  property_count: 7
  slug: entur-fare-table-request
- name: FareTableResponse
  property_count: 10
  slug: entur-fare-table-response
- name: FareZoneDistanceRequest
  property_count: 6
  slug: entur-fare-zone-distance-request
- name: FareZoneDistanceResponse
  property_count: 6
  slug: entur-fare-zone-distance-response
- name: FeeRequest
  property_count: 7
  slug: entur-fee-request
- name: GenericParameterAssignment
  property_count: 33
  slug: entur-generic-parameter-assignment
- name: GivenConsentBulkUpdateRequest
  property_count: 12
  slug: entur-given-consent-bulk-update-request
- name: GivenConsentRequest
  property_count: 12
  slug: entur-given-consent-request
- name: GivenConsentResponse
  property_count: 18
  slug: entur-given-consent-response
- name: ImportedEmployeeMergePatchRequest
  property_count: 22
  slug: entur-imported-employee-merge-patch-request
- name: ImportedEmployeeRequest
  property_count: 33
  slug: entur-imported-employee-request
- name: ImportedEmployeeResponse
  property_count: 37
  slug: entur-imported-employee-response
- name: MapStringString
  property_count: 2
  slug: entur-map-string-string
- name: MultiStockResponse
  property_count: 4
  slug: entur-multi-stock-response
- name: NetexImport
  property_count: 2
  slug: entur-netex-import
- name: Notification
  property_count: 2
  slug: entur-notification
- name: OneStopBookingEvent
  property_count: 4
  slug: entur-one-stop-booking-event
- name: OneStopBooking
  property_count: 9
  slug: entur-one-stop-booking
- name: OrderCreateRequest
  property_count: 5
  slug: entur-order-create-request
- name: OrderLineIdsAndReservationIds
  property_count: 4
  slug: entur-order-line-ids-and-reservation-ids
- name: OrderLineRequest
  property_count: 18
  slug: entur-order-line-request
- name: OrderLine
  property_count: 0
  slug: entur-order-line
- name: OrderNoteRequest
  property_count: 6
  slug: entur-order-note-request
- name: OrderNoteResponse
  property_count: 9
  slug: entur-order-note-response
- name: OrderRequest
  property_count: 4
  slug: entur-order-request
- name: Order
  property_count: 0
  slug: entur-order
- name: PageOfOrderNoteResponse
  property_count: 3
  slug: entur-page-of-order-note-response
- name: PartnerDatasetDownloadJobDto
  property_count: 10
  slug: entur-partner-dataset-download-job-dto
- name: PartnerDatasetRpt
  property_count: 19
  slug: entur-partner-dataset-rpt
- name: PartnerSettlementImportDto
  property_count: 11
  slug: entur-partner-settlement-import-dto
- name: PartnerSettlementImportResponseDto
  property_count: 10
  slug: entur-partner-settlement-import-response-dto
- name: Payment
  property_count: 12
  slug: entur-payment-response
- name: PointPeriod
  property_count: 4
  slug: entur-point-period
- name: PostSkoleskyssRequest
  property_count: 7
  slug: entur-post-skoleskyss-request
- name: PostSkoleskyssResponse
  property_count: 3
  slug: entur-post-skoleskyss-response
- name: Program
  property_count: 12
  slug: entur-program
- name: PurchaseWindowListResponse
  property_count: 0
  slug: entur-purchase-window-list-response
- name: PurchaseWindowRequest
  property_count: 12
  slug: entur-purchase-window-request
- name: PurchaseWindowResponse
  property_count: 15
  slug: entur-purchase-window-response
- name: QuotaConfigurationResponseV1
  property_count: 9
  slug: entur-quota-configuration-response-v1
- name: QuotaConfiguration
  property_count: 8
  slug: entur-quota-configuration
- name: QuotaRequestV1
  property_count: 8
  slug: entur-quota-request-v1
- name: QuotaResponseV1
  property_count: 9
  slug: entur-quota-response-v1
- name: RebookedReservationResponse
  property_count: 17
  slug: entur-rebooked-reservation-response
- name: RebookedReservationResponseV1
  property_count: 18
  slug: entur-rebooked-reservation-response-v1
- name: ReceiptTypeResponse
  property_count: 1
  slug: entur-receipt-type-response
- name: RefundOptionResponse
  property_count: 3
  slug: entur-refund-option-response
- name: RefundRequest
  property_count: 3
  slug: entur-refund-request
- name: RefundResponse
  property_count: 5
  slug: entur-refund-response
- name: ReservationLineResponse
  property_count: 8
  slug: entur-reservation-line-response
- name: ReservationResponse
  property_count: 16
  slug: entur-reservation-response
- name: ReservationResponseV1
  property_count: 9
  slug: entur-reservation-response-v1
- name: ReserveOffersRequest
  property_count: 2
  slug: entur-reserve-offers-request
- name: ReserveSpecificSeatsRequest
  property_count: 1
  slug: entur-reserve-specific-seats-request
- name: ReserveThirdPartyProductsRequest
  property_count: 2
  slug: entur-reserve-third-party-products-request
- name: ReserveThirdPartyProductsResponse
  property_count: 2
  slug: entur-reserve-third-party-products-response
- name: Result
  property_count: 4
  slug: entur-result
- name: SaleDiscountRight
  property_count: 30
  slug: entur-sale-discount-right
- name: SalesOfferPackageAssignmentRequest
  property_count: 3
  slug: entur-sales-offer-package-assignment-request
- name: SalesOfferPackagePublicationResponse
  property_count: 7
  slug: entur-sales-offer-package-publication-response
- name: SalesOfferPackageResponse
  property_count: 10
  slug: entur-sales-offer-package-response
- name: SearchAuthorityRequest
  property_count: 3
  slug: entur-search-authority-request
- name: SearchGeoLocationRequest
  property_count: 9
  slug: entur-search-geo-location-request
- name: searchOfferInput
  property_count: 9
  slug: entur-search-offer-input
- name: SearchResponse
  property_count: 6
  slug: entur-search-response
- name: SearchTripPatternRequest
  property_count: 5
  slug: entur-search-trip-pattern-request
- name: SeatingOfferDebugResponse
  property_count: 18
  slug: entur-seating-offer-debug-response
- name: SeatingOfferResponse
  property_count: 15
  slug: entur-seating-offer-response
- name: SendReceiptRequest
  property_count: 6
  slug: entur-send-receipt-request
- name: SeqCancelSeatRequest
  property_count: 2
  slug: entur-seq-cancel-seat-request
- name: SeqCompanionForSeatResponse
  property_count: 2
  slug: entur-seq-companion-for-seat-response
- name: SeqJourneyQuery
  property_count: 2
  slug: entur-seq-journey-query
- name: SeqProductAttributeRequest
  property_count: 2
  slug: entur-seq-product-attribute-request
- name: subscriber
  property_count: 3
  slug: entur-subscriber
- name: SupplementProductRequest
  property_count: 16
  slug: entur-supplement-product-request
- name: SupplementProductResponse
  property_count: 20
  slug: entur-supplement-product-response
- name: SupplementProduct
  property_count: 31
  slug: entur-supplement-product
- name: SupportRequest
  property_count: 7
  slug: entur-support-request
- name: TemporaryCustomerPostRequest
  property_count: 13
  slug: entur-temporary-customer-post-request
- name: TemporaryCustomerResponse
  property_count: 31
  slug: entur-temporary-customer-response
- name: TerminalRequest
  property_count: 9
  slug: entur-terminal-request
- name: TransactionByOrder
  property_count: 13
  slug: entur-transaction-by-order
- name: TransactionImportRequest
  property_count: 9
  slug: entur-transaction-import-request
- name: TransactionRequest
  property_count: 10
  slug: entur-transaction-request
- name: Transaction
  property_count: 17
  slug: entur-transaction-response
- name: updateTravellerInput
  property_count: 6
  slug: entur-update-traveller-input
- name: UserReceiptResponse
  property_count: 1
  slug: entur-user-receipt-response
- name: VersionRequest
  property_count: 4
  slug: entur-version-request
- name: VersionResponse
  property_count: 8
  slug: entur-version-response
- name: ZonalStopPlaceDistanceRequest
  property_count: 5
  slug: entur-zonal-stop-place-distance-request
jsonld:
- class_count: 120
  name: Entur Context
  property_count: 304
  slug: entur-context
layout: provider
mcp_servers:
- description: Entur publishes, in its own GitHub org, a Java/Spring AI MCP server described as a "poc mcp using journey-planner and geocoder apis". It wraps the Journey Planner v3 (OpenTripPlanner transmodel GraphQ
  name: Entur OpenTripPlanner MCP (proof of concept)
  slug: entur-opentripplanner-mcp-proof-of-concept
modified: '2026-10-09'
name: Entur
nav: Providers
network: true
overview: 'Entur publishes 199 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin/bucket Invalidation API, Admin/cache API, Amount Of Price Unit Products API, and 196 more. Tagged areas include Company, Public Transport, Journey Planning, Mobility, and Open Data.


  The Entur catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Entur''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 41 more developer resources.'
plans:
- name: Entur Plans Pricing
  plan_count: 0
  slug: entur-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 9
  name: Entur Rate Limits
  slug: entur-rate-limits
rules:
- authorship: provider
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Entur — api guidelines rules
  rule_count: 48
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 14
  slug: entur-api-guidelines-spectral-rules
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Entur API Rules
  rule_count: 13
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 5
  slug: entur-rules
scopes:
- name: Entur Scopes
  scope_count: 1
  slug: entur-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 69.6
  coverage:
    artifact_dirs: 31
    catalog_earned: 91.3
    catalog_earned_first_party: 30.0
    catalog_gap: 23.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.1
  facets:
    access_clarity: 21.1
    contract_governance: 76.5
    contract_quality: 74.6
    developer_ergonomics: 73.2
    discoverability: 80.0
    operational_transparency: 63.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - norway
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 65.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 95.4
      derived: 0
      marker_coverage: 0.0
      total: 196
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 40.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/entur/refs/heads/main/screenshots/entur-2026-10-11T104224.png
security:
- kind: authentication
  name: Entur Authentication
  slug: entur-authentication
  summary_line: apiKey/http/oauth2 · 6 schemes
- kind: domain-security
  name: Entur Domain Security
  slug: entur-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Entur Vulnerability Disclosure
  slug: entur-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: entur
tags:
- Company
- Public Transport
- Journey Planning
- Mobility
- Open Data
- Norway
- Transit
- GraphQL
website: https://entur.no/
---
