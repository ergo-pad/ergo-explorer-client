# UOutputInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**box_id** | **str** | Id of the box | 
**transaction_id** | **str** | Id of the transaction that created the box | 
**value** | **int** | Value of the box in nanoERG | 
**index** | **int** | Index of the output in a transaction | 
**creation_height** | **int** | Height at which the box was created | 
**ergo_tree** | **str** | Serialized ergo tree | 
**address** | **str** | An address derived from ergo tree | 
**assets** | [**list[AssetInstanceInfo]**](AssetInstanceInfo.md) |  | [optional] 
**additional_registers** | **dict(str, str)** |  | 
**spent_transaction_id** | **str** | Id of the transaction this output was spent by | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

