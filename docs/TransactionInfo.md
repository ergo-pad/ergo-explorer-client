# TransactionInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Transaction ID | 
**block_id** | **str** | ID of the corresponding header | 
**inclusion_height** | **int** | Height of the block the transaction was included in | 
**timestamp** | **int** | Timestamp the transaction got into the network | 
**index** | **int** | Index of a transaction inside a block | 
**global_index** | **int** | global index of a transaction in the blockchain | 
**num_confirmations** | **int** | Number of transaction confirmations | 
**inputs** | [**list[InputInfo]**](InputInfo.md) |  | [optional] 
**data_inputs** | [**list[DataInputInfo]**](DataInputInfo.md) |  | [optional] 
**outputs** | [**list[OutputInfo]**](OutputInfo.md) |  | [optional] 
**size** | **int** | Transaction size in bytes | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

