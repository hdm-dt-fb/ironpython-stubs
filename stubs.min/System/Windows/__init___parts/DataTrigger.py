class DataTrigger(TriggerBase,IAddChild):
 """
 Represents a trigger that applies property values or performs actions when the bound data meets a specified condition.
 
 DataTrigger()
 """
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: DependencyObject,e: DependencyPropertyChangedEventArgs)
   Invoked whenever the effective value of any dependency property on this 
    System.Windows.DependencyObject has been updated. The specific dependency 
    property that changed is reported in the event data.
  
  
   e: Event data that will contain the dependency property identifier of interest,
    the property metadata for the type,and old and new values.
  
  OnPropertyChanged(self: Window_16$17,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Label_17$18,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: TextBox_18$19,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Button_19$20,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: CheckBox_20$21,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: ComboBox_21$22,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Separator_22$23,e: DependencyPropertyChangedEventArgs)
  """
  pass
 @staticmethod
 def ReceiveMarkupExtension(targetObject,eventArgs):
  """
  ReceiveMarkupExtension(targetObject: object,eventArgs: XamlSetMarkupExtensionEventArgs)
   Handles cases where a markup extension provides a value for a property of a 
    System.Windows.DataTrigger object.
  
  
   targetObject: The object where the markup extension sets the value.
   eventArgs: Data that is relevant for markup extension processing.
  """
  pass
 def ShouldSerializeProperty(self,*args):
  """
  ShouldSerializeProperty(self: DependencyObject,dp: DependencyProperty) -> bool
  
   Returns a value that indicates whether serialization processes should serialize 
    the value for the provided dependency property.
  
  
   dp: The identifier for the dependency property that should be serialized.
   Returns: true if the dependency property that is supplied should be value-serialized; 
    otherwise,false.
  
  ShouldSerializeProperty(self: Window_16$17,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Label_17$18,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: TextBox_18$19,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Button_19$20,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: CheckBox_20$21,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: ComboBox_21$22,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Separator_22$23,dp: DependencyProperty) -> bool
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Binding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the binding that produces the property value of the data object.

Get: Binding(self: DataTrigger) -> BindingBase

Set: Binding(self: DataTrigger)=value
"""

 Setters=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of System.Windows.Setter objects,which describe the property values to apply when the data item meets the specified condition.

Get: Setters(self: DataTrigger) -> SetterBaseCollection

"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value to be compared with the property value of the data object.

Get: Value(self: DataTrigger) -> object

Set: Value(self: DataTrigger)=value
"""


