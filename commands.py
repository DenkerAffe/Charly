from functions import *

commands = {
	"A" : ISortAsc,
	"a" : ISortAscWithKey,
	"c" : ICountOccurences,
	"C" : ISplit,
	"D" : ISortDesc,
	"d" : ISortDescWithKey,
	"e" : IEval,
	"h" : IFirstChar,
	"i" : IInsert,
	"j" : IJoin,
	"k" : ISwapCase,
	"l" : ILowerCase,
	"o" : ISort,
	"R" : IReplace,
	"r" : IReverse,
	"s" : IStrip,
	"t" : ILength,
	"u" : IUpperCase,
	"v" : ILastChar,
	"w" : IWrap,
	"x" : IRemoveWithRegex,
	"y" : IAllButFirstChar,
	"z" : IAllButLastChar,
	"*" : IRepeat,
	"-" : IRemove,
	"+" : IConcatenate,
	":" : ISlice,
	"<" : IFirstChars,
	">" : ILastChars,
	"_" : IDuplicateTopStackItem,
	";" : IDiscardTopStackItem,
	"/" : ISwapTopStackItems,
	"$" : ICopyStackItem,
	"@" : IRotateTopStack,
	"#" : IExecuteCommands,
	"~" : IApplyToChars,
	"%" : IApplyToParts,
	"?" : IApplyToPartsRandomly,
}
