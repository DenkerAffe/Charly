from functions import *

commands = {
	# Stack manipulation
	"_" : IDuplicateTopStackItem,
	";" : IDiscardTopStackItem,
	"/" : ISwapTopStackItems,
	"$" : ICopyStackItem,
	"@" : IRotateTopStack,
	
	# String processing
	"A" : ISortAsc,
	"D" : ISortDesc,
	"e" : IEval,
	"k" : ISwapCase,
	"o" : ISort,
	"R" : IReplace,
	"r" : IReverse,
	"s" : IStrip,
	"u" : IUppercase,
	"w" : IWrap,	
	"*" : IMultiply,	
	"-" : IRemove,
	"+" : IConcatenate,
	":" : ISlice,
	
	# Functional programming
	"#" : IExecuteCommands,
	"~" : IApplyToChars,
	"%" : IApplyToParts,
	"?" : IApplyToPartsRandomly,	
	"a" : ISortAscWithKey,	
	"d" : ISortDescWithKey,
}
