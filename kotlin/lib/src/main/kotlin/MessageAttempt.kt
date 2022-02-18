package com.svix.kotlin

import com.svix.kotlin.exceptions.ApiException
import com.svix.kotlin.internal.apis.MessageAttemptApi
import com.svix.kotlin.models.ListResponseEndpointMessageOut
import com.svix.kotlin.models.ListResponseMessageAttemptEndpointOut
import com.svix.kotlin.models.ListResponseMessageAttemptOut
import com.svix.kotlin.models.ListResponseMessageEndpointOut
import com.svix.kotlin.models.MessageAttemptOut

class MessageAttempt internal constructor(token: String, options: SvixOptions) {
    val api = MessageAttemptApi(options.serverUrl)

    init {
        api.accessToken = token
        api.userAgent = options.getUA()
    }

    /**
     * @deprecated use listByMsg or listByEndpoint instead.
     */
    @Deprecated(message = "use listByMsg or listByEndpoint instead.")
    suspend fun list(appId: String, msgId: String, options: MessageAttemptListOptions = MessageAttemptListOptions()): ListResponseMessageAttemptOut {
        return this.listByMsg(appId, msgId, options)
    }

    suspend fun listByMsg(appId: String, msgId: String, options: MessageAttemptListOptions = MessageAttemptListOptions()): ListResponseMessageAttemptOut {
        try {
            return api.listAttemptedDestinationsByMsgApiV1AppAppIdAttemptMsgMsgIdGet(
                appId,
                msgId,
                null,
                options.iterator,
                options.limit,
                options.messageStatus,
                null,
                null,
                options.before,
                null,
            )
        } catch (e: Exception) {
            throw ApiException.wrap(e)
        }
    }

    suspend fun listByEndpoint(appId: String, endpointId: String, options: MessageAttemptListOptions = MessageAttemptListOptions()): ListResponseMessageAttemptOut {
        try {
            return api.listAttemptedDestinationsByEndpointApiV1AppAppIdAttemptEndpointEndpointIdGet(
                appId,
                endpointId,
                options.iterator,
                options.limit,
                options.messageStatus,
                null,
                null,
                options.before,
                null,
            )
        } catch (e: Exception) {
            throw ApiException.wrap(e)
        }
    }

    suspend fun get(appId: String, msgId: String, attemptId: String): MessageAttemptOut {
        try {
            return api.getAttemptApiV1AppAppIdMsgMsgIdAttemptAttemptIdGet(attemptId, msgId, appId, null)
        } catch (e: Exception) {
            throw ApiException.wrap(e)
        }
    }

    suspend fun resend(appId: String, msgId: String, endpointId: String) {
        try {
            api.resendWebhookApiV1AppAppIdMsgMsgIdEndpointEndpointIdResendPost(endpointId, msgId, appId, null)
        } catch (e: Exception) {
            throw ApiException.wrap(e)
        }
    }

    suspend fun listAttemptedMessages(
        appId: String,
        endpointId: String,
        options: MessageAttemptListOptions = MessageAttemptListOptions()
    ): ListResponseEndpointMessageOut {
        try {
            return api.listAttemptedMessagesApiV1AppAppIdEndpointEndpointIdMsgGet(
                endpointId,
                appId,
                options.iterator,
                options.limit,
                options.messageStatus,
                options.before,
                null
            )
        } catch (e: Exception) {
            throw ApiException.wrap(e)
        }
    }

    suspend fun listAttemptedDestinations(
        appId: String,
        msgId: String,
        options: MessageAttemptListOptions = MessageAttemptListOptions()
    ): ListResponseMessageEndpointOut {
        try {
            return api.listAttemptedDestinationsApiV1AppAppIdMsgMsgIdEndpointGet(
                msgId,
                appId,
                options.iterator,
                options.limit,
                null
            )
        } catch (e: Exception) {
            throw ApiException.wrap(e)
        }
    }

    suspend fun listAttemptsForEndpoint(
        appId: String,
        endpointId: String,
        msgId: String,
        options: MessageAttemptListOptions = MessageAttemptListOptions()
    ): ListResponseMessageAttemptEndpointOut {
        return try {
            api.listAttemptsForEndpointApiV1AppAppIdMsgMsgIdEndpointEndpointIdAttemptGet(
                msgId,
                appId,
                endpointId,
                options.iterator,
                options.limit,
                options.eventTypes,
                null,
                options.messageStatus,
                options.before,
                null
            )
        } catch (e: Exception) {
            throw ApiException.wrap(e)
        }
    }
}
