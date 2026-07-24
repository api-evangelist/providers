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
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 53.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Deribit Agentic Access
  operation_count: 351
  slug: deribit-agentic-access
  summary_line: 351 operations
api_count: 19
apis:
- description: JSON-RPC over WebSocket interface for real-time bidirectional communication with the Deribit exchange. Recommended for most use cases, supporting real-time market data subscriptions, trading operation
  name: Deribit WebSocket API
  slug: deribit-websocket-api
- description: Financial Information eXchange protocol interface for institutional trading on Deribit. Designed for professional trading firms requiring low-latency order entry and execution reports using the indust
  name: Deribit FIX API
  slug: deribit-fix-api
- description: The Account Management API from Deribit — 37 operation(s) for account management.
  name: Deribit Account Management API
  slug: deribit-account-management-api
- description: The Authentication API from Deribit — 4 operation(s) for authentication.
  name: Deribit Authentication API
  slug: deribit-authentication-api
- description: The Block RFQ API from Deribit — 13 operation(s) for block rfq.
  name: Deribit Block RFQ API
  slug: deribit-block-rfq-api
- description: The Block Trade API from Deribit — 11 operation(s) for block trade.
  name: Deribit Block Trade API
  slug: deribit-block-trade-api
- description: The Combo Books API from Deribit — 5 operation(s) for combo books.
  name: Deribit Combo Books API
  slug: deribit-combo-books-api
- description: The Mark Price API from Deribit — 1 operation(s) for mark price.
  name: Deribit Mark Price API
  slug: deribit-mark-price-api
- description: The Market Data API from Deribit — 31 operation(s) for market data.
  name: Deribit Market Data API
  slug: deribit-market-data-api
- description: The Matching Engine API from Deribit — 23 operation(s) for matching engine.
  name: Deribit Matching Engine API
  slug: deribit-matching-engine-api
- description: Endpoints that operate on the authenticated portfolio.
  name: Deribit Portfolio Management API
  slug: deribit-portfolio-management-api
- description: <p>Private methods require authentication. All requests must include a valid OAuth2 token.</p> <p>A token can be requested using the <a href="#public-auth">/public/auth</a> method.</p> <p>When using t
  name: Deribit Private API
  slug: deribit-private-api
- description: Public methods can be used without authentication.
  name: Deribit Public API
  slug: deribit-public-api
- description: The Session Management API from Deribit — 5 operation(s) for session management.
  name: Deribit Session Management API
  slug: deribit-session-management-api
