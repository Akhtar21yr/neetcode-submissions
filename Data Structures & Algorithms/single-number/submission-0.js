class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    singleNumber(nums) {
        const obj = {}
        for (let i =0;i<nums.length;i++){
            obj[nums[i]] = (obj[nums[i]] || 0) + 1
        }
        console.log(obj)
        for (let i in obj){
            if (obj[i] == 1) {
                return i
            }
        }
    }
}
