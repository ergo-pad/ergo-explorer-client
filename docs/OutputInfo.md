# OutputInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**box_id** | **str** | Id of the box | 
**transaction_id** | **str** | Id of the transaction that created the box | 
**block_id** | **str** | Id of the block a box included in | 
**value** | **int** | Value of the box in nanoERG | 
**index** | **int** | Index of the output in a transaction | 
**global_index** | **int** | Global index of the output in the blockchain | 
**creation_height** | **int** | Height at which the box was created | 
**settlement_height** | **int** | Height at which the box got fixed in blockchain | 
**ergo_tree** | **str** | Serialized ergo tree | 
**address** | **str** | An address derived from ergo tree | 
**assets** | [**list[AssetInstanceInfo]**](AssetInstanceInfo.md) |  | [optional] 
**additional_registers** | **dict(str, str)** |  | 
**spent_transaction_id** | **str** | Id of the transaction this output was spent by | [optional] 
**main_chain** | **bool** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

