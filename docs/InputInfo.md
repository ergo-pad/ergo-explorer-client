# InputInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**box_id** | **str** | ID of the corresponding box | 
**value** | **int** | Number of nanoErgs in the corresponding box | 
**index** | **int** | Index of the input in a transaction | 
**spending_proof** | **str** | Hex-encoded serialized sigma proof | [optional] 
**output_block_id** | **str** | Modifier ID | 
**output_transaction_id** | **str** | ID of the transaction outputting corresponding box | 
**output_index** | **int** | Index of the output corresponding this input | 
**output_global_index** | **int** | Global index of the output corresponding this input | 
**output_created_at** | **int** | Height the output corresponding this input was created at | 
**output_settled_at** | **int** | Height the output corresponding this input was settled at | 
**ergo_tree** | **str** | Hex-encoded string | 
**address** | **str** | Decoded address of the corresponding box holder | 
**assets** | [**list[AssetInstanceInfo]**](AssetInstanceInfo.md) |  | [optional] 
**additional_registers** | **dict(str, str)** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