- description: Subscription works as [notifications](#notifications), so users will automatically (after subscribing) receive messages from the server. Overview for each channel response format is described in [subs
  name: Deribit Subscription Management API
  slug: deribit-subscription-management-api
- description: The Supporting API from Deribit — 4 operation(s) for supporting.
  name: Deribit Supporting API
  slug: deribit-supporting-api
- description: The Trading API from Deribit — 38 operation(s) for trading.
  name: Deribit Trading API
  slug: deribit-trading-api
- description: The Wallet API from Deribit — 21 operation(s) for wallet.
  name: Deribit Wallet API
  slug: deribit-wallet-api
- description: Can only be used over websockets.
  name: Deribit WebSocket Only API
  slug: deribit-websocket-only-api
artifact_total: 594
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/deribit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deribit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/deribit-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://insights.deribit.com/
- group: start
  title: ''
  type: Portal
  url: https://insights.deribit.com/dev-hub/
- group: other
  title: ''
  type: ExchangeUpdates
  url: https://insights.deribit.com/exchange-updates/
- group: operate
  title: ''
  type: Status
  url: https://status.deribit.com/
- group: operate
  title: ''
  type: Support
  url: https://support.deribit.com/hc/en-us
- group: other
  title: ''
  type: Fees
  url: https://support.deribit.com/hc/en-us/articles/25944746248989-Fees
- group: commercial
  title: ''
  type: TermsOfService
  url: https://support.deribit.com/hc/en-us/sections/25944530944285-Terms-Of-Service-Overview
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://support.deribit.com/hc/en-us/articles/25944470689309-Privacy-Notice
- group: start
  title: ''
  type: Console
  url: https://www.deribit.com/api_console
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.deribit.com/pages/information/Releases
- group: docs
  title: ''
  type: MulticastGuide
  url: https://support.deribit.com/hc/en-us/articles/29392445838877-Multicast-Developer-Guide
- group: commercial
  title: ''
  type: x-plans
  url: https://raw.githubusercontent.com/api-evangelist/deribit/refs/heads/main/plans/plans.yml
- group: other
  title: ''
  type: x-rate-limits
  url: https://raw.githubusercontent.com/api-evangelist/deribit/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: x-finops
  url: https://raw.githubusercontent.com/api-evangelist/deribit/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: Deribit is a leading Bitcoin and Ethereum options and futures exchange offering a comprehensive REST and WebSocket API for derivatives trading, market data, portfolio management, and block trades. The platform supports futures, perpetuals, options, and spot trading across BTC, ETH, and SOL with both individual and institutional access via JSON-RPC, HTTP, and FIX protocol interfaces.
examples:
- key_count: 4
  name: Private_Accept_Block_Rfq_Get_Request_Request
  slug: private_accept_block_rfq_get_request_request
- key_count: 4
  name: Private_Add_Block_Rfq_Quote_Get_Request_Request
  slug: private_add_block_rfq_quote_get_request_request
- key_count: 4
  name: Private_Add_To_Address_Book_Get_Request_Request
  slug: private_add_to_address_book_get_request_request
- key_count: 4
  name: Private_Approve_Block_Trade_Get_Request_Request
  slug: private_approve_block_trade_get_request_request
- key_count: 4
  name: Private_Buy_Get_Request_Request
  slug: private_buy_get_request_request
- key_count: 4
  name: Private_Cancel_All_Block_Rfq_Quotes_Get_Request_Request
  slug: private_cancel_all_block_rfq_quotes_get_request_request
- key_count: 4
  name: Private_Cancel_All_By_Currency_Get_Request_Request
  slug: private_cancel_all_by_currency_get_request_request
- key_count: 4
  name: Private_Cancel_All_By_Currency_Pair_Get_Request_Request
  slug: private_cancel_all_by_currency_pair_get_request_request
- key_count: 4
  name: Private_Cancel_All_By_Instrument_Get_Request_Request
  slug: private_cancel_all_by_instrument_get_request_request
- key_count: 4
  name: Private_Cancel_All_By_Kind_Or_Type_Get_Request_Request
  slug: private_cancel_all_by_kind_or_type_get_request_request
- key_count: 4
  name: Private_Cancel_All_Get_Request_Request
  slug: private_cancel_all_get_request_request
- key_count: 4
  name: Private_Cancel_Block_Rfq_Get_Request_Request
  slug: private_cancel_block_rfq_get_request_request
- key_count: 4
  name: Private_Cancel_Block_Rfq_Quote_Get_Request_Request
  slug: private_cancel_block_rfq_quote_get_request_request
- key_count: 4
  name: Private_Cancel_Block_Rfq_Trigger_Get_Request_Request
  slug: private_cancel_block_rfq_trigger_get_request_request
- key_count: 4
  name: Private_Cancel_By_Label_Get_Request_Request
  slug: private_cancel_by_label_get_request_request
- key_count: 4
  name: Private_Cancel_Get_Request_Request
  slug: private_cancel_get_request_request
- key_count: 4
  name: Private_Cancel_Quotes_Get_Request_Request
  slug: private_cancel_quotes_get_request_request
- key_count: 4
  name: Private_Cancel_Transfer_By_Id_Get_Request_Request
  slug: private_cancel_transfer_by_id_get_request_request
- key_count: 4
  name: Private_Cancel_Withdrawal_Get_Request_Request
  slug: private_cancel_withdrawal_get_request_request
- key_count: 4
  name: Private_Change_Api_Key_Name_Get_Request_Request
  slug: private_change_api_key_name_get_request_request
- key_count: 4
  name: Private_Change_Margin_Model_Get_Request_Request
  slug: private_change_margin_model_get_request_request
- key_count: 4
  name: Private_Change_Scope_In_Api_Key_Get_Request_Request
  slug: private_change_scope_in_api_key_get_request_request
- key_count: 4
  name: Private_Change_Subaccount_Name_Get_Request_Request
  slug: private_change_subaccount_name_get_request_request
- key_count: 4
  name: Private_Close_Position_Get_Request_Request
  slug: private_close_position_get_request_request
- key_count: 4
  name: Private_Create_Api_Key_Get_Request_Request
  slug: private_create_api_key_get_request_request
- key_count: 4
  name: Private_Create_Block_Rfq_Get_Request_Request
  slug: private_create_block_rfq_get_request_request
- key_count: 4
  name: Private_Create_Combo_Get_Request_Request
  slug: private_create_combo_get_request_request
- key_count: 4
  name: Private_Create_Deposit_Address_Get_Request_Request
  slug: private_create_deposit_address_get_request_request
- key_count: 4
  name: Private_Create_Subaccount_Get_Request_Request
  slug: private_create_subaccount_get_request_request
- key_count: 4
  name: Private_Delete_Address_Beneficiary_Get_Request_Request
  slug: private_delete_address_beneficiary_get_request_request
- key_count: 4
  name: Private_Disable_Api_Key_Get_Request_Request
  slug: private_disable_api_key_get_request_request
- key_count: 4
  name: Private_Disable_Cancel_On_Disconnect_Get_Request_Request
  slug: private_disable_cancel_on_disconnect_get_request_request
- key_count: 4
  name: Private_Edit_Api_Key_Get_Request_Request
  slug: private_edit_api_key_get_request_request
- key_count: 4
  name: Private_Edit_Block_Rfq_Quote_Get_Request_Request
  slug: private_edit_block_rfq_quote_get_request_request
- key_count: 4
  name: Private_Edit_By_Label_Get_Request_Request
  slug: private_edit_by_label_get_request_request
- key_count: 4
  name: Private_Edit_Get_Request_Request
  slug: private_edit_get_request_request
- key_count: 4
  name: Private_Enable_Affiliate_Program_Get_Request_Request
  slug: private_enable_affiliate_program_get_request_request
- key_count: 4
  name: Private_Enable_Api_Key_Get_Request_Request
  slug: private_enable_api_key_get_request_request
- key_count: 4
  name: Private_Enable_Cancel_On_Disconnect_Get_Request_Request
  slug: private_enable_cancel_on_disconnect_get_request_request
- key_count: 4
  name: Private_Execute_Block_Trade_Get_Request_Request
  slug: private_execute_block_trade_get_request_request
- key_count: 4
  name: Private_Get_Access_Log_Get_Request_Request
  slug: private_get_access_log_get_request_request
- key_count: 4
  name: Private_Get_Account_Summaries_Get_Request_Request
  slug: private_get_account_summaries_get_request_request
- key_count: 4
  name: Private_Get_Account_Summary_Get_Request_Request
  slug: private_get_account_summary_get_request_request
- key_count: 4
  name: Private_Get_Address_Beneficiary_Get_Request_Request
  slug: private_get_address_beneficiary_get_request_request
- key_count: 4
  name: Private_Get_Address_Book_Get_Request_Request
  slug: private_get_address_book_get_request_request
- key_count: 4
  name: Private_Get_Affiliate_Program_Info_Get_Request_Request
  slug: private_get_affiliate_program_info_get_request_request
- key_count: 4
  name: Private_Get_Block_Rfq_Makers_Get_Request_Request
  slug: private_get_block_rfq_makers_get_request_request
- key_count: 4
  name: Private_Get_Block_Rfq_Quotes_Get_Request_Request
  slug: private_get_block_rfq_quotes_get_request_request
- key_count: 4
  name: Private_Get_Block_Rfq_User_Info_Get_Request_Request
  slug: private_get_block_rfq_user_info_get_request_request
- key_count: 4
  name: Private_Get_Block_Rfqs_Get_Request_Request
  slug: private_get_block_rfqs_get_request_request
- key_count: 4
  name: Private_Get_Block_Trade_Get_Request_Request
  slug: private_get_block_trade_get_request_request
- key_count: 4
  name: Private_Get_Block_Trade_Requests_Get_Request_Request
  slug: private_get_block_trade_requests_get_request_request
- key_count: 4
  name: Private_Get_Block_Trades_Get_Request_Request
  slug: private_get_block_trades_get_request_request
- key_count: 4
  name: Private_Get_Broker_Trade_Requests_Get_Request_Request
  slug: private_get_broker_trade_requests_get_request_request
- key_count: 4
  name: Private_Get_Broker_Trades_Get_Request_Request
  slug: private_get_broker_trades_get_request_request
- key_count: 4
  name: Private_Get_Cancel_On_Disconnect_Get_Request_Request
  slug: private_get_cancel_on_disconnect_get_request_request
- key_count: 4
  name: Private_Get_Current_Deposit_Address_Get_Request_Request
  slug: private_get_current_deposit_address_get_request_request
- key_count: 4
  name: Private_Get_Deposits_Get_Request_Request
  slug: private_get_deposits_get_request_request
- key_count: 4
  name: Private_Get_Email_Language_Get_Request_Request
  slug: private_get_email_language_get_request_request
- key_count: 4
  name: Private_Get_Leg_Prices_Get_Request_Request
  slug: private_get_leg_prices_get_request_request
- key_count: 4
  name: Private_Get_Margins_Get_Request_Request
  slug: private_get_margins_get_request_request
- key_count: 4
  name: Private_Get_Mmp_Config_Get_Request_Request
  slug: private_get_mmp_config_get_request_request
- key_count: 4
  name: Private_Get_Mmp_Status_Get_Request_Request
  slug: private_get_mmp_status_get_request_request
- key_count: 4
  name: Private_Get_New_Announcements_Get_Request_Request
  slug: private_get_new_announcements_get_request_request
- key_count: 4
  name: Private_Get_Open_Orders_By_Currency_Get_Request_Request
  slug: private_get_open_orders_by_currency_get_request_request
- key_count: 4
  name: Private_Get_Open_Orders_By_Instrument_Get_Request_Request
  slug: private_get_open_orders_by_instrument_get_request_request
- key_count: 4
  name: Private_Get_Open_Orders_By_Label_Get_Request_Request
  slug: private_get_open_orders_by_label_get_request_request
- key_count: 4
  name: Private_Get_Open_Orders_Get_Request_Request
  slug: private_get_open_orders_get_request_request
- key_count: 4
  name: Private_Get_Order_History_By_Currency_Get_Request_Request
  slug: private_get_order_history_by_currency_get_request_request
- key_count: 4
  name: Private_Get_Order_History_By_Instrument_Get_Request_Request
  slug: private_get_order_history_by_instrument_get_request_request
- key_count: 4
  name: Private_Get_Order_Margin_By_Ids_Get_Request_Request
  slug: private_get_order_margin_by_ids_get_request_request
- key_count: 4
  name: Private_Get_Order_State_By_Label_Get_Request_Request
  slug: private_get_order_state_by_label_get_request_request
- key_count: 4
  name: Private_Get_Order_State_Get_Request_Request
  slug: private_get_order_state_get_request_request
- key_count: 4
  name: Private_Get_Position_Get_Request_Request
  slug: private_get_position_get_request_request
- key_count: 4
  name: Private_Get_Positions_Get_Request_Request
  slug: private_get_positions_get_request_request
- key_count: 4
  name: Private_Get_Reward_Eligibility_Get_Request_Request
  slug: private_get_reward_eligibility_get_request_request
- key_count: 4
  name: Private_Get_Settlement_History_By_Currency_Get_Request_Request
  slug: private_get_settlement_history_by_currency_get_request_request
- key_count: 4
  name: Private_Get_Settlement_History_By_Instrument_Get_Request_Request
  slug: private_get_settlement_history_by_instrument_get_request_request
- key_count: 4
  name: Private_Get_Subaccounts_Details_Get_Request_Request
  slug: private_get_subaccounts_details_get_request_request
- key_count: 4
  name: Private_Get_Subaccounts_Get_Request_Request
  slug: private_get_subaccounts_get_request_request
- key_count: 4
  name: Private_Get_Transaction_Log_Get_Request_Request
  slug: private_get_transaction_log_get_request_request
- key_count: 4
  name: Private_Get_Transfers_Get_Request_Request
  slug: private_get_transfers_get_request_request
- key_count: 4
  name: Private_Get_Trigger_Order_History_Get_Request_Request
  slug: private_get_trigger_order_history_get_request_request
- key_count: 4
  name: Private_Get_User_Locks_Get_Request_Request
  slug: private_get_user_locks_get_request_request
- key_count: 4
  name: Private_Get_User_Trades_By_Currency_And_Time_Get_Request_Request
  slug: private_get_user_trades_by_currency_and_time_get_request_request
- key_count: 4
  name: Private_Get_User_Trades_By_Currency_Get_Request_Request
  slug: private_get_user_trades_by_currency_get_request_request
- key_count: 4
  name: Private_Get_User_Trades_By_Instrument_And_Time_Get_Request_Request
  slug: private_get_user_trades_by_instrument_and_time_get_request_request
- key_count: 4
  name: Private_Get_User_Trades_By_Instrument_Get_Request_Request
  slug: private_get_user_trades_by_instrument_get_request_request
- key_count: 4
  name: Private_Get_User_Trades_By_Order_Get_Request_Request
  slug: private_get_user_trades_by_order_get_request_request
- key_count: 4
  name: Private_Get_Withdrawals_Get_Request_Request
  slug: private_get_withdrawals_get_request_request
- key_count: 4
  name: Private_Invalidate_Block_Trade_Signature_Get_Request_Request
  slug: private_invalidate_block_trade_signature_get_request_request
- key_count: 4
  name: Private_List_Address_Beneficiaries_Get_Request_Request
  slug: private_list_address_beneficiaries_get_request_request
- key_count: 4
  name: Private_List_Custody_Accounts_Get_Request_Request
  slug: private_list_custody_accounts_get_request_request
- key_count: 4
  name: Private_Logout_Get_Request_Request
  slug: private_logout_get_request_request
- key_count: 4
  name: Private_Mass_Quote_Get_Request_Request
  slug: private_mass_quote_get_request_request
- key_count: 4
  name: Private_Move_Positions_Get_Request_Request
  slug: private_move_positions_get_request_request
- key_count: 4
  name: Private_Pme_Simulate_Get_Request_Request
  slug: private_pme_simulate_get_request_request
- key_count: 4
  name: Private_Reject_Block_Trade_Get_Request_Request
  slug: private_reject_block_trade_get_request_request
- key_count: 4
  name: Private_Remove_Api_Key_Get_Request_Request
  slug: private_remove_api_key_get_request_request
- key_count: 4
  name: Private_Remove_From_Address_Book_Get_Request_Request
  slug: private_remove_from_address_book_get_request_request
- key_count: 4
  name: Private_Remove_Subaccount_Get_Request_Request
  slug: private_remove_subaccount_get_request_request
- key_count: 4
  name: Private_Reset_Api_Key_Get_Request_Request
  slug: private_reset_api_key_get_request_request
- key_count: 4
  name: Private_Reset_Mmp_Get_Request_Request
  slug: private_reset_mmp_get_request_request
- key_count: 4
  name: Private_Save_Address_Beneficiary_Get_Request_Request
  slug: private_save_address_beneficiary_get_request_request
- key_count: 4
  name: Private_Sell_Get_Request_Request
  slug: private_sell_get_request_request
- key_count: 4
  name: Private_Set_Announcement_As_Read_Get_Request_Request
  slug: private_set_announcement_as_read_get_request_request
- key_count: 4
  name: Private_Set_Clearance_Originator_Get_Request_Request
  slug: private_set_clearance_originator_get_request_request
- key_count: 4
  name: Private_Set_Email_For_Subaccount_Get_Request_Request
  slug: private_set_email_for_subaccount_get_request_request
- key_count: 4
  name: Private_Set_Email_Language_Get_Request_Request
  slug: private_set_email_language_get_request_request
- key_count: 4
  name: Private_Set_Mmp_Config_Get_Request_Request
  slug: private_set_mmp_config_get_request_request
- key_count: 4
  name: Private_Set_Self_Trading_Config_Get_Request_Request
  slug: private_set_self_trading_config_get_request_request
- key_count: 4
  name: Private_Simulate_Block_Trade_Get_Request_Request
  slug: private_simulate_block_trade_get_request_request
- key_count: 4
  name: Private_Simulate_Portfolio_Get_Request_Request
  slug: private_simulate_portfolio_get_request_request
- key_count: 4
  name: Private_Submit_Transfer_Between_Subaccounts_Get_Request_Request
  slug: private_submit_transfer_between_subaccounts_get_request_request
- key_count: 4
  name: Private_Submit_Transfer_To_Subaccount_Get_Request_Request
  slug: private_submit_transfer_to_subaccount_get_request_request
- key_count: 4
  name: Private_Submit_Transfer_To_User_Get_Request_Request
  slug: private_submit_transfer_to_user_get_request_request
- key_count: 4
  name: Private_Subscribe_Get_Request_Request
  slug: private_subscribe_get_request_request
- key_count: 4
  name: Private_Toggle_Notifications_From_Subaccount_Get_Request_Request
  slug: private_toggle_notifications_from_subaccount_get_request_request
- key_count: 4
  name: Private_Toggle_Subaccount_Login_Get_Request_Request
  slug: private_toggle_subaccount_login_get_request_request
- key_count: 4
  name: Private_Unsubscribe_All_Get_Request_Request
  slug: private_unsubscribe_all_get_request_request
- key_count: 4
  name: Private_Unsubscribe_Get_Request_Request
  slug: private_unsubscribe_get_request_request
- key_count: 4
  name: Private_Update_In_Address_Book_Get_Request_Request
  slug: private_update_in_address_book_get_request_request
- key_count: 4
  name: Private_Verify_Block_Trade_Get_Request_Request
  slug: private_verify_block_trade_get_request_request
- key_count: 4
  name: Private_Withdraw_Get_Request_Request
  slug: private_withdraw_get_request_request
- key_count: 4
  name: Public_Auth_Get_Request_Request
  slug: public_auth_get_request_request
- key_count: 4
  name: Public_Disable_Heartbeat_Get_Request_Request
  slug: public_disable_heartbeat_get_request_request
- key_count: 4
  name: Public_Exchange_Token_Get_Request_Request
  slug: public_exchange_token_get_request_request
- key_count: 4
  name: Public_Fork_Token_Get_Request_Request
  slug: public_fork_token_get_request_request
- key_count: 4
  name: Public_Get_Announcements_Get_Request_Request
  slug: public_get_announcements_get_request_request
- key_count: 4
  name: Public_Get_Apr_History_Get_Request_Request
  slug: public_get_apr_history_get_request_request
- key_count: 4
  name: Public_Get_Block_Rfq_Trades_Get_Request_Request
  slug: public_get_block_rfq_trades_get_request_request
- key_count: 4
  name: Public_Get_Book_Summary_By_Currency_Get_Request_Request
  slug: public_get_book_summary_by_currency_get_request_request
- key_count: 4
  name: Public_Get_Book_Summary_By_Instrument_Get_Request_Request
  slug: public_get_book_summary_by_instrument_get_request_request
- key_count: 4
  name: Public_Get_Combo_Details_Get_Request_Request
  slug: public_get_combo_details_get_request_request
- key_count: 4
  name: Public_Get_Combo_Ids_Get_Request_Request
  slug: public_get_combo_ids_get_request_request
- key_count: 4
  name: Public_Get_Combos_Get_Request_Request
  slug: public_get_combos_get_request_request
- key_count: 4
  name: Public_Get_Currencies_Get_Request_Request
  slug: public_get_currencies_get_request_request
- key_count: 4
  name: Public_Get_Delivery_Prices_Get_Request_Request
  slug: public_get_delivery_prices_get_request_request
- key_count: 4
  name: Public_Get_Expirations_Get_Request_Request
  slug: public_get_expirations_get_request_request
- key_count: 4
  name: Public_Get_Funding_Rate_History_Get_Request_Request
  slug: public_get_funding_rate_history_get_request_request
- key_count: 4
  name: Public_Get_Funding_Rate_Value_Get_Request_Request
  slug: public_get_funding_rate_value_get_request_request
- key_count: 4
  name: Public_Get_Historical_Volatility_Get_Request_Request
  slug: public_get_historical_volatility_get_request_request
- key_count: 4
  name: Public_Get_Index_Chart_Data_Get_Request_Request
  slug: public_get_index_chart_data_get_request_request
- key_count: 4
  name: Public_Get_Index_Price_Names_Get_Request_Request
  slug: public_get_index_price_names_get_request_request
- key_count: 4
  name: Public_Get_Instrument_Get_Request_Request
  slug: public_get_instrument_get_request_request
- key_count: 4
  name: Public_Get_Instruments_Get_Request_Request
  slug: public_get_instruments_get_request_request
- key_count: 4
  name: Public_Get_Last_Settlements_By_Currency_Get_Request_Request
  slug: public_get_last_settlements_by_currency_get_request_request
- key_count: 4
  name: Public_Get_Last_Settlements_By_Instrument_Get_Request_Request
  slug: public_get_last_settlements_by_instrument_get_request_request
- key_count: 4
  name: Public_Get_Last_Trades_By_Currency_And_Time_Get_Request_Request
  slug: public_get_last_trades_by_currency_and_time_get_request_request
- key_count: 4
  name: Public_Get_Last_Trades_By_Currency_Get_Request_Request
  slug: public_get_last_trades_by_currency_get_request_request
- key_count: 4
  name: Public_Get_Last_Trades_By_Instrument_And_Time_Get_Request_Request
  slug: public_get_last_trades_by_instrument_and_time_get_request_request
- key_count: 4
  name: Public_Get_Last_Trades_By_Instrument_Get_Request_Request
  slug: public_get_last_trades_by_instrument_get_request_request
- key_count: 4
  name: Public_Get_Mark_Price_History_Get_Request_Request
  slug: public_get_mark_price_history_get_request_request
- key_count: 4
  name: Public_Get_Order_Book_Get_Request_Request
  slug: public_get_order_book_get_request_request
- key_count: 4
  name: Public_Get_Time_Get_Request_Request
  slug: public_get_time_get_request_request
- key_count: 4
  name: Public_Get_Tradingview_Chart_Data_Get_Request_Request
  slug: public_get_tradingview_chart_data_get_request_request
- key_count: 4
  name: Public_Get_Volatility_Index_Data_Get_Request_Request
  slug: public_get_volatility_index_data_get_request_request
- key_count: 4
  name: Public_Hello_Get_Request_Request
  slug: public_hello_get_request_request
- key_count: 4
  name: Public_Set_Heartbeat_Get_Request_Request
  slug: public_set_heartbeat_get_request_request
- key_count: 4
  name: Public_Status_Get_Request_Request
  slug: public_status_get_request_request
- key_count: 4
  name: Public_Subscribe_Get_Request_Request
  slug: public_subscribe_get_request_request
- key_count: 4
  name: Public_Test_Get_Request_Request
  slug: public_test_get_request_request
- key_count: 4
  name: Public_Ticker_Get_Request_Request
  slug: public_ticker_get_request_request
- key_count: 4
  name: Public_Unsubscribe_All_Get_Request_Request
  slug: public_unsubscribe_all_get_request_request
- key_count: 4
  name: Public_Unsubscribe_Get_Request_Request
  slug: public_unsubscribe_get_request_request
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://www.deribit.com/images/deribit-logo.png
json_schemas:
- name: Addressownershipresponse
  property_count: 3
  slug: AddressOwnershipResponse
- name: Errormessageresponse
  property_count: 4
  slug: ErrorMessageResponse
- name: Errorresponse
  property_count: 2
  slug: ErrorResponse
- name: Getlistcustodyaccounts200Response
  property_count: 0
  slug: GetlistCustodyAccounts200response
- name: Getunsubscribe200Response
  property_count: 3
  slug: Getunsubscribe200response
- name: Multicastgetinstrumentdictionaryresponse
  property_count: 3
  slug: MulticastGetInstrumentDictionaryResponse
- name: Multicastgetpacketresponse
  property_count: 3
  slug: MulticastGetPacketResponse
- name: Multicastgetpacketsresponse
  property_count: 3
  slug: MulticastGetPacketsResponse
- name: Okresponse
  property_count: 3
  slug: OkResponse
- name: Privateacceptblockrfqresponse
  property_count: 3
  slug: PrivateAcceptBlockRfqResponse
- name: Privateaccountresponse
  property_count: 3
  slug: PrivateAccountResponse
- name: Privateaccountsummariesresponse
  property_count: 3
  slug: PrivateAccountSummariesResponse
- name: Privateaddblockrfqquoteresponse
  property_count: 3
  slug: PrivateAddBlockRfqQuoteResponse
- name: Privateaddtoaddressbookresponse
  property_count: 3
  slug: PrivateAddToAddressBookResponse
- name: Privateaddressbookresponse
  property_count: 3
  slug: PrivateAddressBookResponse
- name: Privateapikeyresponse
  property_count: 3
  slug: PrivateApiKeyResponse
- name: Privatebuyandsellresponse
  property_count: 3
  slug: PrivateBuyAndSellResponse
- name: Privatecancelallblockrfqquotesresponse
  property_count: 3
  slug: PrivateCancelAllBlockRfqQuotesResponse
- name: Privatecancelallresponse
  property_count: 3
  slug: PrivateCancelAllResponse
- name: Privatecancelblockrfqquoteresponse
  property_count: 3
  slug: PrivateCancelBlockRfqQuoteResponse
- name: Privatecancelblockrfqresponse
  property_count: 3
  slug: PrivateCancelBlockRfqResponse
- name: Privatecancelblockrfqtriggerresponse
  property_count: 0
  slug: PrivateCancelBlockRfqTriggerResponse
- name: Privatecancelquotesresponse
  property_count: 3
  slug: PrivateCancelQuotesResponse
- name: Privatecancelresponse
  property_count: 3
  slug: PrivateCancelResponse
- name: Privatechangemarginmodelresponse
  property_count: 3
  slug: PrivateChangeMarginModelResponse
- name: Privatechangepasswordresponse
  property_count: 3
  slug: PrivateChangePasswordResponse
- name: Privatechatgetaccountsummaryresponse
  property_count: 3
  slug: PrivateChatGetAccountSummaryResponse
- name: Privatechatsetnickresponse
  property_count: 3
  slug: PrivateChatSetNickResponse
- name: Privatecreateblockrfqresponse
  property_count: 3
  slug: PrivateCreateBlockRfqResponse
- name: Privatecreatecomboresponse
  property_count: 3
  slug: PrivateCreateComboResponse
- name: Privatecreatesubaccountresponse
  property_count: 3
  slug: PrivateCreateSubaccountResponse
- name: Privatecustodysettlementresponse
  property_count: 3
  slug: PrivateCustodySettlementResponse
- name: Privatedeleteaddressbeneficiaryresponse
  property_count: 3
  slug: PrivateDeleteAddressBeneficiaryResponse
- name: Privatedepositaddressresponse
  property_count: 3
  slug: PrivateDepositAddressResponse
- name: Privateeditblockrfqquoteresponse
  property_count: 3
  slug: PrivateEditBlockRfqQuoteResponse
- name: Privateeditresponse
  property_count: 3
  slug: PrivateEditResponse
- name: Privategetaccesslogresponse
  property_count: 3
  slug: PrivateGetAccessLogResponse
- name: Privategetaddressbeneficiaryresponse
  property_count: 3
  slug: PrivateGetAddressBeneficiaryResponse
- name: Privategetaffiliateprograminforesponse
  property_count: 3
  slug: PrivateGetAffiliateProgramInfoResponse
- name: Privategetallbalancessnapshotresponse
  property_count: 3
  slug: PrivateGetAllBalancesSnapshotResponse
- name: Privategetbalanceresponse
  property_count: 3
  slug: PrivateGetBalanceResponse
- name: Privategetbalancesnapshotresponse
  property_count: 3
  slug: PrivateGetBalanceSnapshotResponse
- name: Privategetblockrfqmakersresponse
  property_count: 3
  slug: PrivateGetBlockRfqMakersResponse
- name: Privategetblockrfqquotesresponse
  property_count: 3
  slug: PrivateGetBlockRfqQuotesResponse
- name: Privategetblockrfquserinforesponse
  property_count: 3
  slug: PrivateGetBlockRfqUserInfoResponse
- name: Privategetblockrfqsresponse
  property_count: 3
  slug: PrivateGetBlockRfqsResponse
- name: Privategetblocktraderequestsresponse
  property_count: 3
  slug: PrivateGetBlockTradeRequestsResponse
- name: Privategetblocktraderesponse
  property_count: 3
  slug: PrivateGetBlockTradeResponse
- name: Privategetblocktradesresponse
  property_count: 3
  slug: PrivateGetBlockTradesResponse
- name: Privategetbrokertraderequestsresponse
  property_count: 3
  slug: PrivateGetBrokerTradeRequestsResponse
- name: Privategetbrokertradesresponse
  property_count: 3
  slug: PrivateGetBrokerTradesResponse
- name: Privategetcancelondisconnectresponse
  property_count: 3
  slug: PrivateGetCancelOnDisconnectResponse
- name: Privategetdepositsresponse
  property_count: 3
  slug: PrivateGetDepositsResponse
- name: Privategetemaillanguageresponse
  property_count: 3
  slug: PrivateGetEmailLanguageResponse
- name: Privategetjwtresponse
  property_count: 3
  slug: PrivateGetJwtResponse
- name: Privategetlegpricesresponse
  property_count: 3
  slug: PrivateGetLegPricesResponse
- name: Privategetmarginsresponse
  property_count: 3
  slug: PrivateGetMarginsResponse
- name: Privategetmmpconfigresponse
  property_count: 3
  slug: PrivateGetMmpConfigResponse
- name: Privategetmmpstatusresponse
  property_count: 3
  slug: PrivateGetMmpStatusResponse
- name: Privategetopenordersresponse
  property_count: 3
  slug: PrivateGetOpenOrdersResponse
- name: Privategetorderhistoryresponse
  property_count: 3
  slug: PrivateGetOrderHistoryResponse
- name: Privategetordermarginbyidsresponse
  property_count: 3
  slug: PrivateGetOrderMarginByIdsResponse
- name: Privategetorderstatebylabelresponse
  property_count: 3
  slug: PrivateGetOrderStateByLabelResponse
- name: Privategetorderstateresponse
  property_count: 3
  slug: PrivateGetOrderStateResponse
- name: Privategetpositionresponse
  property_count: 3
  slug: PrivateGetPositionResponse
- name: Privategetpositionsresponse
  property_count: 3
  slug: PrivateGetPositionsResponse
- name: Privategetrewardeligibilityresponse
  property_count: 3
  slug: PrivateGetRewardEligibilityResponse
- name: Privategetsecuritykeyactivationdataresponse
  property_count: 3
  slug: PrivateGetSecurityKeyActivationDataResponse
- name: Privategetsecuritykeystatusresponse
  property_count: 3
  slug: PrivateGetSecurityKeyStatusResponse
- name: Privategetsubaccountsdetailsresponse
  property_count: 3
  slug: PrivateGetSubaccountsDetailsResponse
- name: Privategetsubaccountsresponse
  property_count: 3
  slug: PrivateGetSubaccountsResponse
- name: Privategettransactionlogresponse
  property_count: 3
  slug: PrivateGetTransactionLogResponse
- name: Privategettransfersresponse
  property_count: 3
  slug: PrivateGetTransfersResponse
- name: Privategettriggerorderhistoryresponse
  property_count: 3
  slug: PrivateGetTriggerOrderHistoryResponse
- name: Privategetuserlocksresponse
  property_count: 3
  slug: PrivateGetUserLocksResponse
- name: Privategetusertradesbyorderresponse
  property_count: 2
  slug: PrivateGetUserTradesByOrderResponse
- name: Privategetusertradeshistoryresponse
  property_count: 3
  slug: PrivateGetUserTradesHistoryResponse
- name: Privategetwithdrawalpolicylimitsresponse
  property_count: 3
  slug: PrivateGetWithdrawalPolicyLimitsResponse
- name: Privategetwithdrawalpolicymoderesponse
  property_count: 3
  slug: PrivateGetWithdrawalPolicyModeResponse
- name: Privategetwithdrawalsresponse
  property_count: 3
  slug: PrivateGetWithdrawalsResponse
- name: Privatelistaddressbeneficiariesresponse
  property_count: 3
  slug: PrivateListAddressBeneficiariesResponse
- name: Privatelistsecuritykeysresponse
  property_count: 3
  slug: PrivateListSecurityKeysResponse
- name: Privatemassquoteresponse
  property_count: 3
  slug: PrivateMassQuoteResponse
- name: Privatepmeparamsresponse
  property_count: 3
  slug: PrivatePmeParamsResponse
- name: Privatepmesimulateresponse
  property_count: 3
  slug: PrivatePmeSimulateResponse
- name: Privatepositionmoveresponse
  property_count: 3
  slug: PrivatePositionMoveResponse
- name: Privateputbalanceresponse
  property_count: 3
  slug: PrivatePutBalanceResponse
- name: Privateremovefromaddressbookresponse
  property_count: 3
  slug: PrivateRemoveFromAddressBookResponse
- name: Privatesaveaddressbeneficiaryresponse
  property_count: 3
  slug: PrivateSaveAddressBeneficiaryResponse
- name: Privatesetmmpconfigresponse
  property_count: 3
  slug: PrivateSetMmpConfigResponse
- name: Privatesettlementresponse
  property_count: 3
  slug: PrivateSettlementResponse
- name: Privatesimulateblocktraderesponse
  property_count: 3
  slug: PrivateSimulateBlockTradeResponse
- name: Privatesimulateportfolioresponse
  property_count: 3
  slug: PrivateSimulatePortfolioResponse
- name: Privatestatsresponse
  property_count: 3
  slug: PrivateStatsResponse
- name: Privatesubmittransferresponse
  property_count: 3
  slug: PrivateSubmitTransferResponse
- name: Privatesubscriberesponse
  property_count: 3
  slug: PrivateSubscribeResponse
- name: Privateupdateinaddressbookresponse
  property_count: 3
  slug: PrivateUpdateInAddressBookResponse
- name: Privateverifyblocktraderesponse
  property_count: 3
  slug: PrivateVerifyBlockTradeResponse
- name: Privatewithdrawresponse
  property_count: 3
  slug: PrivateWithdrawResponse
- name: Publicauthresponse
  property_count: 3
  slug: PublicAuthResponse
- name: Publicgetannouncementsresponse
  property_count: 3
  slug: PublicGetAnnouncementsResponse
- name: Publicgetaprhistoryresponse
  property_count: 3
  slug: PublicGetAprHistoryResponse
- name: Publicgetblockrfqtradesresponse
  property_count: 3
  slug: PublicGetBlockRfqTradesResponse
- name: Publicgetbooksummaryresponse
  property_count: 3
  slug: PublicGetBookSummaryResponse
- name: Publicgetcombodetailsresponse
  property_count: 3
  slug: PublicGetComboDetailsResponse
- name: Publicgetcomboidsresponse
  property_count: 3
  slug: PublicGetComboIdsResponse
- name: Publicgetcombosresponse
  property_count: 3
  slug: PublicGetCombosResponse
- name: Publicgetcontractsizeresponse
  property_count: 3
  slug: PublicGetContractSizeResponse
- name: Publicgetcurrenciesresponse
  property_count: 3
  slug: PublicGetCurrenciesResponse
- name: Publicgetdeliverypricesresponse
  property_count: 3
  slug: PublicGetDeliveryPricesResponse
- name: Publicgetexpirationsresponse
  property_count: 3
  slug: PublicGetExpirationsResponse
- name: Publicgetfundingchartdataresponse
  property_count: 3
  slug: PublicGetFundingChartDataResponse
- name: Publicgetfundingratehistoryresponse
  property_count: 3
  slug: PublicGetFundingRateHistoryResponse
- name: Publicgetfundingratevalueresponse
  property_count: 3
  slug: PublicGetFundingRateValueResponse
- name: Publicgethistoricalvolatilityresponse
  property_count: 3
  slug: PublicGetHistoricalVolatilityResponse
- name: Publicgetindexchartdataresponse
  property_count: 3
  slug: PublicGetIndexChartDataResponse
- name: Publicgetindexpricenamesresponse
  property_count: 3
  slug: PublicGetIndexPriceNamesResponse
- name: Publicgetindexpriceresponse
  property_count: 3
  slug: PublicGetIndexPriceResponse
- name: Publicgetinstrumentresponse
  property_count: 3
  slug: PublicGetInstrumentResponse
- name: Publicgetinstrumentsresponse
  property_count: 3
  slug: PublicGetInstrumentsResponse
- name: Publicgetmarkpricehistoryresponse
  property_count: 3
  slug: PublicGetMarkPriceHistoryResponse
- name: Publicgetmarkpricechartdataresponse
  property_count: 3
  slug: PublicGetMarkpriceChartDataResponse
- name: Publicgetorderbookresponse
  property_count: 3
  slug: PublicGetOrderBookResponse
- name: Publicgetsecuritykeysresetdataresponse
  property_count: 3
  slug: PublicGetSecurityKeysResetDataResponse
- name: Publicgettimeresponse
  property_count: 3
  slug: PublicGetTimeResponse
- name: Publicgettradesvolumesresponse
  property_count: 3
  slug: PublicGetTradesVolumesResponse
- name: Publicgettradingviewchartdataresponse
  property_count: 3
  slug: PublicGetTradingviewChartDataResponse
- name: Publicgetvolatilityindexdataresponse
  property_count: 3
  slug: PublicGetVolatilityIndexDataResponse
- name: Publiclistapikeysresponse
  property_count: 3
  slug: PublicListApiKeysResponse
- name: Publicplaceholderresponse
  property_count: 3
  slug: PublicPlaceholderResponse
- name: Publicsettlementresponse
  property_count: 3
  slug: PublicSettlementResponse
- name: Publicstatusresponse
  property_count: 3
  slug: PublicStatusResponse
- name: Publictestresponse
  property_count: 3
  slug: PublicTestResponse
- name: Publictickerresponse
  property_count: 3
  slug: PublicTickerResponse
- name: Publictickersbyexpirationresponse
  property_count: 3
  slug: PublicTickersByExpirationResponse
- name: Publictokenresponse
  property_count: 3
  slug: PublicTokenResponse
- name: Publictradeshistoryresponse
  property_count: 3
  slug: PublicTradesHistoryResponse
- name: Tickernotification
  property_count: 27
  slug: TickerNotification
- name: Tickernotificationwithbidsandasks
  property_count: 27
  slug: TickerNotificationWithBidsAndAsks
- name: Vaspsresponse
  property_count: 3
  slug: VaspsResponse
- name: Access Log
  property_count: 7
  slug: access_log
- name: Additional Reserve
  property_count: 0
  slug: additional_reserve
- name: Address Beneficiary Item
  property_count: 16
  slug: address_beneficiary_item
- name: Address Book Item
  property_count: 19
  slug: address_book_item
- name: Address Book Type
  property_count: 0
  slug: address_book_type
- name: Address Book Type Without Deposit Source
  property_count: 0
  slug: address_book_type_without_deposit_source
- name: Address Info Required
  property_count: 0
  slug: address_info_required
- name: Address Label
  property_count: 0
  slug: address_label
- name: Address Ownership Item
  property_count: 5
  slug: address_ownership_item
- name: Advanced
  property_count: 0
  slug: advanced
- name: Agree To Share With 3Rd Party
  property_count: 0
  slug: agree_to_share_with_3rd_party
- name: Amount
  property_count: 0
  slug: amount
- name: Api
  property_count: 0
  slug: api
- name: Api Key
  property_count: 11
  slug: api_key
- name: Api Key Default
  property_count: 0
  slug: api_key_default
- name: Api Key Enabled
  property_count: 0
  slug: api_key_enabled
- name: Api Key Features
  property_count: 0
  slug: api_key_features
- name: Api Key Name
  property_count: 0
  slug: api_key_name
- name: Api Limits
  property_count: 0
  slug: api_limits
- name: Ask Iv
  property_count: 0
  slug: ask_iv
- name: Asks
  property_count: 0
  slug: asks
- name: Average Price
  property_count: 0
  slug: average_price
- name: Beneficiary Address
  property_count: 0
  slug: beneficiary_address
- name: Beneficiary Company Name
  property_count: 0
  slug: beneficiary_company_name
- name: Beneficiary First Name
  property_count: 0
  slug: beneficiary_first_name
- name: Beneficiary Last Name
  property_count: 0
  slug: beneficiary_last_name
- name: Beneficiary Vasp Did
  property_count: 0
  slug: beneficiary_vasp_did
- name: Beneficiary Vasp Name
  property_count: 0
  slug: beneficiary_vasp_name
- name: Beneficiary Vasp Website
  property_count: 0
  slug: beneficiary_vasp_website
- name: Best Ask Amount
  property_count: 0
  slug: best_ask_amount
- name: Best Ask Price
  property_count: 0
  slug: best_ask_price
- name: Best Bid Amount
  property_count: 0
  slug: best_bid_amount
- name: Best Bid Price
  property_count: 0
  slug: best_bid_price
- name: Bid Iv
  property_count: 0
  slug: bid_iv
- name: Bids
  property_count: 0
  slug: bids
- name: Block Rfq
  property_count: 24
  slug: block_rfq
- name: Block Rfq Currency
  property_count: 0
  slug: block_rfq_currency
- name: Block Rfq For Maker
  property_count: 16
  slug: block_rfq_for_maker
- name: Block Rfq Hedge Leg
  property_count: 4
  slug: block_rfq_hedge_leg
- name: Block Rfq Legs
  property_count: 0
  slug: block_rfq_legs
- name: Block Rfq Quote
  property_count: 16
  slug: block_rfq_quote
- name: Block Rfq Time In Force
  property_count: 0
  slug: block_rfq_time_in_force
- name: Block Rfq Trade Tape Continuation
  property_count: 0
  slug: block_rfq_trade_tape_continuation
- name: Block Trade
  property_count: 6
  slug: block_trade
- name: Block Trade Id
  property_count: 0
  slug: block_trade_id
- name: Block Trade Id In Result
  property_count: 0
  slug: block_trade_id_in_result
- name: Block Trade Leg Count
  property_count: 0
  slug: block_trade_leg_count
- name: Block Trade Order
  property_count: 0
  slug: block_trade_order
- name: Block Trade Signature
  property_count: 0
  slug: block_trade_signature
- name: Book State
  property_count: 0
  slug: book_state
- name: Book Summary
  property_count: 23
  slug: book_summary
- name: Business Registration Number
  property_count: 0
  slug: business_registration_number
- name: Cancel Reason
  property_count: 0
  slug: cancel_reason
- name: Chart Volume
  property_count: 0
  slug: chart_volume
- name: Clearance State
  property_count: 0
  slug: clearance_state
- name: Client Id
  property_count: 0
  slug: client_id
- name: Client Secret
  property_count: 0
  slug: client_secret
- name: Cod Scope
  property_count: 0
  slug: cod_scope
- name: Combo
  property_count: 6
  slug: combo
- name: Combo Id
  property_count: 0
  slug: combo_id
- name: Combo Leg
  property_count: 2
  slug: combo_leg
- name: Combo Leg Amount
  property_count: 0
  slug: combo_leg_amount
- name: Combo State
  property_count: 0
  slug: combo_state
- name: Commission
  property_count: 0
  slug: commission
- name: Continuation
  property_count: 0
  slug: continuation
- name: Continuation With Null
  property_count: 0
  slug: continuation_with_null
- name: Contract Size
  property_count: 0
  slug: contract_size
- name: Contracts
  property_count: 0
  slug: contracts
- name: Currency
  property_count: 0
  slug: currency
- name: Currency Address
  property_count: 0
  slug: currency_address
- name: Currency Address Type
  property_count: 0
  slug: currency_address_type
- name: Currency Amount
  property_count: 0
  slug: currency_amount
- name: Currency Pair
  property_count: 0
  slug: currency_pair
- name: Currency Portfolio
  property_count: 10
  slug: currency_portfolio
- name: Currency Transaction Id
  property_count: 0
  slug: currency_transaction_id
- name: Currency With Any
  property_count: 0
  slug: currency_with_any
- name: Currency With Any And Grouped
  property_count: 0
  slug: currency_with_any_and_grouped
- name: Currency With Any And List
  property_count: 0
  slug: currency_with_any_and_list
- name: Currency With Apr
  property_count: 12
  slug: currency_with_apr
- name: Current Funding
  property_count: 0
  slug: current_funding
- name: Custody Account
  property_count: 11
  slug: custody_account
- name: Custody Log
  property_count: 6
  slug: custody_log
- name: Custody Name
  property_count: 0
  slug: custody_name
- name: Custody Settlement
  property_count: 8
  slug: custody_settlement
- name: Date
  property_count: 0
  slug: date
- name: Delivery Price
  property_count: 0
  slug: delivery_price
- name: Delta Total
  property_count: 0
  slug: delta_total
- name: Deposit
  property_count: 11
  slug: deposit
- name: Deposit State
  property_count: 0
  slug: deposit_state
- name: Did
  property_count: 0
  slug: did
- name: Direction
  property_count: 0
  slug: direction
- name: Display Amount
  property_count: 0
  slug: display_amount
- name: Enabled Field
  property_count: 0
  slug: enabled_field
- name: Estimated Delivery Price
  property_count: 0
  slug: estimated_delivery_price
- name: Estimated Liquidation Ratio
  property_count: 0
  slug: estimated_liquidation_ratio
- name: Execution Instruction
  property_count: 0
  slug: execution_instruction
- name: Expirations
  property_count: 2
  slug: expirations
- name: External Id
  property_count: 0
  slug: external_id
- name: Extra Currencies
  property_count: 0
  slug: extra_currencies
- name: Fee
  property_count: 0
  slug: fee
- name: Fee Balance
  property_count: 0
  slug: fee_balance
- name: Fee Role
  property_count: 0
  slug: fee_role
- name: Filled Amount
  property_count: 0
  slug: filled_amount
- name: Filled Amount Quote
  property_count: 0
  slug: filled_amount_quote
- name: Funding 8H
  property_count: 0
  slug: funding_8h
- name: Get Balance
  property_count: 7
  slug: get_balance
- name: Get Custody Balance
  property_count: 7
  slug: get_custody_balance
- name: Greeks
  property_count: 5
  slug: greeks
- name: Group Rate And Burst
  property_count: 4
  slug: group_rate_and_burst
- name: Id
  property_count: 0
  slug: id
- name: Implied Volatility
  property_count: 0
  slug: implied_volatility
- name: Implv
  property_count: 0
  slug: implv
- name: Index Name
  property_count: 0
  slug: index_name
- name: Index Name Derivative
  property_count: 0
  slug: index_name_derivative
- name: Index Name For Dvol
  property_count: 0
  slug: index_name_for_dvol
- name: Index Price
  property_count: 0
  slug: index_price
- name: Instrument
  property_count: 28
  slug: instrument
- name: Instrument Id
  property_count: 0
  slug: instrument_id
- name: Instrument Name
  property_count: 0
  slug: instrument_name
- name: Interest Rate
  property_count: 0
  slug: interest_rate
- name: Interest Value
  property_count: 0
  slug: interest_value
- name: Is Secondary Oto
  property_count: 0
  slug: is_secondary_oto
- name: Jurisdictions
  property_count: 0
  slug: jurisdictions
- name: Jwt
  property_count: 0
  slug: jwt
- name: Key Id
  property_count: 0
  slug: key_id
- name: Key Number Pair
  property_count: 2
  slug: key_number_pair
- name: Kind
  property_count: 0
  slug: kind
- name: Kind Future Or Option With Any
  property_count: 0
  slug: kind_future_or_option_with_any
- name: Kind With Any
  property_count: 0
  slug: kind_with_any
- name: Kind With Combo All
  property_count: 0
  slug: kind_with_combo_all
- name: Kind Without Spot
  property_count: 0
  slug: kind_without_spot
- name: Label
  property_count: 0
  slug: label
- name: Label Presentation
  property_count: 0
  slug: label_presentation
- name: Last Price
  property_count: 0
  slug: last_price
- name: Last Rfq Timestamp
  property_count: 0
  slug: last_rfq_timestamp
- name: Leg Structure
  property_count: 0
  slug: leg_structure
- name: Log Amount
  property_count: 0
  slug: log_amount
- name: Mark Iv
  property_count: 0
  slug: mark_iv
- name: Mark Price
  property_count: 0
  slug: mark_price
- name: Max Price
  property_count: 0
  slug: max_price
- name: Max Scope
  property_count: 0
  slug: max_scope
- name: Max Show
  property_count: 0
  slug: max_show
- name: Min Price
  property_count: 0
  slug: min_price
- name: Mobile
  property_count: 0
  slug: mobile
- name: Nonce
  property_count: 0
  slug: nonce
- name: Oco Ref
  property_count: 0
  slug: oco_ref
- name: Only Combo Kind
  property_count: 0
  slug: only_combo_kind
- name: Open Interest
  property_count: 0
  slug: open_interest
- name: Open Order Price
  property_count: 0
  slug: open_order_price
- name: Order
  property_count: 52
  slug: order
- name: Order Id
  property_count: 0
  slug: order_id
- name: Order Id Initial Margin Pair
  property_count: 3
  slug: order_id_initial_margin_pair
- name: Order State
  property_count: 0
  slug: order_state
- name: Order State In User Trade
  property_count: 0
  slug: order_state_in_user_trade
- name: Order State Stop
  property_count: 0
  slug: order_state_stop
- name: Order Type
  property_count: 0
  slug: order_type
- name: Order Type2
  property_count: 0
  slug: order_type2
- name: Orders
  property_count: 0
  slug: orders
- name: Original Order Type
  property_count: 0
  slug: original_order_type
- name: Pending Block Trade
  property_count: 12
  slug: pending_block_trade
- name: Personal Wallet
  property_count: 0
  slug: personal_wallet
- name: Pme Currency
  property_count: 0
  slug: pme_currency
- name: Portfolio
  property_count: 1
  slug: portfolio
- name: Position
  property_count: 23
  slug: position
- name: Position Direction
  property_count: 0
  slug: position_direction
- name: Position Move
  property_count: 1
  slug: position_move
- name: Position Move Trade
  property_count: 6
  slug: position_move_trade
- name: Position With Elp
  property_count: 0
  slug: position_with_elp
- name: Post Only
  property_count: 0
  slug: post_only
- name: Price
  property_count: 0
  slug: price
- name: Price Index
  property_count: 0
  slug: price_index
- name: Profit Loss
  property_count: 0
  slug: profit_loss
- name: Projected Delta Total
  property_count: 0
  slug: projected_delta_total
- name: Projected Initial Margin
  property_count: 0
  slug: projected_initial_margin
- name: Projected Maintenance Margin
  property_count: 0
  slug: projected_maintenance_margin
- name: Public Key
  property_count: 0
  slug: public_key
- name: Public Trade
  property_count: 18
  slug: public_trade
- name: Quantity
  property_count: 0
  slug: quantity
- name: Quote Asks
  property_count: 0
  slug: quote_asks
- name: Quote Bids
  property_count: 0
  slug: quote_bids
- name: Quote Direction
  property_count: 0
  slug: quote_direction
- name: Quote Price
  property_count: 0
  slug: quote_price
- name: Rate And Burst
  property_count: 2
  slug: rate_and_burst
- name: Reduce Only
  property_count: 0
  slug: reduce_only
- name: Refresh Amount
  property_count: 0
  slug: refresh_amount
- name: Reject Post Only
  property_count: 0
  slug: reject_post_only
- name: Replaced Quote
  property_count: 0
  slug: replaced_quote
- name: Requires Confirmation
  property_count: 0
  slug: requires_confirmation
- name: Requires Confirmation Change
  property_count: 0
  slug: requires_confirmation_change
- name: Responses
  property_count: 0
  slug: responses
- name: Result Count
  property_count: 0
  slug: result_count
- name: Role
  property_count: 0
  slug: role
- name: Rpl
  property_count: 0
  slug: rpl
- name: Scale Down
  property_count: 2
  slug: scale_down
- name: Security Key
  property_count: 6
  slug: security_key
- name: Security Key Assignments
  property_count: 0
  slug: security_key_assignments
- name: Security Key Id
  property_count: 0
  slug: security_key_id
- name: Security Key Last Used
  property_count: 0
  slug: security_key_last_used
- name: Security Key Name
  property_count: 0
  slug: security_key_name
- name: Security Key Timestamp
  property_count: 0
  slug: security_key_timestamp
- name: Security Key Type
  property_count: 0
  slug: security_key_type
- name: Settlement
  property_count: 14
  slug: settlement
- name: Settlement Currency With Any And Grouped
  property_count: 0
  slug: settlement_currency_with_any_and_grouped
- name: Settlement Price
  property_count: 0
  slug: settlement_price
- name: Settlement Type
  property_count: 0
  slug: settlement_type
- name: Side
  property_count: 0
  slug: side
- name: Simple Order Type
  property_count: 0
  slug: simple_order_type
- name: Sorting
  property_count: 0
  slug: sorting
- name: Source
  property_count: 0
  slug: source
- name: Stats
  property_count: 5
  slug: stats
- name: Status
  property_count: 0
  slug: status
- name: Tick Direction
  property_count: 0
  slug: tick_direction
- name: Tick Size Step
  property_count: 2
  slug: tick_size_step
- name: Time In Force
  property_count: 0
  slug: time_in_force
- name: Timestamp
  property_count: 0
  slug: timestamp
- name: Timestamp For Book Notifications
  property_count: 0
  slug: timestamp_for_book_notifications
- name: Trade Allocations
  property_count: 0
  slug: trade_allocations
- name: Trade Id
  property_count: 0
  slug: trade_id
- name: Trade Seq
  property_count: 0
  slug: trade_seq
- name: Trade Timestamp
  property_count: 0
  slug: trade_timestamp
- name: Trade Trigger
  property_count: 4
  slug: trade_trigger
- name: Trade Trigger State
  property_count: 0
  slug: trade_trigger_state
- name: Trades Volumes
  property_count: 13
  slug: trades_volumes
- name: Transaction Log
  property_count: 34
  slug: transaction_log
- name: Transfer Direction
  property_count: 0
  slug: transfer_direction
- name: Transfer Id
  property_count: 0
  slug: transfer_id
- name: Transfer Item
  property_count: 10
  slug: transfer_item
- name: Transfer Other Side
  property_count: 0
  slug: transfer_other_side
- name: Transfer State
  property_count: 0
  slug: transfer_state
- name: Transfer Type
  property_count: 0
  slug: transfer_type
- name: Trigger
  property_count: 0
  slug: trigger
- name: Trigger Fill Condition
  property_count: 0
  slug: trigger_fill_condition
- name: Trigger Offset
  property_count: 0
  slug: trigger_offset
- name: Trigger Order History Record
  property_count: 20
  slug: trigger_order_history_record
- name: Trigger Price
  property_count: 0
  slug: trigger_price
- name: Trigger Reference Price
  property_count: 0
  slug: trigger_reference_price
- name: Triggered
  property_count: 0
  slug: triggered
- name: Underlying Index
  property_count: 0
  slug: underlying_index
- name: Underlying Price
  property_count: 0
  slug: underlying_price
- name: Unhosted Wallet
  property_count: 0
  slug: unhosted_wallet
- name: Upl
  property_count: 0
  slug: upl
- name: Usd
  property_count: 0
  slug: usd
- name: User Change
  property_count: 4
  slug: user_change
- name: User Id
  property_count: 0
  slug: user_id
- name: User Trade
  property_count: 38
  slug: user_trade
- name: Username
  property_count: 0
  slug: username
- name: Vasp Item
  property_count: 3
  slug: vasp_item
- name: Vasp Name
  property_count: 0
  slug: vasp_name
- name: Volatility
  property_count: 0
  slug: volatility
- name: Volume Usd
  property_count: 0
  slug: volume_usd
- name: Waiting Timestamp
  property_count: 0
  slug: waiting_timestamp
- name: Wallet Address Type
  property_count: 0
  slug: wallet_address_type
- name: Wallet Currency
  property_count: 0
  slug: wallet_currency
- name: Web
  property_count: 0
  slug: web
- name: Withdrawal
  property_count: 12
  slug: withdrawal
- name: Withdrawal Policy Amount
  property_count: 0
  slug: withdrawal_policy_amount
- name: Withdrawal Policy Category
  property_count: 0
  slug: withdrawal_policy_category
- name: Withdrawal Policy Limit Bucket
  property_count: 0
  slug: withdrawal_policy_limit_bucket
- name: Withdrawal Policy Limit Buckets
  property_count: 2
  slug: withdrawal_policy_limit_buckets
- name: Withdrawal Policy Limits
  property_count: 1
  slug: withdrawal_policy_limits
- name: Withdrawal Policy Mode
  property_count: 0
  slug: withdrawal_policy_mode
- name: Withdrawal State
  property_count: 0
  slug: withdrawal_state
jsonld:
- class_count: 406
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-06-13'
name: Deribit
nav: Providers
network: true
overview: 'Deribit publishes 18 APIs on the [APIs.io](https://apis.io/) network, including WebSocket API, Account Management API, Authentication API, and 15 more. Tagged areas include Derivatives, Cryptocurrency, Bitcoin, Ethereum, and Options.


  The Deribit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Deribit''s developer surface includes authentication, engineering blog, developer portal, status page, support, developer console, changelog, and 10 more developer resources.'
plans:
- name: Plans
  plan_count: 7
  slug: plans
random_paper: 25
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Deribit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: deribit-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.1
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 58.4
    developer_ergonomics: 32.6
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 15.8
  previous_composite: 54.1
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deribit/refs/heads/main/screenshots/deribit-2026-06-20T175930.png
security:
- kind: authentication
  name: Deribit Authentication
  slug: deribit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Deribit Domain Security
  slug: deribit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deribit
tags:
- Derivatives
- Cryptocurrency
- Bitcoin
- Ethereum
- Options
- Futures
- Perpetuals
- Trading
- Market Data
- Block Trading
- WebSocket
- Financial
website: https://insights.deribit.com/dev-hub/
---
