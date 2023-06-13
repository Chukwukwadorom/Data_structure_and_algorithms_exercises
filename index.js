
// Javascript implementation of algorithms


function validAnagram(arr1, arr2){
   
    if (arr1.length !== arr2.length)
      {return false;}
  
  
     let freq_dict1 = {}
     let  freq_dict2 = {}
  
      for(let chr of arr1){
          if (chr in  freq_dict1)
              {freq_dict1[chr] += 1}
          else
              {freq_dict1[chr] = 1}}
              
              
      for(let chr of arr2){
          if (chr in freq_dict2)
              {freq_dict2[chr] += 1}
          else
              {freq_dict2[chr] = 1}}
              
      
  
      for (let chr in freq_dict1){
          if(!(chr in freq_dict2))
              {return false}
          else if (freq_dict1[chr] !== freq_dict2[chr])
              return false}
  
      return true   
  }


// console.log(validAnagram('', '')) 
// console.log(validAnagram('aaz', 'zza')) 
// console.log(validAnagram('anagram', 'nagaram'))
// console.log(validAnagram("rat","car")) 
// console.log(validAnagram('awesome', 'awesom'))
// console.log(validAnagram('qwerty', 'qeywrt')) 
// console.log(validAnagram('texttwisttime', 'timetwisttext'))



function countUniqueValues_multi_pointer(arr){
    // count unique values using pointer, altering the list. time complexity:O(N)
    // this method presupposes that the list is sorted
    
    if (arr.length == 0)
        return 0


    let left_pointer = 0
    let right_pointer = 1

    while (right_pointer !== arr.length) 
    {
        if (arr[right_pointer]!== arr[left_pointer])
        {
            left_pointer += 1
            arr[left_pointer] = arr[right_pointer]
        }
        right_pointer++
    }
           
    return [left_pointer+1, arr.slice(0,left_pointer+1)] 

}

 
// console.log("...................using multi pointer..................")

// console.log("counting unique values using multi pointer:", countUniqueValues_multi_pointer([1,1,1,1,1,2]))
// console.log("counting unique values using multi pointer:", countUniqueValues_multi_pointer([1,2,3,4,4,4,7,7,12,12,13]))
// console.log("counting unique values using multi pointer:", countUniqueValues_multi_pointer([]))
// console.log("counting unique values using multi pointer:", countUniqueValues_multi_pointer([-2,-1,-1,0,1]))


// slidding windows. return the maximum in a consecutive sequence of number
function max_subarray_sum(arr, n){
    if (arr.length === 0 || n > arr.length)
            return null
    running_sum = 0
    for(let x=0; x<n; x++)
        running_sum+= arr[x]
    
    max_sum = running_sum

    for(let index =n; index<arr.length; index++)
    {
        running_sum = (running_sum + arr[index]) - arr[index-n]
        if (running_sum > max_sum)
            max_sum = running_sum 
    }

return max_sum
}


console.log("........................a better implemtation...............................")
console.log(max_subarray_sum([1,2,5,2,8,1,5],2)) 
console.log(max_subarray_sum([1,2,5,2,8,1,5],4)) 
console.log(max_subarray_sum([4,2,1,6],1))
console.log(max_subarray_sum([4,2,1,6,2],4)) 
console.log(max_subarray_sum([],4))